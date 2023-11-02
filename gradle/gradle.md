# gradle 관련 Ref
- [gradle 공식 유저 가이드](https://docs.gradle.org/current/userguide/userguide.html)
- [gradle-dependencies](https://kwonnam.pe.kr/wiki/gradle/dependencies)
- [declaring dependencies](https://docs.gradle.org/current/userguide/declaring_dependencies.html)

- **`gradle bootRun`** 및 WildFly 서버로 Spring Boot 애플리케이션을 실행하는 주요 차이점
  1. 내장 웹 서버 vs. 외부 애플리케이션 서버:
      - **`gradle bootRun`**: **`gradle bootRun`** 명령을 사용하면 Spring Boot 애플리케이션을 내장 웹 서버 (일반적으로 Tomcat, Jetty 또는 Undertow)에서 실행합니다. 즉, 애플리케이션과 웹 서버가 함께 패키지되어 있으며 독립 실행 가능한 JAR 파일 또는 WAR 파일로 실행됩니다.
      - WildFly Server: WildFly (이전에는 JBoss)와 같은 외부 애플리케이션 서버를 사용하는 경우 Spring Boot 애플리케이션은 외부 서버에서 실행됩니다. 애플리케이션은 서버의 컨테이너 내에서 실행되며 서버의 관리 및 설정이 필요합니다. 애플리케이션은 서버에 배포된 WAR 파일로 실행됩니다.
  2. 배포 및 구성:
      - **`gradle bootRun`**: Spring Boot의 내장 웹 서버를 사용하면 애플리케이션을 JAR 파일로 패키지하고 간단하게 실행할 수 있습니다. 애플리케이션의 구성은 애플리케이션 소스 코드와 함께 제공되며 **`application.properties`** 또는 **`application.yml`** 파일을 통해 설정됩니다.
      - WildFly Server: 외부 애플리케이션 서버를 사용하는 경우 애플리케이션을 WAR 파일로 패키지하고 서버에 배포해야 합니다. 서버의 설정 및 구성은 서버 관리자 또는 설정 파일을 통해 수행됩니다.
  3. 환경 및 운영:
      - **`gradle bootRun`**: **`gradle bootRun`**을 사용하면 개발 및 로컬 테스트 목적으로 애플리케이션을 간단히 실행할 수 있습니다. 주로 개발 환경에서 사용됩니다.
      - WildFly Server: 외부 애플리케이션 서버를 사용하면 애플리케이션을 본격적인 프로덕션 환경에서 실행할 수 있습니다. 서버 환경에서 대규모 및 실제 운영용 애플리케이션을 호스팅하는 데 사용됩니다.
  4. 서버 종속성:
      - **`gradle bootRun`**: Spring Boot의 내장 웹 서버는 애플리케이션과 함께 제공되므로 별도의 웹 서버 설치나 구성이 필요하지 않습니다.
      - WildFly Server: 외부 애플리케이션 서버를 사용하려면 해당 서버 (예: WildFly)를 설치하고 구성해야 합니다.

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
  2. web-application-type: none으로 설정하는 경우 tomcat server를 띄우지못해 설정은 servlet으로 하고 tomcat을 띄우는 경우 configurations에서 tomcat을 exclude하는 로직을 지워야함!
  ```
  //configurations.all {
  //	exclude group: "org.springframework.boot", module: "spring-boot-starter-tomcat"
  //	exclude group: "org.apache.tomcat.embed", module: "tomcat-embed-el"
  //}

  spring:
  profiles: prod
  main:
    web-application-type: servlet
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
