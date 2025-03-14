# AI RAG (Retrieval-Augmented Generation) 개념을 연동하는 Azure Function App
- Azure Functions 기반으로 AI RAG (Retrieval-Augmented Generation) 개념을 연동하는 가벼운 아키텍처 설계

## 아키텍처 구성 : 최소한의 Azure 서비스만 사용하면서도 RAG 개념을 적용할 수 있도록 설계
1. Azure Functions (API Gateway 역할)
- HTTP 트리거 기반의 서버리스 API
- OpenAI API 호출 및 벡터 검색 처리
- 비용 최적화를 위해 Consumption Plan 사용 가능
2. Azure AI Search (벡터 검색)
- 문서 임베딩 저장 및 검색
- Azure OpenAI의 text-embedding-ada-002 모델 활용
3. Azure Blob Storage (데이터 저장소, 선택 사항)
- PDF, TXT 등 문서 저장
- Azure Functions에서 필요할 때 불러와 처리
4. Azure OpenAI (GPT 모델 사용)
- 벡터 검색 결과를 기반으로 프롬프트 생성
- ChatGPT 또는 GPT-4 모델 호출
  
## 데이터 흐름
- 사용자가 Azure Function API 호출
- 입력 텍스트를 Azure AI Search에서 벡터 검색
- 검색된 문서를 바탕으로 OpenAI GPT 모델 호출
- 응답을 사용자에게 반환

## 배포 및 확장성
- Azure Functions는 HTTP 트리거로 API 역할을 수행하며, 필요할 때만 실행되어 비용 절감
- Azure AI Search는 벡터 인덱스를 관리하여 빠른 검색 지원
- Blob Storage를 활용하면 대용량 데이터 저장 가능


### 추가 구성 (optional)
- 더 확장하려면 Azure Kubernetes Service (AKS)나 Azure Machine Learning을 추가할 수도 있음


# Python 소스 레벨 구현 (Azure Function App을 기반으로 RAG(Retrieval-Augmented Generation)를 구현하는 가벼운 아키텍처 코드)

## RAG 관련 라이브러리
1. langchain: LLM과 벡터 검색을 쉽게 연결
2. faiss: 빠른 벡터 검색을 위한 라이브러리
3. openai: OpenAI API 호출


## Azure Functions + FAISS + OpenAI 기반의 RAG 아키텍처를 구현
### 1. 프로젝트 구조
```plaintext
rag-azure-function/
│── function_app.py   # Azure Function 엔트리포인트
│── embeddings.py     # 문서 임베딩 처리
│── vector_store.py   # FAISS 기반 벡터 검색
│── requirements.txt  # 필요한 라이브러리 목록
```
### 2. 코드 구현
(1) requirements.txt - 필요한 패키지
```txt
azure-functions
openai
langchain
faiss-cpu
```
(2) embeddings.py - 문서 임베딩 처리
```python
import openai
import numpy as np

openai.api_key = "YOUR_OPENAI_API_KEY"

def get_embedding(text: str):
    """OpenAI API를 사용해 텍스트 임베딩 벡터를 반환"""
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=text
    )
    return np.array(response["data"][0]["embedding"])
```
(3) vector_store.py - FAISS 기반 벡터 검색
```python
import faiss
import numpy as np

# 임베딩 벡터 저장소 (FAISS IndexFlatL2 사용)
dimension = 1536  # OpenAI Embedding 차원
index = faiss.IndexFlatL2(dimension)
documents = []  # 원본 문서 저장

def add_document(text: str, embedding: np.array):
    """문서를 FAISS 벡터 DB에 추가"""
    index.add(np.array([embedding], dtype=np.float32))
    documents.append(text)

def search(query_embedding: np.array, top_k: int = 3):
    """FAISS를 사용해 가장 유사한 문서 검색"""
    distances, indices = index.search(np.array([query_embedding], dtype=np.float32), top_k)
    results = [documents[i] for i in indices[0] if i < len(documents)]
    return results
```
(4) function_app.py - Azure Function API
```python
import azure.functions as func
import json
from embeddings import get_embedding
from vector_store import search
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_response(query: str):
    """벡터 검색 후 OpenAI GPT 호출"""
    query_embedding = get_embedding(query)
    relevant_docs = search(query_embedding, top_k=3)

    prompt = f"다음 문서를 참고하여 질문에 답하세요:\n{relevant_docs}\n\n질문: {query}\n답변:"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

# Azure Function 엔드포인트
def main(req: func.HttpRequest) -> func.HttpResponse:
    req_body = req.get_json()
    query = req_body.get("query")

    if not query:
        return func.HttpResponse(json.dumps({"error": "Query is required"}), status_code=400)

    response = generate_response(query)
    return func.HttpResponse(json.dumps({"response": response}), mimetype="application/json")
```
### 3. 실행 방법
- Azure Function Core Tools 설치
```sh
npm install -g azure-functions-core-tools
```
- 로컬에서 실행
```sh
func start
```
- 테스트 요청 (POST 요청)
```sh
curl -X POST http://localhost:7071/api/function_app -H "Content-Type: application/json" -d '{"query": "Azure Functions란?"}'
```
### 4. 아키텍처 개요
1. 사용자가 질문을 Azure Function으로 요청
2. Azure Function이 FAISS 벡터 DB에서 관련 문서 검색
3. 검색된 문서를 기반으로 OpenAI GPT 호출
4. 결과를 JSON 형태로 반환

