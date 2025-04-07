# app/rag_engine.py
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_core.runnables import RunnableSequence

from dotenv import load_dotenv
from pathlib import Path
import os

VECTOR_PATH = "data/vectors"

if not Path(VECTOR_PATH).exists():
    raise FileNotFoundError(f"❌ 벡터 저장소가 존재하지 않습니다: {VECTOR_PATH}\n먼저 문서를 업로드하고 벡터를 생성해 주세요.")

# API 키 환경 변수로 관리 (보안!)
load_dotenv()  # .env 파일에서 환경변수 로딩
api_key = os.environ["OPENAI_API_KEY"]

try:
    api_key = os.environ["OPENAI_API_KEY"]
    print(f"✅ 키 확인 완료: {api_key[:5]}...******")
except KeyError:
    print("❌ OPENAI_API_KEY 환경변수가 설정되지 않았습니다.")

    

# 초기 세팅 (임베딩 모델, 검색 DB, LLM)
embedding_model = OpenAIEmbeddings(openai_api_key=api_key)
vector_store = FAISS.load_local("data/vectors", embeddings=embedding_model, allow_dangerous_deserialization=True)
retriever = vector_store.as_retriever(search_kwargs={"k": 2})  # 검색 문서 개수 줄이기
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.2,
    max_tokens=300,
    openai_api_key=api_key
)

# LangChain QA 체인 구성
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",  # simple prompt
    retriever=retriever,
    return_source_documents=False  # 응답만 받고 싶다면
)

def generate_answer_from_rag(question: str) -> str:
    result = qa_chain.run(question)
    return result
