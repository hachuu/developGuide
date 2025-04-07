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
### 4. 필수 패키지 설치
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