-> 실제 배포 시에는 Azure AI Search를 활용해 FAISS를 대체하면 더욱 확장성이 좋아질 수 있습니다.

# 활용된 library에 대한 기능 정의

## . RAG 개념에서 langchain과 faiss-cpu의 역할
- RAG(Retrieval-Augmented Generation)에서는 정보 검색(Retrieval)과 생성(Generation) 두 단계가 중요합니다.
각 라이브러리는 이 과정에서 다음과 같은 역할을 합니다.

### 1. langchain - RAG의 오케스트레이션 (Orchestration)
- langchain은 RAG의 핵심 흐름을 쉽게 구성하도록 도와주는 라이브러리입니다.
- 주요 역할:
  - ✅ 벡터 데이터베이스 연동 (FAISS, Pinecone, Azure AI Search 등)
  - ✅ 문서 처리 (PDF, TXT, CSV 등 다양한 문서에서 텍스트 추출)
  - ✅ 프롬프트 생성 (검색된 문서를 LLM에 전달할 최적의 형태로 변환)
  - ✅ LLM 호출 (OpenAI, Azure OpenAI 등 다양한 모델과 연동 가능)

- 🔹 RAG에서 langchain이 하는 일:
  - 사용자의 입력을 받아 벡터 검색을 수행
  - 검색된 문서를 활용해 LLM이 이해할 수 있는 프롬프트 생성
  - OpenAI, Hugging Face 같은 LLM 모델을 호출
- 🔹 예제: FAISS와 함께 사용하기

```python
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

# OpenAI API 키 설정
import openai
openai.api_key = "YOUR_OPENAI_API_KEY"

# 텍스트 임베딩 변환
embedding_model = OpenAIEmbeddings(model="text-embedding-ada-002")

# FAISS를 벡터 검색 엔진으로 사용
vector_db = FAISS.load_local("faiss_index", embedding_model)

# 검색 실행
query = "Azure Functions란?"
docs = vector_db.similarity_search(query, k=3)  # 가장 관련 있는 3개 문서 검색

for doc in docs:
    print(doc.page_content)
```
### 2. faiss-cpu - 빠른 벡터 검색 (Retrieval)
- faiss-cpu는 대량의 문서 데이터에서 가장 유사한 정보(벡터)를 빠르게 검색할 수 있도록 하는 라이브러리입니다.
- FAISS는 Facebook AI Research에서 개발한 고성능 벡터 검색 라이브러리로, GPU를 사용할 수도 있지만, 경량 서비스에서는 faiss-cpu를 많이 사용합니다.

- 주요 역할:
  - ✅ 대량의 벡터를 빠르게 검색 (유사도 기반 검색)
  - ✅ 고차원 데이터(임베딩 벡터) 검색 최적화
  - ✅ 메모리 내 인덱싱을 통해 빠른 검색 속도 제공

- 🔹 RAG에서 faiss-cpu가 하는 일:
  - 텍스트 데이터를 벡터(숫자 배열)로 변환해 저장
  - 사용자의 질문을 벡터로 변환 후, 가장 유사한 문서를 빠르게 검색
  - 검색된 문서를 LLM에게 전달하여 답변 생성
- 🔹 FAISS 사용 예제

```python
import faiss
import numpy as np

# 벡터 차원 (예: OpenAI Embedding = 1536차원)
dimension = 1536

# L2 거리 기반 벡터 검색 인덱스 생성
index = faiss.IndexFlatL2(dimension)

# 예제 문서 3개 (벡터 값은 가상의 숫자로 대체)
doc_vectors = np.random.rand(3, dimension).astype("float32")
index.add(doc_vectors)  # 벡터 데이터 저장

# 검색할 질문을 벡터로 변환 (가상의 벡터 사용)
query_vector = np.random.rand(1, dimension).astype("float32")

# 검색 실행 (가장 가까운 2개 문서 반환)
distances, indices = index.search(query_vector, k=2)

print(f"가장 유사한 문서 인덱스: {indices}")
print(f"각 문서와의 거리: {distances}")
```
## 정리 - langchain과 faiss-cpu의 역할 비교

| 라이브러리 | 역할 | 주요 기능 |
|------------|------|-----------|
| **langchain** | RAG 전체 워크플로 관리 | - 벡터 검색 엔진 연동 (FAISS, Pinecone, Azure AI Search) <br>- 문서에서 텍스트 추출 및 처리 <br>- LLM 프롬프트 자동 생성 <br>- OpenAI API 호출 |
| **faiss-cpu** | 빠른 벡터 검색 | - 텍스트 임베딩 벡터 저장 <br>- 유사도 검색 수행 <br>- L2 거리 기반 벡터 인덱싱 |

  
## 📌 한 문장 요약
- langchain → RAG의 전체 흐름을 조율하는 오케스트레이터
- faiss-cpu → 빠른 벡터 검색을 수행하는 데이터베이스
