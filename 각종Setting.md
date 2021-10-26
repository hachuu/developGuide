# Setting 정리 문서

## VSCode 세팅
[TSLint](http://ngmsoftware.com/bbs/board.php?bo_table=study&wr_id=266&sca=Error&sst=wr_datetime&sod=desc&sop=and&page=1)
=> eslint 변환 작업
- npm install --save-dev eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin
- npx tslint-to-eslint-config
- [tslint to eslint](https://pks2974.medium.com/tslint-%EC%97%90%EC%84%9C-eslint-%EB%A1%9C-%EC%9D%B4%EC%82%AC%ED%95%98%EA%B8%B0-ecd460a1e599)

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

## npm install 시 python이나 기타 모듈 내려받을 때 에러나는 경우
- powershell 관리자 권한으로 실행
- 해당 프로젝트 경로에서 하위를 입력
- [!!! 에러 해결법 총집합 !!! npm-gyp 오류/python 오류/truffle 컴파일 에러/Unknown network klaytn 에러 나시는 분들은](https://www.inflearn.com/questions/11540)
  - [python down grade](https://www.python.org/downloads/release/python-2710/)
```
npm install --global --production windows-build-tools
npm install --global node-gyp
```
- node_modules 삭제 명령어
```
rmdir node_modules /s /q 
rmdir node_modules /s /q  && npm install --legacy-peer-deps
```
### npm install 시 왠지 node때문인거 같을 때
```
 npm install -g n
 sudo n 14.15.4
```

### npm install 시 명령어 정리
```
-P, --save-prod: Package will appear in your dependencies. This is the default unless -D or -O are present.

-D, --save-dev: Package will appear in your devDependencies.

-O, --save-optional: Package will appear in your optionalDependencies.

--no-save: Prevents saving to dependencies.
```
*--save를 쓰지 않아도 되는 이유 추가: npm5 부터는 --save 옵션을 사용하지 않아도 dependencies에 항목을 추가해줌
출처: https://xtring-dev.tistory.com/entry/NPM-npm-install-할-때-save를-함께-입력하는-이유*
- [axios excel 파일 다운로드](https://soonh.tistory.com/38)

## Mac M1 세팅
[맥 세팅 작업중...](https://github.com/hachuu/developGuide/blob/main/MacSetting.md)
[GitHub ssh key 생성하고 등록하고 사용하기](https://syung05.tistory.com/20)
* window ssh key 생성 [Use SSH key authentication](https://docs.microsoft.com/en-us/azure/devops/repos/git/use-ssh-keys-to-authenticate?view=azure-devops)
```
~/.ssh
ssh-keygen -C "jamal@fabrikam.com"
```

## Setting Of Developement

- java
  1. [spring boot 프로젝트 생성](https://aljjabaegi.tistory.com/480)
  2. [eclipse setting](#eclipse-setting)
  3. [스프링 배치만들기](https://github.com/hachuu/developGuide/blob/main/%EC%8A%A4%ED%94%84%EB%A7%81%20%EB%B0%B0%EC%B9%98%20%EB%A7%8C%EB%93%A4%EA%B8%B0.md)
- Gradle
  1. [실제 gradle 설치 방법](https://park-jongseok.github.io/languages/java/2019/11/01/installing-gradle.html) - eclipse marketplace가 아님
  2. 'gradle'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는 배치 파일이 아닙니다. => 시스템 환경 변수 %GRADLE_HOME%\bin 순서를 상위로 옮겨줌.
  3. Run the init task (gradle init --type java-library) [출처](https://docs.gradle.org/current/samples/sample_building_java_libraries.html)

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
