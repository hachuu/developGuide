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
- 변경 파일 리스트 (12개)
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
1. build.gradle
  1. dependencies에 명시하는 compile, providedRuntime, testCompile, runtime이 implementation providedRuntime, runtimeOnly 등으로 변경
    ```
     compile => implementation
     providedRuntime = providedRuntime
     testCompile => implementation
     runtime => runtimeOnly
    ```
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
3. AbstractGboxBatch.java
  1. 기존 batch 변경 작업으로 해당 파일 삭제 -> [작업 내용 정리](https://github.com/hachuu/developGuide/blob/main/java/%EC%8A%A4%ED%94%84%EB%A7%81%20%EB%B0%B0%EC%B9%98%20%EB%A7%8C%EB%93%A4%EA%B8%B0.md)
4. 
  

### 이번 작업하면서 알게 되었던 것들
