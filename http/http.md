1. Content-Disposition [출처](https://developer.mozilla.org/ko/docs/Web/HTTP/Headers/Content-Disposition)
- 정의 : HTTP 응답에서 Content-Disposition 헤더
  - inline :  컨텐츠가 브라우저에 inline 되어야 하는 웹페이지 자체이거나 웹페이지의 일부
  - attachment로써 다운로드 되거나 로컬에 저장될 용도록 쓰이는 것인지를 알려주는 헤더

2. RESTful Api
- 400: 400 Bad Request 응답 상태 코드는 서버가 클라이언트 오류(예: 잘못된 요청 구문, 유효하지 않은 요청 메시지 프레이밍, 또는 변조된 요청 라우팅) 를 감지해 요청을 처리할 수 없거나, 하지 않는다는 것을 의미
- 401, 403: 권한 없음
  - 401 에러는 유효하지 않은 인증 토큰일 경우 반환하고
  - 403 에러는 토큰은 있지만, 그 토큰을 받은 유저가 scope 가 부족할 때 반환하는 것
- [REST API 제대로 알고 사용하기](https://meetup.toast.com/posts/92)
- [고양이사진으로 보는 응답코드](https://http.cat/)
- [Front 외부 API 연동 의구심](https://okky.kr/article/882992?note=2257178)
- put과 patch의 차이점
```
PUT|	Update/Replace|	405 (Method Not Allowed), unless you want to update/replace every resource in the entire collection.|	200 (OK) or 204 (No Content). 404 (Not Found), if ID not found or invalid.
PATCH|	Update/Modify|	405 (Method Not Allowed), unless you want to modify the collection itself.|	200 (OK) or 204 (No Content). 404 (Not Found), if ID not found or invalid.
```
- 413: 브라우저에서 파일 업로드 하는 경우 파일 용량이 제한되어 발생할 수 있는 error
