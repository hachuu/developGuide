# Router
- routerLink vs href
- href: 서버로 페이지 요청이 이뤄짐
- routerLink: 자신의 값을 라우터에 전달, 해당 컴포넌트를 활성화, 뷰 출력

# SEO문제
- 서버 사이드 랜더링을 지원하는 SEO 대응 기술이 이미 존재

# 모듈
- 모듈 분리
- 기능 모듈: 특정 화면을 구성하는 구성요소
- 공유 모듈: 애플리케이션 전역에서 사용하는 컴포넌크, 디렉티브, 파이프 등
- 핵심 모듈: 애플리케이션 전역에서 사용하는 데이터 서비스, 인증 서비스, 인증 가드 등
- module provider 등록하는 경우 service의 Injdectable의 providedIn 메타데이터 삭제 (모듈에 등록된 서비스가 많은 경우 모듈의 프로바이더에서 서비스를 관리하는 것이 유리)

# 양방향 바인딩

<counter [count]="value" (countChange)="value=$event"></counter>
