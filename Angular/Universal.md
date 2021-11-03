# Ahead-of-Time (AOT) 컴파일러
- 브라우저가 애플리케이션 코드를 받아서 전에 미리 HTML 파일과 TypeScript코드를 브라우저가 실행할 수 있는 JavaScript 코드로 변환
- 장점
```
렌더링이 빠르다
비동기 요청횟수가 줄어든다
내려받아야할 Angular프레임워크 용량이 줄어든다
템플릿 에러를 더 빠르게 발견할 수 있다
클라이언트 쪽에서 위험한 HTML 코드나 Javascript 코드가 실행될 가능성이 없고 인젝션 공격의 가능성도 더 적ㄷㅏ
```
- 컴파일 방식 차이: angular.json 설정 파일에서 aot 프로퍼티 값으로 변경가능
```
Just-in-Time (JIT): 브라우저에서 애플리케이션을 실행하면서 코드를 직접 컴파일하는 방식입니다. Angular 8까지는 기본 컴파일러였습니다.
Ahead-of-Time (AOT): 브라우저에 애플리케이션 코드를 보내기 전에 미리 컴파일하는 방식입니다. Angular 9부터 기본 컴파일러
```

# Universal 구조
```
src/
  index.html                 애플리케이션 웹 페이지
  main.ts                    클라이언트 앱을 부트스트랩하는 파일
  main.server.ts             * 서버 앱을 부트스트랩하는 파일
  style.css                  앱 전역 스타일 파일
  app/ ...                   애플리케이션 코드
    app.server.module.ts     * 서버 사이드 애플리케이션 모듈
server.ts                    * Express 웹 서버
tsconfig.json                TypeScript 기본 환경설정 파일
tsconfig.app.json            TypeScript 브라우저용 환경설정 파일
tsconfig.server.json         TypeScript 서버용 환경설정 파일
tsconfig.spec.json           TypeScript 스펙용 환경설정 파일
```
