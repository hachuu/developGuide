# app/generate_vector_store.py
from langchain_openai import OpenAIEmbeddings  # 설치 필요
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    print("❌ OPENAI_API_KEY가 설정되지 않았습니다.")
    exit()

print(f"✅ API 키 시작: {api_key[:5]}...******")

embedding_model = OpenAIEmbeddings(openai_api_key=api_key)

# 1. 문서 로드
doc_path = "data/raw_docs/sample.txt"
if not os.path.exists(doc_path):
    print(f"❌ 문서 파일 없음: {doc_path}")
    exit()

loader = TextLoader(doc_path, encoding="utf-8")
documents = loader.load()
print(f"✅ 문서 {len(documents)}개 로드")

# 2. Chunk 분할
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)
print(f"✅ Chunk {len(docs)}개 생성")

# 3. 벡터 생성 및 저장
vector_store = FAISS.from_documents(docs, embedding_model)
os.makedirs("data/vectors", exist_ok=True)
vector_store.save_local("data/vectors")
print("✅ 벡터 저장 완료! data/vectors 폴더 확인")
