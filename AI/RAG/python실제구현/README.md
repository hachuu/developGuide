# Python3 + RAG (AI) 기술 연동 웹앱서비스 구현
- 작업 순서 그냥 작성 (정리 안되어 있음)

## 환경 세팅
### 1. python version 확인
```
py --version
=>Python 3.11.2
```
### 2. 경로 생성
```
mkdir rag_webapp
cd rag_webapp
```
### 3. 가상환경 생성 및 실행 - vscode terminal에서 실행
```
python -m venv venv
>> venv\Scripts\activate  # Windows 기준
```
- 안되는 경우 이렇게 진행하라고 하는데 나는 terminal, cmd, bash에서 안되다가 그냥 vscode에서 함
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
### 4. 필수 패키지 설치 (새로운 vscode terminal)
```
pip install openai langchain faiss-cpu streamlit tiktoken unstructured
```
### 5. 기본 디렉토리 구성
```bash
rag_webapp/
├── app/                 # 뇌
│   ├── main.py          # 전체 백엔드 진입점. 필요한 함수 호출하고 연결
│   ├── rag_engine.py    # 핵심 RAG 처리 로직: 문서 chunk, 임베딩, 검색, 응답 생성 등
│   ├── vector_store.py  # 벡터 저장소 관리 (FAISS, Chroma 등)
│   └── utils.py         # 텍스트 추출, 정제, 시간 포맷 등 유틸 함수들
├── data/
│   ├── raw_docs/        # 원본 문서
│   └── vectors/         # 벡터 임베딩 저장
├── frontend/            # 얼굴
│   └── app.py           # Streamlit UI 웹앱 진입점. 사용자 입력 받고 app/의 함수 호출해서 결과 표시
└── requirements.txt
```
```
mkdir app, frontend, data
mkdir -p data\raw_docs, data\vectors
New-Item app\main.py -ItemType File
New-Item app\rag_engine.py -ItemType File
New-Item app\vector_store.py -ItemType File
New-Item app\utils.py -ItemType File
New-Item frontend\app.py -ItemType File
```

## 개발 (드디어..)

### ✅ 개발 단계
  - 1️⃣	Streamlit으로 간단한 UI 틀 만들기 (frontend/app.py)
  - 2️⃣	문서 업로드 → 텍스트 추출 (unstructured)
  - 3️⃣	텍스트 → chunk → embedding → vector 저장 (rag_engine.py, vector_store.py)
  - 4️⃣	질문 입력 → 유사 문서 검색 → LLM 응답 생성
  - 5️⃣	전체 통합해서 실사용 가능한 서비스 완성!

### 구현
1. backend api 설치
```
pip install fastapi uvicorn
```
2. /app/main.py 소스
```
from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

# 질문 요청 형식 정의
class QuestionRequest(BaseModel):
    question: str

# 샘플 응답 로직
@app.post("/api/ask")
async def ask_question(req: QuestionRequest):
    question = req.question
    # TODO: 여기서 RAG 처리 로직 연결 예정
    answer = f"'{question}'에 대한 응답입니다. (예시)"
    return {"answer": answer}
```
2. main.py 실행 명령어
```
uvicorn app.main:app --reload
```
3. postman으로 api 호출해보기
```
// 주소 : http://localhost:8000/api/ask
// post
// request
{
    "question": "입력..."
}
```
4. 명령어 실행 - 새로운 vscode terminal에서 실행
```
pip install openai langchain faiss-cpu tiktoken
```
5. rag engine.py
```
# app/rag_engine.py
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS  # 또는 Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import os

# API 키 환경 변수로 관리 (보안!)
os.environ["OPENAI_API_KEY"] = "your-api-key-here"

# 초기 세팅 (임베딩 모델, 검색 DB, LLM)
embedding_model = OpenAIEmbeddings()
vector_store = FAISS.load_local("data/vectors", embeddings=embedding_model)
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)

# LangChain QA 체인 구성
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",  # simple prompt
    retriever=vector_store.as_retriever()
)

def answer_question(question: str) -> str:
    result = qa_chain.run(question)
    return result

```
6. main.py에서 langchain 쪽 소스 연결
```
# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from .rag_engine import answer_question  # rag_engine 함수 임포트

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.post("/api/ask")
async def ask_question(req: QuestionRequest):
    try:
        answer = answer_question(req.question)
        return {"answer": answer}
    except Exception as e:
        return {"error": str(e)}

```
7. 실행
```
uvicorn app.main:app --reload
```
8. 
9. 
