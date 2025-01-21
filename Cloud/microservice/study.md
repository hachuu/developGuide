1. [Micro Frontends](https://martinfowler.com/articles/micro-frontends.html)
2. [리액트를 사용하여 마이크로프론트엔드 개발하는 방법](https://blog.daum.net/followyourdream/10086859)
3. [마이크로서비스 모델링 ⑤ : FrontEnd 설계](https://engineering-skcc.github.io/microservice%20modeling/FrontEnd-modeling/)

| **특징**           | **SSR (Server-Side Rendering)**                                     | **CSR (Client-Side Rendering)**                                   | **SSG (Static Site Generation)**                                  |
|---------------------|--------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------|
| **렌더링 시점**     | 요청 시 서버에서 HTML 생성 후 전달                                 | 브라우저에서 JavaScript로 렌더링                                 | 빌드 시 HTML 파일을 생성 후 정적으로 제공                        |
| **속도**           | 초기 로딩 속도는 느림, 이후는 빠름                                 | 초기 로딩 속도는 느림, 이후는 매우 빠름                          | 초기 로딩 속도와 이후 속도 모두 빠름                             |
| **SEO**            | 매우 우수 (HTML이 서버에서 즉시 생성됨)                            | 제한적 (초기 HTML이 빈 상태로 제공됨)                            | 매우 우수 (정적 HTML 제공)                                       |
| **사용 사례**      | - 동적 데이터 필요 시<br>- 개인화 서비스<br>- 실시간 업데이트       | - 단일 페이지 앱(SPA)<br>- 사용자 인터랙션이 많은 앱              | - 블로그<br>- 문서 사이트<br>- 자주 변하지 않는 콘텐츠           |
| **서버 부하**       | 요청마다 서버가 HTML을 생성하므로 부하가 큼                        | 초기 요청 시 API 호출만 처리하므로 서버 부하 적음                | 빌드 시 서버 부하가 있음, 이후 요청은 정적 파일 제공으로 부하 적음 |
| **구현 난이도**     | 중간 (서버 설정 필요, Next.js, Nuxt.js로 구현 용이)                | 낮음 (React, Vue.js 등에서 기본적으로 CSR 지원)                  | 낮음~중간 (빌드 프로세스 필요, Next.js, Gatsby 등으로 구현 용이)  |
| **데이터 최신성**   | 항상 최신 데이터 제공 가능                                        | 클라이언트에서 API를 호출해 최신 데이터를 가져와야 함            | 빌드 시점의 데이터로 한정 (정기적 재빌드 필요)                   |
| **예시 프레임워크** | Next.js, Nuxt.js                                                  | React, Vue.js                                                   | Next.js, Gatsby, Hugo                                           |
