# **python 기반 AI RAG 프로젝트를 Azure App Service에 배포하기**

# VS Code 사용

## 🎯 목표
```txt
현재 로컬 프로젝트(Streamlit + RAG)를
Visual Studio Code에서 클릭 한 번 / 명령 한 줄로 Azure App Service에 배포하는 것!
```
## ✅ 사전 준비
| 항목	| 필요 여부 |
|------|-----------|
|Azure 계정|	✅ 필수|
|VS Code 설치	|✅|
|Azure CLI	|✅ (이미 있다면 OK)|
|Python 3.11+	|✅|
|VS Code 확장<br>: Azure App Service, <br>Azure Account, Python|	✅ 꼭 설치하세요!|

## 📁 예시 프로젝트 구조
```bash
rag_webapp/
├── frontend/
│   └── app.py              ← ✅ Streamlit 메인
├── rag/                    ← RAG 처리 모듈들
├── requirements.txt        ← 필수 라이브러리
├── startup.sh              ← streamlit 실행 스크립트
├── .env                    ← 환경 변수 (로컬 개발용)
```

## ✅ Step 1: requirements.txt 준비
- 필수 라이브러리 포함:
```txt
streamlit
openai
langchain
langchain-community
langchain-openai
faiss-cpu
tiktoken
python-dotenv
PyPDF2
```
## ✅ Step 2: startup.sh 작성
```bash
#!/bin/bash
streamlit run frontend/app.py --server.port=8000 --server.enableCORS=false
```
- ✅ 반드시 포트를 8000으로, CORS 꺼야 정상 작동함
- 윈도우에서는 .sh 대신 .bat 써도 됨

## ✅ Step 3: VS Code에서 Azure App Service 연결
1. 왼쪽 사이드바 > Azure 아이콘 클릭
2. 상단의 “Sign in to Azure” 클릭
3. “App Services” 섹션에서 → + 버튼 클릭
4. Create New Web App… 선택
5. 이름 입력: rag-streamlit-demo
6. 런타임: Python 3.11
7. 리소스 그룹/플랜 선택 또는 새로 만들기

## ✅ Step 4: 배포 (Deploy)
1. App Service에 오른쪽 클릭 → "Deploy to Web App..."
2. 현재 디렉토리 선택
3. .env는 제외하거나, Azure 포털에 키 입력
4. 자동으로 zip 패키징 → 업로드 → 빌드됨
5. 💡 배포 완료 후, Azure가 자동으로 실행합니다!

## ✅ Step 5: startup.sh 지정 (포털에서)
1. Azure Portal → App Service → 구성(Configuration) → 일반 설정
2. Startup Command에 입력:
```bash
bash startup.sh
```
- Windows 기반 App Service라면:
  - startup.bat 또는 python frontend/app.py (비추천)

## ✅ Step 6: 실행 확인
- 브라우저에서 아래 주소 접속:
```arduino
https://rag-streamlit-demo.azurewebsites.net
```

### 🧠 보너스: .env 변수 처리 방법
1. 방법 1: Azure 포털에서 등록
- App Service → 구성 → 애플리케이션 설정
- OPENAI_API_KEY → 값 입력

2. 방법 2: 코드에서 fallback 처리
```python
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY", "fallback-key-here")
```

## ✅ 전체 흐름 요약
|단계|설명|
|---|----|
|✅ requirements.txt, startup.sh 준비	|Streamlit 실행 설정|
|✅ Azure App Service 만들기	|VS Code에서 클릭으로 가능|
|✅ "Deploy to Web App..." 클릭	|로컬 코드 → Azure|
|✅ 포털에서 Startup Command 지정	|bash startup.sh|
|✅ 브라우저에서 실행 확인	|웹 앱 주소 접속|

---

# GitHub 저장소를 Azure App Service에 연결해서 자동 배포

## ✅ 전체 흐름 요약
```css
[로컬 VSCode 작업] 
     ↓ git push
[GitHub Repo]
     ↓ 자동 연동
[Azure App Service]
     ↓ 자동 재배포!
웹앱 새 버전 바로 실행 🎯
```

## 🔧 준비물
|항목|	필요 여부|
|GitHub 계정	|✅
|Azure 계정 + App Service|	✅
|VS Code + Git 설치|	✅
|GitHub에 프로젝트 Push 되어 있음	|✅|

## 🎯 Step-by-Step: GitHub → Azure App Service 자동 배포

## ✅ 1. GitHub 저장소 준비
- 로컬 프로젝트를 GitHub에 올려주세요:
```bash
git init
git remote add origin https://github.com/<your-username>/<repo-name>.git
git add .
git commit -m "initial commit"
git push -u origin main
```
- 📁 requirements.txt, startup.sh, frontend/app.py 등 배포 파일 포함 필수!

## ✅ 2. Azure Portal에서 App Service 생성 (또는 기존 앱 사용)
- Azure App Service 만들기
- 런타임: Python 3.11
- App name: rag-from-github
- 배포 위치: koreacentral (또는 가까운 리전)

## ✅ 3. GitHub와 배포 연결
- App Service → 배포 센터(Deployment Center) 클릭
- 소스: GitHub
- 빌드 제공자: GitHub Actions
- 리포지토리/브랜치 선택
- → main/master

- 💡 자동으로 GitHub Actions Workflow (.github/workflows/azure.yml)가 생성됩니다.

## ✅ 4. Startup Command 설정
- App Service → 구성 > 일반 설정 → Startup Command 입력:
```bash
bash startup.sh
(= Streamlit 앱 실행하는 스크립트)
```
## ✅ 5. .env 변수 등록 (예: OpenAI API 키)
- App Service → 구성 > 애플리케이션 설정
- OPENAI_API_KEY → sk-xxxx 형식 입력

## ✅ 6. 코드 수정 → Git Push → 자동 배포
```bash
git add .
git commit -m "update app"
git push origin main
```
- 🤖 GitHub Action이 자동으로 실행되고,
- Azure로 배포 완료되면 웹사이트가 새로 업데이트됩니다!

## 📁 GitHub Repo 구조 예시
```markdown
.
├── frontend/
│   └── app.py
├── rag/
│   ├── loader.py
│   ├── qa_engine.py
│   └── vector_store.py
├── requirements.txt
├── startup.sh
└── .github/
    └── workflows/
        └── azure.yml     ← GitHub에서 자동 생성됨
```

## ✅ 장점 요약
|장점|	설명|
|---|-------|
|🔁 코드 커밋만 해도 배포됨|	GitHub Actions 자동화|
|🧑‍🤝‍🧑 협업에 유리|	팀원들도 배포 가능|
|🔄 롤백/기록 추적 쉬움|	Git history 그대로 남음|
|🎯 실무에서 많이 씀	|DevOps 기본 패턴|

## ❗ 배포 안 될 때 체크리스트
|항목	|확인 사항|
|---|-------|
|startup.sh 위치	|루트 디렉토리에 있는가?|
|requirements.txt|	streamlit, openai 등 포함됐는가?|
|App Service 설정|	Python 3.11, bash startup.sh 설정됨?|
|.env → App Setting|	OPENAI_API_KEY 제대로 설정됨?|
