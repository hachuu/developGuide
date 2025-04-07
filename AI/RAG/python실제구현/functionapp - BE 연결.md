# 🎯 최종 목표
1. Azure Function App에 Python 코드 배포
2. /api/ask 엔드포인트로 질문 받아서 LangChain + OpenAI로 응답 생성
3. 나중에 FE에서 POST 요청만 하면 끝!

## ✅ 1단계: Azure Functions Core Tools 설치 (로컬 개발용)
1. 설치 (윈도우 기준):
```bash
npm install -g azure-functions-core-tools@4 --unsafe-perm true
```
2. 설치 확인:
```bash
func --version
```
## ✅ 2단계: 함수 앱 프로젝트 생성
```bash
func init rag_function_app --python
cd rag_function_app
func new --name ask --template "HTTP trigger" --authlevel "anonymous"
```
- 이렇게 하면 폴더 구조가 생깁니다:
```pgsql
rag_function_app/
├── ask/
│   ├── __init__.py     ← 질문 처리 함수
│   └── function.json   ← HTTP 설정
├── requirements.txt
└── host.json
```
## ✅ 3단계: ask/__init__.py 수정 – RAG 로직 연결
```python
import azure.functions as func
import json
from langchain_openai import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
import os
from dotenv import load_dotenv

load_dotenv()

# 모델 세팅
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.3,
    openai_api_key=os.environ["OPENAI_API_KEY"]
)

embedding_model = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])
vector_store = FAISS.load_local(
    "data/vectors",
    embeddings=embedding_model,
    allow_dangerous_deserialization=True
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vector_store.as_retriever(search_kwargs={"k": 2})
)

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
        question = body.get("question", "")
        answer = qa_chain.run(question)
        return func.HttpResponse(
            json.dumps({"answer": answer}),
            mimetype="application/json",
            status_code=200
        )
    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
```
## ✅ 4단계: requirements.txt 수정
```txt
azure-functions
openai
langchain
langchain-openai
langchain-community
faiss-cpu
tiktoken
python-dotenv
```
## ✅ 5단계: 로컬에서 테스트
```bash
func start
```
- → 브라우저에서 http://localhost:7071/api/ask
- → 또는 curl:
```bash
curl -X POST http://localhost:7071/api/ask \
    -H "Content-Type: application/json" \
    -d "{\"question\": \"은수는 언제 자나요?\"}"
```
## ☁️ 6단계: Azure에 배포
- 리소스 생성:
```bash
az login
az functionapp create \
  --resource-group rag-group \
  --consumption-plan-location koreacentral \
  --runtime python \
  --functions-version 4 \
  --name rag-function-api \
  --storage-account <스토리지명>
```
- storage-account는 미리 만들거나 자동 생성되게 해도 됨
- 배포:
```bash
func azure functionapp publish rag-function-api
```
- 배포 후, 요청은:
```arduino
https://rag-function-api.azurewebsites.net/api/ask
```
- 🧠 CORS 설정도 필요하면:
```bash
az functionapp cors add \
  --name rag-function-api \
  --resource-group rag-group \
  --allowed-origins "https://rag-frontend.azurewebsites.net"
```
- ✅ 여기까지 하면? 🎉 Azure Function으로 RAG 백엔드가 완성됩니다!
