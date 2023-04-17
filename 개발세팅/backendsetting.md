1. [IntellijGradleSetting](https://lifere.tistory.com/entry/Intellij-%EC%9D%B8%ED%85%94%EB%A6%AC%EC%A0%9C%EC%9D%B4-Refresh-Gradle-Dependencies)
2. [wildfly설치](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=yyj9301&logNo=221159017119)
3. [java 환경변수 등록](https://whitepaek.tistory.com/28)
4. [Intellij SDK(JDK) 설정 방법](https://atoz-develop.tistory.com/entry/IntelliJ-SDK-JDK-%EC%84%A4%EC%A0%95-%EB%B0%A9%EB%B2%95-cannot-start-compiler-the-sdk-is-not-specified)


## Java Spring Framework를 VS Code에서 실행 방법

1. Java 환경 설정하기: Java를 설치하고, JAVA_HOME 환경 변수를 설정합니다. Java 버전은 Spring Framework 버전에 따라 다릅니다. Java 8 이상이 필요합니다.
2. VS Code 설치: VS Code를 다운로드하고 설치합니다.
3. VS Code Extensions 설치: Java Extension Pack, Spring Boot Extension Pack 등 Spring Framework 개발에 필요한 Extension Pack을 설치합니다.
4. 프로젝트 가져오기: 이미 작성된 소스코드가 있으므로 해당 프로젝트를 가져옵니다.
5. 프로젝트 설정: 가져온 프로젝트의 설정 파일을 확인합니다. Spring Boot의 경우, application.properties 또는 application.yml 파일에서 포트 번호, 데이터베이스 등의 설정을 확인할 수 있습니다.
6. VS Code에서 터미널 열기: Ctrl+Shift+ 키를 누르거나, VS Code 메뉴에서 Terminal > New Terminal을 선택합니다.
7. Maven 빌드: 프로젝트 루트 디렉토리에서 mvn clean package 명령어를 실행합니다. 이 명령어는 Maven 라이브러리를 다운로드하고, 소스코드를 컴파일하여 실행 가능한 JAR 파일을 생성합니다.
8. JAR 파일 실행: java -jar target/[JAR 파일명] 명령어를 실행합니다. 이 명령어는 JAR 파일을 실행합니다.
9. 브라우저에서 확인: 브라우저에서 http://localhost:[포트번호]를 입력하여 결과를 확인합니다.

## JAVA_HOME환경 변수 설정하는 방법

1. Java를 설치합니다. Java 버전은 Spring Framework 버전에 따라 다릅니다. Java 8 이상이 필요합니다.
2. Java 설치 경로를 복사합니다. 예를 들어, Windows에서는 C:\Program Files\Java\jdk-16.0.1 경로를 복사합니다.
3. 시스템 환경 변수 편집 창을 엽니다. Windows에서는 제어판 > 시스템 및 보안 > 시스템 > 고급 시스템 설정 > 환경 변수를 선택합니다.
4. 새로 만들기 버튼을 클릭합니다.
5. 변수 이름 필드에 JAVA_HOME을 입력합니다.
6. 변수 값 필드에 복사한 Java 설치 경로를 붙여넣습니다.
7. 확인 버튼을 클릭합니다.
8. 시스템 변수 목록에서 Path를 선택하고, 편집 버튼을 클릭합니다.
9. 새로 만들기 버튼을 클릭하여 %JAVA_HOME%\bin을 추가합니다.
10. 변경사항을 저장하고 창을 닫습니다.
11. 이제 JAVA_HOME 환경 변수가 설정되었습니다. Java 개발환경에서 JAVA_HOME 환경 변수를 사용하여 Java 경로를 참조할 수 있습니다. 예를 들어, Maven을 사용할 때, JAVA_HOME 환경 변수를 참조하여 Java 경로를 설정합니다.

## 운영체제별 환경 변수를 만드는 방법
- Windows에서 환경 변수 만들기
1. 제어판 > 시스템 및 보안 > 시스템 > 고급 시스템 설정을 차례로 선택합니다.
2. 환경 변수 버튼을 클릭합니다.
3. 새로 만들기 버튼을 클릭합니다.
4. 변수 이름 필드에 변수 이름을 입력합니다.
5. 변수 값 필드에 변수 값(경로, 문자열 등)을 입력합니다.
6. 확인 버튼을 클릭합니다.

- Windows에서 시스템 변수에 추가하는 방법
1. 제어판 > 시스템 및 보안 > 시스템 > 고급 시스템 설정을 차례로 선택합니다.
2. 환경 변수 버튼을 클릭합니다.
3. 시스템 변수 목록에서 추가하려는 환경 변수를 선택합니다.
4. 편집 버튼을 클릭합니다.
5. 변수 값 필드에 환경 변수의 값(경로, 문자열 등)을 입력합니다.
6. 확인 버튼을 클릭합니다.

- Linux에서 환경 변수 만들기
1. 터미널을 엽니다.
2. export 명령어와 함께 변수 이름과 변수 값(경로, 문자열 등)을 입력합니다.
```
export 변수이름=변수값
```
3. .bashrc 파일에 환경 변수를 추가하여 영구적으로 설정할 수 있습니다. 다음 명령어를 입력하고, .bashrc 파일을 수정합니다.
```
nano ~/.bashrc
```
4. 파일 하단에 다음과 같은 구문을 추가합니다.
```
export 변수이름=변수값
```
5. Ctrl + X를 눌러 파일을 저장하고 종료합니다.
6. .bashrc 파일을 새로고침합니다.
```
source ~/.bashrc
```
7. 환경 변수가 성공적으로 만들어졌는지 확인하려면, echo 명령어와 함께 변수 이름을 입력합니다.
```
echo $변수이름
```
8. 변수 값이 출력되면, 환경 변수가 제대로 설정된 것입니다.

- Linux에서 시스템 변수에 추가하는 방법
1. 터미널을 엽니다.
2. sudo nano /etc/environment 명령어를 입력하여 환경 변수 설정 파일을 엽니다.
3. export 명령어와 함께 변수 이름과 변수 값(경로, 문자열 등)을 입력합니다.
```
변수이름=변수값
```
4. Ctrl + X를 눌러 파일을 저장하고 종료합니다.
5. source /etc/environment 명령어를 입력하여 변경 사항을 적용합니다.
6. 환경 변수가 시스템 변수에 추가된 후에는 새로운 터미널 창을 열어서 해당 환경 변수를 사용할 수 있습니다.
