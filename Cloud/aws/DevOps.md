# AWS 교육

## DEVOPS

1. ec2 vm 서버 환경
2. container 환경
3. serverless 배포 전략

### 목표 : CICD PipeLine

---

- 강의 진행 일정
    1. 월요일
    - 인프라 자동화
    - CodeDeploy
    
    2. 화요일
    - ec2
    - 마이크로서비스 (Container) 배포
    
    3. 수요일
    - CodePipeline

---

### 09/18 Day1

- **AWS DevOps 특징**
    - **C**ulture 문화철학
    - **A**utomation 자동화
    - **M**easure 측정
    - **S**haring 공유
- CICD TOOL
    - code commit : aws에서 사용하는 git 툴킷 ex)gitlab..
    - code build
    - code deploy
- ETC
    
    ```sql
    외부에 소스 관리를 한다 s3에서 관리하여 이벤트 있는 경우 연동시킬 수 있음 ex) github 소스에서 s3 연동
    artifact : 빌드 결과 
    bucket
    iam : aws 권한 - Authentication : 인증 / Authorization : 부여
    lambda : function
    ```

---

### 09/19 Day2

- 실습 2 : EC2배포
- 실습 3 : pipeline
- Docker, 컨테이너화
- Fargate : 컨테이너를 위한 서버리스 컴퓨팅 엔징 (task) vs k8s (pod)
- Elastic Container Service
- API gateway + lambda 를 pipeline에 구축하여 배포함

---

### 09/20 Day3

### ⭐️실습 5: CI/CD 파이프라인 및 Amazon Elastic Container Service를 사용하여 블루/그린 배포 수행

- 이 실습에서는 CI/CD 파이프라인을 빌드하여 웹 애플리케이션을 배포하고 파이프라인을 구성해 블루/그린 배포 모델을 실행합니다. 이번 실습에서는 AWS Cloud9, AWS CodeBuild, AWS CodeCommit, AWS CodeDeploy, AWS CodePipeline, Amazon EC2 Container Registry(ECR), Amazon Elastic Container Service(ECS) 및 AWS Fargate를 사용하여 빌드할 사용자 지정 컨테이너 이미지상의 코드 빌드 및 배포를 오케스트레이션합니다.
- mocking 서버
    - dev target에서 test target 써드파티 접근이 어려운 경우 API gateway나 mocking서버를 두어 임의의 데이터를 return 시킬수 있도록 작업
- DevSecOps
    - https://yozm.wishket.com/magazine/detail/1553/
- policy
    - 생성 가능
    - ex) EC2FullAccess
    - IAM 사용자, 사용자그룹에게 역할권한을 부여하는 것은 영구적
    - ROLE 임시적 자격을 부여하는 것임
- AWS Config Rule
- Amazon CloudWatch 시스템 성능에 대한 데이터 보존
- AWS X-ray
