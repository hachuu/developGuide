```text
Fast campus 강의명 - Kubernetes와 Docker로 한 번에 끝내는 컨테이너 기반 MSA
파트 강의 자료 : https://github.com/tedilabs/fastcampus-devops
```

# 컨테이너 기술의 발전
- docker : Container Engine 중 하나
- 컨테이너 : 호스트 운영체제에서의 프로세스라고 보면 됨
  - 하나의 서버에서 관리하는 소프트 웨어
- 쿠버네티스 : Container orchestration system (사실상 표준으로 널리 사용되고 있는)
  - 여러 서버로 구성된 클러스터 환경에서 컨테이너 환경을 관리하는 기술

## 도커 기초
- 컨테이너 기반의 오픈소스 가상화 플랫폼
- 도커 빌드
임시 컨테이너 생성 > 명령어 수행 > 이미지로 저장 > 임시 컨테이너 삭제 > 새로 만든 이미지 기반 임시 컨테이너 생성 > 명령어 수행 > 이미지로 저장 > 임시 컨테이너 삭제 > … 의 과정을 계속해서 반복
- 서버 구현까지 [출처](https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html)
- [참조](https://www.slideshare.net/pyrasis/docker-fordummies-44424016)
