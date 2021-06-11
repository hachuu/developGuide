# Angular를 이용한 SSO 처리 example 및 분석

1. 개념 정리
  1. [OpenID Connect 개념](https://www.ibm.com/docs/ko/sva/9.0.7?topic=concepts-openid-connect)
  2. OAuth: HTTP 기반 권한 부여 프로토콜

- [Angular 10 - JWT Authentication Example & Tutorial](https://jasonwatmore.com/post/2020/07/09/angular-10-jwt-authentication-example-tutorial)
- [Creating a Single-Sign-On Angular Application | OAuth2 and OIDC](https://www.youtube.com/watch?v=AcuzemsJfxA)
- [reating a Single-Sign-On Angular Application | OAuth2 and OIDC Source]https://github.com/shaheershukur/Angular-Single-Sign-On-OAuth2-OIDC-/pulls)

2. 처리 방법
- 로그인 뷰(signin.component.ts)와 로그인 성공시 이동할 대시보드 뷰(dashboard.component.ts)으로 구성되어 있다. 처리의 흐름은 아래와 같다.
  1. 로그인 뷰는 인증 서비스(auth.service.ts)를 사용하여 서버에 인증을 요청한다.
  2. 서버 인증이 성공한 경우, 서버는 토큰을 발행하고 클라이언트로 토큰을 응답한다.
  3. 서버 인증이 성공한 경우, 인증 서비스는 서버가 응답한 토큰을 로컬 스토리지에 저장하고 대시보드 뷰로 이동한다. 이때 가드(auth.guard.ts)를 사용하여 토큰을 검증한다.
  4. 대시보드 컴포넌트는 사용자 서비스(user.service.ts)를 사용하여 서버에 사용자 정보를 요청한다. 이때 요청 헤더(Request Header)에 토큰을 담아 전송한다.
  5. 대시보드 컴포넌트는 서버의 응답을 받아 뷰에 표시한다.
- [13.22 Angular JWT Authentication Token 기반 인증](https://poiemaweb.com/angular-jwt-authentication)
  ```
  로그인 구현에 validation까지 소스 참조가 가능
  ```
- [참조 소스코드](https://github.com/ungmo2/angular8-jwt-auth)
