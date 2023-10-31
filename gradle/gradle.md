# gradle 관련 Ref
- [gradle 공식 유저 가이드](https://docs.gradle.org/current/userguide/userguide.html)
- [gradle-dependencies](https://kwonnam.pe.kr/wiki/gradle/dependencies)
- [declaring dependencies](https://docs.gradle.org/current/userguide/declaring_dependencies.html)

---
- [spring-boot-library 1.5.22 version](https://mvnrepository.com/artifact/org.springframework.boot/spring-boot/1.5.22.RELEASE)
- 공부하다 알게 된 점
  - 2.x 버전 이상 부터는 war SKIPPED되는 이슈가 있어서 아래처럼 build.gradle 설정에 이렇게 작업해줘야 함
    ```
      war {
        enabled = true
      }
    ```
