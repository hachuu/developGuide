# Develop Guide Reference

## Front-End 개발 가이드
- 2022.08.12 가이드 정리
  1. html
  2. css
  3. 크로스브라우징
  4. javascript
  5. http
  6. tool(git, webpack, babel, eslint, npm...)
  7. framework
  8. tdd
  9. 알고리즘 / 자료구조

## [각종 Setting 문서 정리](https://github.com/hachuu/developGuide/blob/main/%EA%B0%81%EC%A2%85Setting.md)

## SEO canonical 기존 link rel 삭제, 새로 등록하는 script
```
const headerDoc = this.document.head;
const bodyDoc = this.document.body;
for (let i = 0; i < bodyDoc.children.length; i++) {
  if (bodyDoc.children[i].localName === 'link' && bodyDoc.children[i].rel === 'canonical') bodyDoc.children[i].remove();
}
for (let i = 0; i < headerDoc.children.length; i++) {
  if (headerDoc.children[i].localName === 'link' && headerDoc.children[i].rel === 'canonical') headerDoc.children[i].remove();
}

const domain = 'www....';

var link = document.createElement('link');
link.setAttribute('rel', 'canonical');
link.setAttribute('href', 'https://' + domain + window.location.pathname);
document.head.appendChild(link);
```

## 개발자도구 lighthouse-SEO

