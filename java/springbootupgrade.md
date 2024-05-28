# Spring boot upgrade
----------------------------------------------------------------------

# 작업 내용

## 작업 요약
- 사건 발단 : Logback 1.2.9 취약성 발견 => 업그레이드 필요
- 이슈 : 오픈 소스 보안취약점 검사 이력을 진행 도중 logback 뿐만 아니라 spring boot 2.5.15, junit, apache tomcat에서도 취약점 검출됨
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
[version upgrade 설정 부분 수정 사항]
1. build.gradle
  1. dependencies에 명시하는 compile, providedRuntime, testCompile, runtime이 implementation providedRuntime, runtimeOnly 등으로 변경
     
     - compile => implementation
     - providedRuntime = providedRuntime
     - testCompile => implementation
     - runtime => runtimeOnly
    
  2. providedRuntime 으로 선언해야하는 embed tomcat 생성
  3. jar 선언시 baseName, version 명시 표시 방법이 바뀜
```
jar {
   baseName = ''; // => archiveBaseName.set('');
   version = ''; // => archiveVersion.set('');
}
```
2. GboxSrvappApplication.java
  1. System.setProperty("org.springframework.boot.logging.LoggingSystem", "none"); 선언
    - Spring Boot는 기본적으로 로깅 시스템을 자동으로 구성합니다. 하지만 개발자가 직접 로깅 시스템을 관리하거나, 타사 로깅 프레임워크를 사용하려는 경우 Spring Boot의 기본 로깅 시스템을 비활성화할 필요가 있습니다.
    - Spring Boot 내장 로깅을 비활성화하여 로그 출력으로 인해 테스트 결과가 혼란스럽지 않게 함 => logback에 설정한 로깅 값만 나오도록 변경
3. application.yml
  1. spring.profiles를 spring.config.activate.on-profile로 변경 => Spring Boot 2.4.0 이후로는 spring.config.activate.on-profile를 사용하는 것이 권장 (spring.profiles는 deprecated)
  2. spring.main.main-class 추가
     - Gradle 및 기타 빌드 도구와의 통합: Gradle이나 다른 빌드 도구와 통합할 때 명시적인 메인 클래스 설정이 필요할 수 있습니다. 이는 빌드 도구가 애플리케이션을 실행하거나 패키징할 때 올바른 메인 클래스를 사용할 수 있도록 합니다.
     - 클래스를 명시적으로 설정하여 빌드 및 실행 환경에서의 명확성과 호환성을 높이기 위함입니다.
    
4. logback.xml
  1. logback-spring.xml 파일에서 logback.xml파일 명칭 변경
    - Logback 1.3.x에서는 초기화 과정에서 Spring Boot가 logback-spring.xml 파일을 처리하는 방식과 충돌이 발생할 수 있습니다. 이로 인해 초기화 오류나 예상치 못한 동작이 발생할 가능성이 있습니다.
    - logback.xml을 사용하면 Logback이 독립적으로 초기화될 수 있어 이러한 문제를 피할 수 있습니다.
5. jboss-deployment-structure.xml
  1. 특정 모듈을 제외하는 설정을 추가
    - JBoss/WildFly 서버의 기본 로깅 시스템과 애플리케이션의 로깅 시스템 간의 충돌을 피하고, 원하는 로깅 시스템(Logback)을 제대로 작동하게 하기 위함입니다.
6. GboxSrvappApplicationTests.java
  1. junit library 버전 변경으로 인한 import 변경
7. gradle-wrapper.properties
  1. distributionUrl 의 target gradle version 변경

[version upgrade 배치 변경 작업]
1. AbstractGboxBatch.java
  1. 기존 batch 변경 작업으로 해당 파일 삭제 -> [작업 내용 정리](https://github.com/hachuu/developGuide/blob/main/java/%EC%8A%A4%ED%94%84%EB%A7%81%20%EB%B0%B0%EC%B9%98%20%EB%A7%8C%EB%93%A4%EA%B8%B0.md)
2. ScholasticTutorBatchService.java
3. GboxBatchConfig.java
  1. batch 서버인지 판별하는 로직에서 isEmpty -> hasText로 변경 작업 (StringUtils.hasText)
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
  

### 이번 작업하면서 알게 되었던 것들
