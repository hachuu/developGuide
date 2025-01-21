# Spring boot upgrade
----------------------------------------------------------------------

## 작업 요약
- 사건 발단 : Logback 1.2.9 취약성 발견 => 업그레이드 필요
- 이슈 : 오픈 소스 보안취약점 검사 이력을 진행 도중 logback 뿐만 아니라 spring boot 2.5.15, junit, apache tomcat에서도 취약점 검출됨
- 해결 방안 : 취약점 오픈소스 SW를 올릴 겸, java 8에서 최대로 올릴 수 있는 spring boot version을 업데이트하면서 문제를 해결하자.
- 추가 작업 : gradle version, wildfly version도 올려야하는 문제 발생
- 작업 소요 시간 : 3~4개월 (스터디 및 실제 개발 2개월, 테스트 2개월, 진단 검수과정 1개월)

## 작업 내용
- 변경 파일 리스트
  ```
  // version upgrade 관련
  1. build.gradle
  2. GboxSrvappApplication.java
  3. application.yml
  4. logback.xml
  5. jboss-deployment-structure.xml
  6. GboxSrvappApplicationTests.java
  7. gradle-wrapper.properties

  // 배치 관련
  1. gboxScholasticTutorMapper.xml
  2. AbstractGboxBatch.java
  3. ScholasticTutorBatchService.java
  4. GboxBatchConfig.java
  5. GboxScholasticTutorDao.java
  6. ScholasticTutorService.java
  ```

### 각 파일 별 수정 사항과 변경 이유
**[version upgrade 설정 부분 수정 사항]**
1. build.gradle
  - dependencies에 명시하는 compile, providedRuntime, testCompile, runtime이 implementation providedRuntime, runtimeOnly 등으로 변경
     
     - compile => implementation
     - providedRuntime = providedRuntime
     - testCompile => implementation
     - runtime => runtimeOnly
    
  - providedRuntime 으로 선언해야하는 embed tomcat 생성
  - jar 선언시 baseName, version 명시 표시 방법이 바뀜
```
jar {
   baseName = ''; // => archiveBaseName.set('');
   version = ''; // => archiveVersion.set('');
}
```
2. GboxSrvappApplication.java
  - System.setProperty("org.springframework.boot.logging.LoggingSystem", "none"); 선언
    - Spring Boot는 기본적으로 로깅 시스템을 자동으로 구성합니다. 하지만 개발자가 직접 로깅 시스템을 관리하거나, 타사 로깅 프레임워크를 사용하려는 경우 Spring Boot의 기본 로깅 시스템을 비활성화할 필요가 있습니다.
    - Spring Boot 내장 로깅을 비활성화하여 로그 출력으로 인해 테스트 결과가 혼란스럽지 않게 함 => logback에 설정한 로깅 값만 나오도록 변경
3. application.yml
  - spring.profiles를 spring.config.activate.on-profile로 변경 => Spring Boot 2.4.0 이후로는 spring.config.activate.on-profile를 사용하는 것이 권장 (spring.profiles는 deprecated)
  - spring.main.main-class 추가
     - Gradle 및 기타 빌드 도구와의 통합: Gradle이나 다른 빌드 도구와 통합할 때 명시적인 메인 클래스 설정이 필요할 수 있습니다. 이는 빌드 도구가 애플리케이션을 실행하거나 패키징할 때 올바른 메인 클래스를 사용할 수 있도록 합니다.
     - 클래스를 명시적으로 설정하여 빌드 및 실행 환경에서의 명확성과 호환성을 높이기 위함입니다.
    
4. logback.xml
  - logback-spring.xml 파일에서 logback.xml파일 명칭 변경
    - Logback 1.3.x에서는 초기화 과정에서 Spring Boot가 logback-spring.xml 파일을 처리하는 방식과 충돌이 발생할 수 있습니다. 이로 인해 초기화 오류나 예상치 못한 동작이 발생할 가능성이 있습니다.
    - logback.xml을 사용하면 Logback이 독립적으로 초기화될 수 있어 이러한 문제를 피할 수 있습니다.
