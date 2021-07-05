# Develop Guide Reference

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

## 'ng'는 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는 배치 파일이 아닙니다.
- 시스템 환경 변수 편집
  1. 시스템 변수 Path => %SystemRoot%\system32%SystemRoot% 추가
  2. node_modules 경로에서 C:\Users\tradlinx\AppData\Roaming\npm\node_modules\@angular\cli\bin\ng 등록, C:\Users\tradlinx\AppData\Roaming\npm 

## choco, yarn 다운
- powershell 관리자도구 
1. Remove-Item C:\ProgramData\chocolatey -Recurse
2. Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
3. choco install yarn
- yarn 다운
```
npm install --global yarn
```

## VSCode 세팅
[TSLint](http://ngmsoftware.com/bbs/board.php?bo_table=study&wr_id=266&sca=Error&sst=wr_datetime&sod=desc&sop=and&page=1)
=> eslint 변환 작업
- npm install --save-dev eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin
- npx tslint-to-eslint-config
- [tslint to eslint](https://pks2974.medium.com/tslint-%EC%97%90%EC%84%9C-eslint-%EB%A1%9C-%EC%9D%B4%EC%82%AC%ED%95%98%EA%B8%B0-ecd460a1e599)

### npm install 시 python이나 기타 모듈 내려받을 때 에러나는 경우
- powershell 관리자 권한으로 실행
- 해당 프로젝트 경로에서 하위를 입력
- [!!! 에러 해결법 총집합 !!! npm-gyp 오류/python 오류/truffle 컴파일 에러/Unknown network klaytn 에러 나시는 분들은](https://www.inflearn.com/questions/11540)
  - [python down grade](https://www.python.org/downloads/release/python-2710/)
```
npm install --global --production windows-build-tools
npm install --global node-gyp
```

## Mac M1 세팅
[맥 세팅 작업중...](https://github.com/hachuu/developGuide/blob/main/MacSetting.md)
[GitHub ssh key 생성하고 등록하고 사용하기](https://syung05.tistory.com/20)
* window ssh key 생성 [Use SSH key authentication](https://docs.microsoft.com/en-us/azure/devops/repos/git/use-ssh-keys-to-authenticate?view=azure-devops)
```
~/.ssh
ssh-keygen -C "jamal@fabrikam.com"
```

## Git 명령어 정리
1. [자주 쓰는 명령어](https://github.com/hachuu/developGuide/blob/main/Git%EB%AA%85%EB%A0%B9%EC%96%B4.md)

## javascript Reference
- [내가 정리하고 있는 javascript concept](https://github.com/hachuu/developGuide/blob/main/javascript.md)
1. [Web Development Resources](https://github.com/MarkoDenic/web-development-resources?fbclid=IwAR0AdDnj6dw1eoONieLcFhDzTg3cbLe_OwTiB3sohqd1kYTisy369piHs80 "Web Development Resources")
2. [javascript utilities - 1loc.dev](https://1loc.dev)
3. [javascript theory](https://helloworldjavascript.net/pages/190-array.html)
4. [javascript concept](https://www.30secondsofcode.org/)
5. [javascript prototype 2016년 글](https://medium.com/@bluesh55/javascript-prototype-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-f8e67c286b67)


## Setting Of Developement

- java
  1. [spring boot 프로젝트 생성](https://aljjabaegi.tistory.com/480)
  2. [eclipse setting](#eclipse-setting)
  3. [스프링 배치만들기](https://github.com/hachuu/developGuide/blob/main/%EC%8A%A4%ED%94%84%EB%A7%81%20%EB%B0%B0%EC%B9%98%20%EB%A7%8C%EB%93%A4%EA%B8%B0.md)
- Gradle
  1. [실제 gradle 설치 방법](https://park-jongseok.github.io/languages/java/2019/11/01/installing-gradle.html) - eclipse marketplace가 아님
  2. 'gradle'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는 배치 파일이 아닙니다. => 시스템 환경 변수 %GRADLE_HOME%\bin 순서를 상위로 옮겨줌.
  3. Run the init task (gradle init --type java-library) [출처](https://docs.gradle.org/current/samples/sample_building_java_libraries.html)


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

## RESTful Api
- 401, 403: 권한 없음
  - 401 에러는 유효하지 않은 인증 토큰일 경우 반환하고
  - 403 에러는 토큰은 있지만, 그 토큰을 받은 유저가 scope 가 부족할 때 반환하는 것
- [REST API 제대로 알고 사용하기](https://meetup.toast.com/posts/92)
- [고양이사진으로 보는 응답코드](https://http.cat/)
- [Front 외부 API 연동 의구심](https://okky.kr/article/882992?note=2257178)
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
---


# eclipse setting



1. [eclipse git 연동](https://recollectionis.tistory.com/166)
2. [JDK 설치 방법, 환경변수 설정](https://jhnyang.tistory.com/224)
3. [STS, Gradle 설치](    https://linked2ev.github.io/gitlog/2019/08/19/springboot-mvc-2-%EA%B0%9C%EB%B0%9C%ED%99%98%EA%B2%BD-%EC%84%A4%EC%A0%95-%EB%B0%8F-Eclipse-STS-Gradle-%EC%84%A4%EC%B9%98/[)
4. [Create Java project structure automatically](http://www.mkyong.com/gradle/gradle-create-java-project-structure-automatically/)
5. [CORS 문제 api 연동 해결 (maven, gradle)](https://spring.io/guides/gs/rest-service-cors/)
6. [STS와 깃허브(GitHub)연동하는 방법](https://all-record.tistory.com/163)

## Eclipse 연동 시 에러 Unable to start embedded Tomcat 🤯

1. [eclipse Git Clone 프로젝트 서버 구동 불가 현상](https://dreaming-soohyun.tistory.com/entry/eclipse-Git-Clone-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%84%9C%EB%B2%84-%EA%B5%AC%EB%8F%99-%EB%B6%88%EA%B0%80-%ED%98%84%EC%83%81)

- clone한 프로젝트 오른쪽 클릭 - properites - project facets에 Dynamic Web Servies를 체크해주면 된다

2. [Gradle과 git 이용해서 Eclipse로 Java 프로젝트 개발 시작하기1 참조](http://www.mkyong.com/gradle/gradle-create-java-project-structure-automatically/)
3. [Gradle과 git 이용해서 Eclipse로 Java 프로젝트 개발 시작하기2 참조](https://docs.gradle.org/current/userguide/build_init_plugin.html)

- 순서
  - Github에 저장소를 만들고 내 PC에 git clone 한다. 
  - git clone한 프로젝트 디렉터리로 이동한 후 gradle로 java project 기본 build 환경을 구축한다. ($ gradle init --type java-library)
  - $ gradle init --type java-library
  - .gitignore 파일을 추가한다. [.gitignore파일 추가](https://github.com/lifove/CLAMI/blob/develop/.gitignore)
  - Eclipse 실행해서,  앞 단계에서 생성한 Java 프로젝트를 import한다.
  - 외부 라이브러리가 있는 경우 Eclipse에서 build.gradle 파일을 연 후 필요한 라이브러리를 추가
  - build.gradle 파일이 수정 됐으므로, Refresh Gradle Project를 해준다

4. The selection cannot be launched and there are no recent launches 문제 해결 방법
    1. Eclipse 프로젝트 이름 위에서 마우스 오른쪽 버튼을 누른 후, Gradle >> Refresh Gradle Project하거나 그냥 프로젝트 Refresh
        1. 삭제하고 싶은 라이브러리의 경우는 build.cradle에서 해당 파일을 삭제 후, 동일하게 Refresh Gradle Project
    2. 그래도 되지 않을때의 방법 [이클립스 The selection cannot be launched and there are no recent launches](https://zxcv5500.tistory.com/268)
        1. Window - > Preferecences 클릭
        2. Run/Debug -> Launching 란을 보면 Launch Operation 항목이 있다.
        3. Launch the selected resource or active editor. if not launchable: 항목의 라디오 그룹에서 --> Launch the associated project 를 선택해 준다. 
    3. <b>run as java 하고 refresh<b> [출처 youtube](https://www.youtube.com/watch?v=OaAz1g2Cwx8)
---
  
## FlexBox (Flexbox Froggy를 통한 정리)
[flexbox.md](https://github.com/hachuu/developGuide/blob/main/flexbox.md)
  
## React 스터디 정리
[React 정리](https://github.com/hachuu/developGuide/blob/main/React/React.md)
[Hook 정리](https://github.com/hachuu/developGuide/blob/main/React/hook.md)

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
```
-P, --save-prod: Package will appear in your dependencies. This is the default unless -D or -O are present.

-D, --save-dev: Package will appear in your devDependencies.

-O, --save-optional: Package will appear in your optionalDependencies.

--no-save: Prevents saving to dependencies.
```
*--save를 쓰지 않아도 되는 이유 추가: npm5 부터는 --save 옵션을 사용하지 않아도 dependencies에 항목을 추가해줌
출처: https://xtring-dev.tistory.com/entry/NPM-npm-install-할-때-save를-함께-입력하는-이유*
- [axios excel 파일 다운로드](https://soonh.tistory.com/38)
  
## Firebase 배포
```
npm run build
firebase init hosting
firebase deploy --only hosting
firebase serve --only hosting
```
  
  
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
  
  
