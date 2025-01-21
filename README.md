# Develop Guide Reference

## 개발 가이드 Index
- [AI](https://github.com/hachuu/developGuide/blob/main/AI)
- [Back-End + Server](https://github.com/hachuu/developGuide/blob/main/Back-End)
- [Cloud](https://github.com/hachuu/developGuide/blob/main/Cloud)
- [DevOps](https://github.com/hachuu/developGuide/blob/main/DevOps)
- [Front-End](https://github.com/hachuu/developGuide/blob/main/Front-End)
---
## TIL 요즘 


## [각종 Setting 문서 정리](https://github.com/hachuu/developGuide/tree/main/%EA%B0%9C%EB%B0%9C%EC%84%B8%ED%8C%85)

## 개발자도구 lighthouse-SEO

## Git 명령어 정리
1. [자주 쓰는 명령어](https://github.com/hachuu/developGuide/blob/main/Git%EB%AA%85%EB%A0%B9%EC%96%B4.md)

## 알고리즘😡😱
1. [알고리즘 공부 시작 방법 및 순서](https://blog.yena.io/studynote/2018/11/14/Algorithm-Basic.html)
2. [PS roadmap](https://plzrun.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4PS-%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0)
3. [인프런 알고리즘 강좌](https://www.inflearn.com/course/알고리즘-강좌/lecture/4083?tab=note)
4. [공부하면서 알게된 것들 ](https://github.com/hachuu/developGuide/blob/main/Algorithm.md)
5. [trekhleb/javascript-algorithms](https://github.com/trekhleb/javascript-algorithms)

## jquery => javascript
- [JQUERY TO JAVASCRIPT](http://www.workversatile.com/jquery-to-javascript-converter)

## npm registry 설정
- 방법 : 전역 .npmrc 파일 수정 및 해당 repo에 레지스트리 연결해지 후 기본 값으로 설정
- 현재 레지스트리 확인 : npm config get registry
- 전역 레지스트리 변경 : npm config set registry https://registry.npmjs.org/
- 디렉토리 기준으로 레지스트리 변경 ex) C:\dev\ang19에서 실행시
  ```
  cd C:\dev\ang19 // 경로 이동
  echo registry=https://registry.npmjs.org/ > .npmrc // 해당 경로에 npmrc 파일 생성
  type .npmrc // registry=https://registry.npmjs.org/ : 출력 확인
  npm config get registry // 레지스트리 확인
  ```
  
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
- [CORS 에러](https://xiubindev.tistory.com/115)

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



