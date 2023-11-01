# gradle 관련 Ref
- [gradle 공식 유저 가이드](https://docs.gradle.org/current/userguide/userguide.html)
- [gradle-dependencies](https://kwonnam.pe.kr/wiki/gradle/dependencies)
- [declaring dependencies](https://docs.gradle.org/current/userguide/declaring_dependencies.html)

---
- [spring-boot-library 2.5.15 version](https://mvnrepository.com/artifact/org.springframework.boot/spring-boot/2.5.15)
- 요약 : 오류 해결하면서 발견한 점
  - slf4j-jboss-logmanager-1.1.0.Final.jar LoggerFactory is not a Logback LoggerContext but Logback is on the classpath.   
  ```
  <?xml version="1.0" encoding="UTF-8"?>
  <jboss-deployment-structure>
    <deployment>
      <exclusions>
        <module name="org.apache.commons.logging" />
        <module name="org.apache.log4j" />
        <module name="org.jboss.logging" />
        <module name="org.jboss.logging.jul-to-slf4j-stub" />
        <module name="org.jboss.logmanager" />
        <module name="org.jboss.logmanager.log4j" />
        <module name="org.slf4j" />
        <module name="org.slf4j.impl" />
      </exclusions>
    </deployment>
  </jboss-deployment-structure>
  ```
  - Exception in thread "main" org.springframework.context.ApplicationContextException: Unable to start embedded container; nested exception is java.lang.ClassCastException: org.apache.tomcat.websocket.WsWebSocketContainer cannot be cast to io.undertow.websockets.jsr.ServerWebSocketContainer


  1. logback을 dependencies에 추가했기 때문에 log4j2, logging 제외시켜줌
  2. tomcat도 제외하기 위해 spring-boot-starter-tomcat, tomcat-embed-* 추가하였는데, gradle library에 자꾸 추가되어 바로 아래와 같이 수정하였다. => 문제 해결 안됨
  ```
  implementation group: 'org.springframework.boot', name: 'spring-boot-starter-web', version: '2.5.15'
  implementation('org.springframework.boot:spring-boot-starter-web') {
    exclude group: 'org.springframework.boot', module: 'spring-boot-starter-logging'
    exclude group: 'org.springframework.boot', module: 'spring-boot-starter-log4j2'
    exclude group: 'org.springframework.boot', module: 'spring-boot-starter-tomcat'
    exclude group: 'org.apache.tomcat.embed', module: 'tomcat-embed-core'
    exclude group: 'org.apache.tomcat.embed', module: 'tomcat-embed-el'
    exclude group: 'org.apache.tomcat.embed', module: 'tomcat-embed-websocket'
  }
  ```
  3. configurations.all에서 tomcat exclude 처리하는 방식 => tomcat제외 됨
    - dependencies library 의존성 문제되는 것들 제외하는 로직
  ```
  configurations.all {
    exclude group: "org.springframework.boot", module: "spring-boot-starter-tomcat"
    exclude group: "org.apache.tomcat.embed", module: "tomcat-embed-el"
  }
  ```
  - org.springframework.context.ApplicationContextException: Unable to start web server; nested exception is org.springframework.context.ApplicationContextException: Unable to start ServletWebServerApplicationContext due to missing ServletWebServerFactory bean.
  1. application.yml에 해당 변수 추가함
    - wildfly run은 문제 없는데 bootRun시 에러나는 문제로 아래 변수 추가 하면 run은 되지만 서버 설정 ex) db, port 이런 설정이 다 작업이 안돼서 더 봐야할 듯
  ```
  spring:
    profiles: prod
    main:
      web-application-type: none
  ```
---
- [spring-boot-library 1.5.22 version](https://mvnrepository.com/artifact/org.springframework.boot/spring-boot/1.5.22.RELEASE)
- 요약 : 공부하다 알게 된 점
  - 2.x 버전 이상 부터는 war SKIPPED되는 이슈가 있어서 아래처럼 build.gradle 설정에 이렇게 작업해줘야 함
  ```
    war {
      enabled = true
    }
  ```
