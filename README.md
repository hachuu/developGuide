# Develop Guide Reference




## javascript Reference

1. [Web Development Resources](https://github.com/MarkoDenic/web-development-resources?fbclid=IwAR0AdDnj6dw1eoONieLcFhDzTg3cbLe_OwTiB3sohqd1kYTisy369piHs80 "Web Development Resources")
2. [javascript utilities - 1loc.dev](https://1loc.dev)
3. [javascript theory](https://helloworldjavascript.net/pages/190-array.html)
4. [javascript concept](https://www.30secondsofcode.org/)

## React Reference

1. [30-Days-Of-React (1day: javascript)](https://github.com/Asabeneh/30-Days-Of-React/blob/master/01_Day_JavaScript_Refresher/01_javascript_refresher.md)

## Setting Of Developement

1. [spring boot 프로젝트 생성](https://aljjabaegi.tistory.com/480)
2. [eclipse setting](#eclipse-setting)





# eclipse setting



1. [eclipse git 연동](https://recollectionis.tistory.com/166)
2. [JDK 설치 방법, 환경변수 설정](https://jhnyang.tistory.com/224)
3. [STS, Gradle 설치](    https://linked2ev.github.io/gitlog/2019/08/19/springboot-mvc-2-%EA%B0%9C%EB%B0%9C%ED%99%98%EA%B2%BD-%EC%84%A4%EC%A0%95-%EB%B0%8F-Eclipse-STS-Gradle-%EC%84%A4%EC%B9%98/[)
4.[Create Java project structure automatically](http://www.mkyong.com/gradle/gradle-create-java-project-structure-automatically/)

## Eclipse 연동 시 에러 Unable to start embedded Tomcat

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
  - 

4. The selection cannot be launched and there are no recent launches 문제 해결

- 방법
  - Eclipse 프로젝트 이름 위에서 마우스 오른쪽 버튼을 누른 후, Gradle >> Refresh Gradle Project하거나 그냥 프로젝트 Refresh
  - 삭제하고 싶은 라이브러리의 경우는 build.cradle에서 해당 파일을 삭제 후, 동일하게 Refresh Gradle Project
  - 그래도 되지 않을때의 방법 [이클립스 The selection cannot be launched and there are no recent launches](https://zxcv5500.tistory.com/268)
  - <b>run as java 하고 refresh<b> [youtube ](https://www.youtube.com/watch?v=OaAz1g2Cwx8)

