1. 쿠키
- 브라우저에 저장되는 작은 크기의 문자열
- HTTP 프로토콜의 일부
- 웹서버에 의해 만들어짐 (서버가 HTTP 응답 헤더의 Set-Cookie에 내용을 넣어 전달하면, 브라우저가 자체적으로 저장함)
- 쿠키는 클라이언트 식별과 같은 인증에 가장 많이 쓰임
- document.cookie 프로퍼티를 이용하면 브라우저에서도 쿠키에 접근할 수 있음
- 용량은 최대 4KB(하나의 쿠키당)
- 도메인 하나당 저장할 수 있는 쿠키 개수 20여개로 제한적
- 쿠키 등록시 도메인을 지정하는 경우 서브 도메인까지 가능/ 기본값은 루트 도메인만 가능 (안정성을 높이기 위함)
```
// site.com에서
// 서브 도메인(*.site.com) 어디서든 쿠키에 접속하게 설정할 수 있습니다.
document.cookie = "user=John; domain=site.com"

// 이렇게 설정하면

// forum.site.com와 같은 서브도메인에서도 쿠키 정보를 얻을 수 있습니다.
alert(document.cookie); // user=John 쿠키를 확인할 수 있습니다.
```
- expires 나 max-age 옵션을 설정하면 브라우저를 닫아도 쿠키가 삭제되지 않음
- 쿠키의 유효 일자는 반드시 GMT(Greenwich Mean Time) 포맷으로 설정
```
// 지금으로부터 하루 후
let date = new Date(Date.now() + 86400e3);
date = date.toUTCString();
document.cookie = "user=John; expires=" + date;
```
- max-age는 expires 옵션의 대안으로, 쿠키 만료 기간을 설정(현재부터 설정하고자 하는 만료일시까지의 시간을 초로 환산한 값을 설정)
```
// 1시간 뒤에 쿠키가 삭제됩니다.
document.cookie = "user=John; max-age=3600";
```
- secure 옵션 활성화의 경우 HTTPS로 통신할 때만 쿠키 전송 가능 (쿠키는 기본적으로 도메인만 확인, 프로토콜 따지지 않음)
- samesite 크로스 사이트 요청 위조(XSRF) 공격을 막기 위해 생긴 옵션 *(사용자가 사이트 외부에서 요청을 보낼 때, samesite=strict 옵션이 있는 쿠키는 절대로 전송되지 않음)*
- httpOnly 옵션 웹서버에서 Set-Cookie 헤더를 이용해 쿠키를 설정할 때 지정 => 클라이언트 측 스크립트가 쿠키를 사용할 수 없게 함
1.1 서드 파티 쿠키
- 다른 도메인에서 설정한 쿠키
- 브라우저 별 허용하지 않을 수 있음 (ex: 사파리)
- 광고회사는 사용자의 이용 행태를 추적하고, 광고를 제공하기 위해 오래전부터 서드 파티 쿠키를 사용하고 있음
- 서드파티 쿠키는 쿠키를 설정한 도메인에 종속되기 때문에 ads.com은 사용자가 어떤 사이트를 방문했는지 추적할 수 있음

1.2 TIL
- [브라우저 쿠키와 SameSite 속성](https://seob.dev/posts/%EB%B8%8C%EB%9D%BC%EC%9A%B0%EC%A0%80-%EC%BF%A0%ED%82%A4%EC%99%80-SameSite-%EC%86%8D%EC%84%B1/)
###### 출처 : [쿠키와 document.cookie](https://ko.javascript.info/cookie)
2. 세션

3. [로그인 유지 작업](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=commind7&logNo=220631505184)
브라우저 닫을 시 로그아웃 처리..
