# [Azure Functions 구현] (https://learn.microsoft.com/ko-kr/training/modules/develop-azure-functions/1-introduction)
1. Azure Functions를 로컬에서 개발 및 테스트
- Azure Portal에서 함수 코드를 편집하는 데 제한이 있으므로 함수를 로컬로 개발하고 Azure의 함수 앱에 코드 프로젝트를 게시
2. 로컬 프로젝트 파일
- host.json
- local.settings.json
3. 로컬 프로젝트 만들기
- Visual Studio Code > F1 > 명령 팔레트 > Azure Functions: Create New Project... 검색 실행
4. 로컬에서 함수 실행
- 터미널
- F5 키를 눌러 디버거에서 함수 앱 프로젝트 시작
- 터미널에서 앱 시작
- 로컬에서 실행 중인 HTTP 트리거 함수의 URL 엔드포인트를 볼 수 있음
- Core Tools가 실행 중인 상태에서 Azure:Functions 영역 이동
- Functions에서 로컬 프로젝트 > Functions를 확장
- HttpExample 함수를 마우스 오른쪽 단추로 클릭 > 지금 함수 실행... 선택
- 요청 본문 입력에 요청 메시지 본문 값 {"name": "Azure"}를 입력 > Enter
- Shift + F5 > Core 도구 중지 후 디버거 연결 끊기
5. Azure 로그인
6. Azure에서 리소스 만들기
7. Azure에 프로젝트 배포
8. Azure에서 함수 실행