## Git 명령어 정리
1. [자주 쓰는 명령어](https://github.com/hachuu/developGuide/blob/main/Git%EB%AA%85%EB%A0%B9%EC%96%B4.md)

## javascript Reference
- [내가 정리하고 있는 javascript concept](https://github.com/hachuu/developGuide/blob/main/javascript.md)
1. [Web Development Resources](https://github.com/MarkoDenic/web-development-resources?fbclid=IwAR0AdDnj6dw1eoONieLcFhDzTg3cbLe_OwTiB3sohqd1kYTisy369piHs80 "Web Development Resources")
2. [javascript utilities - 1loc.dev](https://1loc.dev)
3. [javascript theory](https://helloworldjavascript.net/pages/190-array.html)
4. [javascript concept](https://www.30secondsofcode.org/)
5. [javascript prototype 2016년 글](https://medium.com/@bluesh55/javascript-prototype-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-f8e67c286b67)

## 알고리즘😡😱

1. [알고리즘 공부 시작 방법 및 순서](https://blog.yena.io/studynote/2018/11/14/Algorithm-Basic.html)
2. [PS roadmap](https://plzrun.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4PS-%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0)
3. [인프런 알고리즘 강좌](https://www.inflearn.com/course/알고리즘-강좌/lecture/4083?tab=note)
4. [공부하면서 알게된 것들 ](https://github.com/hachuu/developGuide/blob/main/Algorithm.md)
5. [trekhleb/javascript-algorithms](https://github.com/trekhleb/javascript-algorithms)

## GitHub Action 배포
1. [Github Actions으로 배포 자동화하기](https://velog.io/@bluestragglr/Github-Action%EC%9C%BC%EB%A1%9C-%EB%B0%B0%ED%8F%AC-%EC%9E%90%EB%8F%99%ED%99%94%ED%95%98%EA%B8%B0)
2. React (Movie King) 프로젝트 배포 참조
- [Github Actions를 이용한 클라이언트 CI/CD 구축 1 - 프로젝트 개요](https://velog.io/@eomttt/Github-Actions%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%ED%81%B4%EB%9D%BC%EC%9D%B4%EC%96%B8%ED%8A%B8-CICD-%EA%B5%AC%EC%B6%95)
- [Github Actions를 이용한 클라이언트 CI/CD 구축 2 - 프로젝트 구성 및 S3를 이용한 정적사이트 만들기](https://velog.io/@eomttt/Github-Actions%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%ED%81%B4%EB%9D%BC%EC%9D%B4%EC%96%B8%ED%8A%B8-CICD-%EA%B5%AC%EC%B6%95-ejdd96kp)
- [Github Actions를 이용한 클라이언트 CI/CD 구축 3 - Github Actions 사용해보기](https://velog.io/@eomttt/Github-Actions%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%ED%81%B4%EB%9D%BC%EC%9D%B4%EC%96%B8%ED%8A%B8-CICD-%EA%B5%AC%EC%B6%95-Github-Actions-%EC%82%AC%EC%9A%A9%ED%95%B4%EB%B3%B4%EA%B8%B0)
- [AWS node.js배포](https://velog.io/@rheey90/AWS-EC2-Node.js-서버-배포)

## 연산자
1. [표현식과 연산자](https://github.com/hachuu/developGuide/blob/main/%ED%91%9C%ED%98%84%EC%8B%9D%EA%B3%BC%20%EC%97%B0%EC%82%B0%EC%9E%90.md)
2. [연산자 우선순위 MDN](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/%EC%97%B0%EC%82%B0%EC%9E%90_%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84)

## regular expression
[example](https://github.com/hachuu/developGuide/blob/main/regularExpression.md)

## Webpack vs (Grunt vs Gulp)
[출처](https://ehddnjs8989.medium.com/webpack%EC%97%90-%EB%8C%80%ED%95%B4%EC%84%9C-%EC%95%8C%EC%95%84%EB%B4%85%EC%8B%9C%EB%8B%A4-c953181e79ad)
- Webpack = (Grunt|Gulp) + Browserify(Node.js기반 javascript code를 브라우저 환경에서도 실행 가능하도록 해줌)
- Webpack = 모듈 번들러 / Grunt vs Gulp = task runners

### webpack
- An ejected project cannot use the build command anymore.
=> 해결 angular-cli.json 에서 다음 기입
```
"project": {
   "name": "proj-name",
   "ejected": true,
}
```

## Babel
- Babel : JavaScript 컴파일러, ES6 이후의 코드를 구형 브라우저 환경에 맞게 변환
- polyfill : 폴리필은 웹 개발에서 기능을 지원하지 않는 웹 브라우저 상의 기능을 구현하는 코드


## 도커 Docker
- 컨테이너 기반의 오픈소스 가상화 플랫폼
- 도커 빌드
임시 컨테이너 생성 > 명령어 수행 > 이미지로 저장 > 임시 컨테이너 삭제 > 새로 만든 이미지 기반 임시 컨테이너 생성 > 명령어 수행 > 이미지로 저장 > 임시 컨테이너 삭제 > … 의 과정을 계속해서 반복
- 서버 구현까지 [출처](https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html)
- [참조](https://www.slideshare.net/pyrasis/docker-fordummies-44424016)

## SSO 로그인
- [OAuth2 정리](https://github.com/hachuu/developGuide/blob/main/SSO/OAuth2.md)
- [SSO 정리](https://github.com/hachuu/developGuide/blob/main/SSO/SSO.md)
- [cookie session 정리](https://github.com/hachuu/developGuide/blob/main/SSO/cookie%EC%99%80session.md)

 
## FlexBox (Flexbox Froggy를 통한 정리)
[flexbox.md](https://github.com/hachuu/developGuide/blob/main/flexbox.md)
  
## React 스터디 정리
[React 정리](https://github.com/hachuu/developGuide/blob/main/React/React.md)
[Hook 정리](https://github.com/hachuu/developGuide/blob/main/React/hook.md)

## Firebase 배포
```
npm run build
firebase init hosting
firebase deploy --only hosting
firebase serve --only hosting
```
```
yarn build
firebase deploy
```
[Firebase로 배포하기(yarn 명령어)](https://velog.io/@mygomi/Firebase%EB%A1%9C-%EB%B0%B0%ED%8F%AC%ED%95%98%EA%B8%B0yarn-%EB%AA%85%EB%A0%B9%EC%96%B4)
  
  
## Azure 배포
### Storage, CDN 구조
- Storage 실 소스가 반영
  1. 스토리지 생성
  2. 정적 웹 사이트 사용 활성화 => 엔드포인트 활성화
- CDN 도메인 변경...
  1. 프로필 생성
- Storage - CDN 연결 작업
  1. 엔드포인트 추가
  2. 스토리지 생성에서 생긴 엔드포인트 연결
  
## host 파일 경로
- C:\Windows\System32\drivers\etc
  
## jquery => javascript
- [JQUERY TO JAVASCRIPT](http://www.workversatile.com/jquery-to-javascript-converter)
  
## npm 배포[출처](https://www.daleseo.com/js-npm-publish/)
```
  npm login // 로그인
  npm whoami // 내 id 확인
  npm info hello-login // hello-login npm package가 있는 지 확인 E404응답이면 배포 가능
  npm publish // 배포
```
  
## package의 명령어
  1. --sourceMap==false : webpack에 의해 번들링 된 파일과 해당 파일에 대응되는 sourcemap이 생성, 실제 배포 시 sourcemap은 제거하겠다는 명령어
[React build 시 sourcemap 제거하기](https://velog.io/@racoon/React-build-%EC%8B%9C-sourcemap-%EC%A0%9C%EA%B1%B0%ED%95%98%EA%B8%B0)
  2. node --max-old-space-size=???? : 힙 메모리 부족시 
  
## device나 mobile/pc 판별
```
  /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
```
  
## Static web app 설정
```
  // 
 {
  "routes": [
    {
      "route": "/*",
      "serve": "/index.html",
      "statusCode": 200
    }
  ]
}
```
## How do you explicitly set a new property on `window` in TypeScript?
1. 방법1
```
declare global {
  interface Window { MyNamespace: any; }
}

window.MyNamespace = window.MyNamespace || {};
```
2. 방법2
```
    (window as any).tradlinx = this;
    (window as any).tradlinx.app = app;
```

## IE => edge로 연결
```
<script>
  var agent = navigator.userAgent.toLowerCase();
  if ( (navigator.appName == 'Netscape' && agent.indexOf('trident') != -1) || (agent.indexOf("msie") != -1)) {
    window.location = 'microsoft-edge:' + window.location;
    setTimeout(function () {
    //window.close();
    window.open('','_self').close();
  }, 1000);
  }
</script>
```
## javascript 퍼포먼스 속도 체크하기
```
const t0 = performance.now()
for (let i = 0; i < array.length; i++) {
  // some code.......
}
const t1 = performance.now()
console.log(t1 - t0, 'milliseconds')
```

## 종합 개발 
- [브라우저 개발자도구에서 formdata를 숨기는 방법이 있는가요?](https://studyforus.com/help/667208)
- ppt나 excel 자동 영어 <=> 한글 변환 끄기 [파워포인트(PPT) 자동 한영 전환 기능 끄기](https://dev-jaeho.tistory.com/10)
- [알아두면 쓸만한 Chrome Console 기능](https://dev-momo.tistory.com/entry/%EC%95%8C%EB%A7%88%EB%91%90%EB%A9%B4-%EC%93%B8%EB%A7%8C%ED%95%9C-Chrome-Console-%EA%B8%B0%EB%8A%A5)
- [JWT 토큰 변환](https://jwt.io/)
- [Single Sign On (& Single Sign Out) : 부제(로그인 통합 인증)](https://authentication.tistory.com/26)
- [Create React App 에서 ESLint 와 Prettier 설정 하기](https://velog.io/@gwangsuda/2019-09-25-1009-%EC%9E%91%EC%84%B1%EB%90%A8-bwk0ylejxj)
- [table을 좌우 스크롤(수평 스크롤, 스와이프)할 때 특정 컬럼을 고정하고 싶다면](https://xetown.com/tips/1183430)
- [React table bootstrap](https://react-bootstrap.netlify.app/components/table/#tables)
- [SEO 4가지 사례로 알아보는 올바른 캐노니컬 태그 적용 방법](https://www.twinword.co.kr/blog/how-to-apply-canonical-tag-properly/)
- [Web Testing - Element 검색해서 클릭하기](https://miaow-miaow.tistory.com/m/150)
- [d.ts](https://kjwsx23.tistory.com/522)
- [npm install --save](https://docs.npmjs.com/cli/v7/commands/npm-install)
- [RGB <-> HEX 색상코드 확인](https://hi098123.tistory.com/132#94d0cc)
- [Color palettes](https://colorhunt.co/)
- [함수 퍼포먼스 체크](https://jsbench.me/)
- [slide할때 opacity조절하여 css적용](https://stackoverflow.com/questions/25347946/add-fade-effect-in-slideshow-javascript)
- [우아한 형제들 채팅 구현](https://techblog.woowahan.com/2681/)
- [change detection](https://medium.com/coinone/change-detection-%EC%A4%91%EC%8B%AC-angular-%EC%B5%9C%EC%A0%81%ED%99%94-%EB%B0%A9%EB%B2%95-957962ba3d2e)
- [changebdetection성능](https://medium.com/sjk5766/angular-change-detection-%EC%84%B1%EB%8A%A5-%ED%96%A5%EC%83%81%EB%B0%A9%EB%B2%95-onpush-changedetectionref-71c9bccf0a42)

### 개발 도구

1. [정규식 검사](https://regex101.com/r/cO8lqs/4)
2. [css 에디터](https://jsbin.com/wubapojoci/edit?html,css,output)
3. [flex box 연습 - frogbox](https://flexboxfroggy.com/#ko)
4. [javascript 연습장](https://jsfiddle.net/)
5. [color tool](https://material.io/resources/color/#!/?view.left=0&view.right=0&primary.color=B388FF)
6. [google Font](https://fonts.google.com/specimen/Secular+One?sidebar.open=true&selection.family=Secular+One)
7. [icon `<script>` injection](https://fontawesome.com/icons/bars?style=solid)
8. [소스 한줄 정렬](https://gandevelop.tistory.com/9)
9. [QA자동화](https://www.npmjs.com/package/selenium-webdriver)
10. [HTML WEB 웹 개발 각각 cache 유무 코드의 no-cache 캐시삭제, browser 가 caching 하지 않게 하는 http header 설정](https://202psj.tistory.com/763)
11. [Azure 배포](https://helloblog.net/azure-devops/)
12. [[웹폰트] 올바른 방법으로 로딩하자. - 사이트 로딩 속도 개선](https://web-atelier.tistory.com/43)
13. [웹브라우저에서 알림](https://dororongju.tistory.com/125)
14. [mac에서 input file할때 한글 깨짐 현상](https://gemimi.tistory.com/43)
  ```
  fileName = Normalizer.normalize(fileName, Normalizer.Form.NFC)
  ```
---

```
ngAfterViewInit() {
    window.onpageshow = (event) => {
      if ( event.persisted || (window.performance && window.performance.navigation.type == 2)) {
        this.loginForm.reset();
      }
    }
  }
```
15. [아이폰 사파리 script ](https://orangeheeya.tistory.com/entry/%EB%AA%A8%EB%B0%94%EC%9D%BC-%EC%95%84%EC%9D%B4%ED%8F%B0-%EC%86%8C%EC%8A%A4%EC%BD%94%EB%93%9C%EB%B3%B4%EA%B8%B0)

16. frontend
```
  a tag에서 keyup.enter 이벤트는 (click)과 동일한 이벤트로 인지하여 둘다 선언하는 경우 이벤트가 중복되어 사용됨

  => (keyup.enter)를 삭제 해줘야함
```

17. HTML <slot> Tag
❮Reference ❯

Example
The template element holds HTML code without displaying it:

<template>
  <div>Name:
    <slot name="username"></slot>
  </div>
  <div>Birthday:
    <slot name="birthday"></slot>
  </div>
</template>
Try it Yourself »


- 성능체크 (https://jsbench.me/)
