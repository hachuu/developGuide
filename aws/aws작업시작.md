# AWS + Nextjs + GitHub 연동

## AWS 세팅
### aws 인스턴스 생성 방법
- [출처](https://velog.io/@hajun-ryu/EC2-Github-Actions%EB%A1%9C-Next.js-%EB%B0%B0%ED%8F%AC-%EB%B0%8F-%EC%9E%90%EB%8F%99%ED%99%94CICD-1%ED%8E%B8-AWS-EC2-%EC%83%9D%EC%84%B1-%EB%B0%8F-%EC%84%A4%EC%A0%95)
- ec2 인스턴스 생성하는 방법 순차대로 진행하면됨

### windows에서 방법
- 해당 작업은 mac에서 진행하여 windows에서 진행하는 경우 chmod 400 명령어나 ssh 명령어가 작업이 되지 않는다.
- 기존 파일 속성에서 사용 권한 -> 속성 권한 사용하지 않음 후 현재 사용자만 등록하여 읽기 및 실행 & 읽기만 선택 후 작업
- [출처](https://tipsoda.com/2600)

### github actions와 aws 연동
- aws 인스턴스 생성 방법 여기서 사용자 추가에서 막혔다가 추가로 작업할 수 있었던 링크
- [출처](https://velog.io/@arthur/AWS-EC2%EC%99%80-Github-Actions%EB%A1%9C-%ED%94%84%EB%A1%A0%ED%8A%B8%EC%97%94%EB%93%9C-%EB%B0%B0%ED%8F%AC%ED%95%B4%EB%B3%B4%EA%B8%B0-3)

### github actions에서는 build 정상 작동하지만 aws에서는 배포 실패인 경우
- 확인해야 할 것
- ubuntu log 확인

```
cd /var/log/aws/codedeploy-agent
vi codedeploy-agent.log
// shift+g 맨 아래로 이동 한 후 로그 확인
```
- InstanceAgent::Plugins::CodeDeployPlugin::CommandPoller: Missing credentials - please check if this instance was started with an IAM instance profile
- [출처](https://sarc.io/index.php/aws/1327-tip-codedeploy-missing-credentials)
- sudo service codedeploy-agent restart 실행 후 sudo service codedeploy-agent status 실행해서 active인지 확인 후 배포 진행

### root 비밀번호 생성
```
sudo passwd root
```