5. jboss-deployment-structure.xml
  - 특정 모듈을 제외하는 설정을 추가
    - JBoss/WildFly 서버의 기본 로깅 시스템과 애플리케이션의 로깅 시스템 간의 충돌을 피하고, 원하는 로깅 시스템(Logback)을 제대로 작동하게 하기 위함입니다.
6. GboxSrvappApplicationTests.java
  - junit library 버전 변경으로 인한 import 변경
7. gradle-wrapper.properties
  - distributionUrl 의 target gradle version 변경

**[version upgrade 배치 변경 작업]**
1. AbstractGboxBatch.java
  - 기존 batch 변경 작업으로 해당 파일 삭제 -> [배치 변경 작업 내용 정리](https://github.com/hachuu/developGuide/blob/main/java/%EC%8A%A4%ED%94%84%EB%A7%81%20%EB%B0%B0%EC%B9%98%20%EB%A7%8C%EB%93%A4%EA%B8%B0.md)
2. ScholasticTutorBatchService.java
  - CronTrigger 및 ApplicationRunner 배치 작업 -> [배치 변경 작업 내용 정리](https://github.com/hachuu/developGuide/blob/main/java/%EC%8A%A4%ED%94%84%EB%A7%81%20%EB%B0%B0%EC%B9%98%20%EB%A7%8C%EB%93%A4%EA%B8%B0.md)
3. GboxBatchConfig.java
  - batch 서버인지 판별하는 로직에서 isEmpty -> hasText로 변경 작업 (StringUtils.hasText)
    - 기존 null이거나 빈 문자열을 체크하는 isEmpty가 null, 비어 있지 않고, 실제 텍스트를 포함하는지 확인하는 hasText로 변경함.
```
// Deprecated 방법
if (StringUtils.isEmpty(str)) {
    // 문자열이 null 또는 비어 있음
}

// 권장 방법
if (!StringUtils.hasText(str)) {
    // 문자열이 null이거나 비어 있거나 공백만 있음
}
``` 
  

## 인사이트 (이번 작업하면서 알게 되었던 것들...)
1. gradle bootRun 및 WildFly 서버로 Spring Boot 애플리케이션을 실행하는 주요 차이점
  - 내장 웹 서버 vs. 외부 애플리케이션 서버:
      - **`gradle bootRun`**: **`gradle bootRun`** 명령을 사용하면 Spring Boot 애플리케이션을 내장 웹 서버 (일반적으로 Tomcat, Jetty 또는 Undertow)에서 실행합니다. 즉, 애플리케이션과 웹 서버가 함께 패키지되어 있으며 독립 실행 가능한 JAR 파일 또는 WAR 파일로 실행됩니다.
      - WildFly Server: WildFly (이전에는 JBoss)와 같은 외부 애플리케이션 서버를 사용하는 경우 Spring Boot 애플리케이션은 외부 서버에서 실행됩니다. 애플리케이션은 서버의 컨테이너 내에서 실행되며 서버의 관리 및 설정이 필요합니다. 애플리케이션은 서버에 배포된 WAR 파일로 실행됩니다.
  - 배포 및 구성:
      - **`gradle bootRun`**: Spring Boot의 내장 웹 서버를 사용하면 애플리케이션을 JAR 파일로 패키지하고 간단하게 실행할 수 있습니다. 애플리케이션의 구성은 애플리케이션 소스 코드와 함께 제공되며 **`application.properties`** 또는 **`application.yml`** 파일을 통해 설정됩니다.
      - WildFly Server: 외부 애플리케이션 서버를 사용하는 경우 애플리케이션을 WAR 파일로 패키지하고 서버에 배포해야 합니다. 서버의 설정 및 구성은 서버 관리자 또는 설정 파일을 통해 수행됩니다.
  - 환경 및 운영:
      - **`gradle bootRun`**: **`gradle bootRun`**을 사용하면 개발 및 로컬 테스트 목적으로 애플리케이션을 간단히 실행할 수 있습니다. 주로 개발 환경에서 사용됩니다.
      - WildFly Server: 외부 애플리케이션 서버를 사용하면 애플리케이션을 본격적인 프로덕션 환경에서 실행할 수 있습니다. 서버 환경에서 대규모 및 실제 운영용 애플리케이션을 호스팅하는 데 사용됩니다.
  - 서버 종속성:
      - **`gradle bootRun`**: Spring Boot의 내장 웹 서버는 애플리케이션과 함께 제공되므로 별도의 웹 서버 설치나 구성이 필요하지 않습니다.
      - WildFly Server: 외부 애플리케이션 서버를 사용하려면 해당 서버 (예: WildFly)를 설치하고 구성해야 합니다.

2. gradle bootrun에서 providedRuntime로 tomcat을 선언 (cf. wildfly에서는 tomcat이 필요하지 않을까)
  - 이유 :
      - **`gradle bootRun`** 명령을 사용할 때 Tomcat이 필요한 이유는 Spring Boot 애플리케이션을 내장 서블릿 컨테이너로 실행하려는 것입니다. 
      - Spring Boot는 기본적으로 내장 서블릿 컨테이너로 Tomcat을 사용하며, **`bootRun`** 명령은 내장 서블릿 컨테이너를 시작하고 애플리케이션을 실행하는 것을 의미합니다.
      - Wildfly에서는 **`gradle bootRun`**을 사용하는 대신 Wildfly 애플리케이션 서버를 사용하므로 내장 서블릿 컨테이너가 필요하지 않습니다. 
      - Wildfly는 Java EE (Enterprise Edition) 애플리케이션 서버로, Spring Boot의 애플리케이션을 Wildfly에 배포하고 실행할 때는 Wildfly의 서블릿 컨테이너를 사용합니다.
      - 따라서 **`gradle bootRun`**을 실행하면 Spring Boot 애플리케이션은 Tomcat을 내장 서블릿 컨테이너로 사용하며, 배포 환경에 따라 다른 서블릿 컨테이너나 애플리케이션 서버를 사용할 수 있습니다. Wildfly에서 Spring Boot 애플리케이션을 실행하는 경우에는 Tomcat이 필요하지 않습니다.
  - 동작 :
      - Wildfly 같은 외부 애플리케이션 서버를 사용하는 경우, spring-boot-starter-tomcat과 tomcat-embed-el 의존성을 providedRuntime으로 추가하면 더 이상 내장 Tomcat이 포함되지 않고 애플리케이션 서버에서 실행될 것입니다.
      - 이것이 Wildfly와 같은 외부 서버에서 Spring Boot 애플리케이션을 실행할 때 필요한 설정 중 하나입니다.

3. application.yml에서 context-path '/' 설정
  - 루트 컨텍스트 설정
    - context-path 설정은 애플리케이션의 URL 경로에서 루트 경로를 설정합니다.
    - /로 설정하면 애플리케이션이 웹 서버의 루트 경로에서 시작됩니다. (예를 들어, 'http://localhost:8080/' 가 애플리케이션의 기본 URL이 됩니다.)
  - 단일 애플리케이션 배포
    - 이 설정은 단일 애플리케이션을 루트 컨텍스트에서 제공할 때 유용합니다.
    - 특히, 마이크로서비스 아키텍처나 독립적으로 실행되는 애플리케이션에서는 루트 경로에서 애플리케이션을 제공하는 것이 일반적입니다.

4. application.yml에서 spring.main.web-application-type: servlet설정
  - 서블릿 기반 웹 애플리케이션
    - Spring Boot는 기본적으로 여러 유형의 웹 애플리케이션을 지원합니다. servlet, reactive, none 세 가지 유형이 있습니다. 여기서 servlet은 전통적인 서블릿 기반 웹 애플리케이션을 나타냅니다.
    - spring.main.web-application-type: servlet은 애플리케이션이 서블릿 컨테이너(Tomcat, Jetty, Undertow 등)에서 실행되는 표준 서블릿 기반 웹 애플리케이션임을 명시합니다.

