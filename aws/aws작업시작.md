# AWS + Nextjs + GitHub 연동

## AWS 세팅 순서
1. 인스턴스 생성
2. 인스턴스에 IAM 설정
3. IAM > 역할 생성 > 권한 추가
4. 인스턴스 > 작업 > 보안 > IAM 역할 수정 > 생성한 IAM 연결
5. s3생성
6. 버킷 생성
7. IAM > 사용자 정책 연결
8. github에서 Secrets key 연결

## AWS 세팅하는 방법
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

### DNS 접속안되는 경우 해결 방법
- 아직 시도 중 ㅜㅜ
1. su root 계정 접속
2. iptables -A PREROUTING -t nat -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8080
3. service iptables save (설정 저장 명령어 인데 저장이 안되어서 다른 것으로 진행함) [출처](https://steady-snail.tistory.com/153)
3-1. ubuntu 버전문제로 위 명령어가 실행안되는 경우 아래처럼 진행
```
apt-get install iptables-persistent
netfilter-persistent save
netfilter-persistent reload
```
4. 접속해보기 
- s3 버킷에서 정적 파일 업로드 후 권한 생성 작업 
- [출처](https://weekwith.tistory.com/entry/Nextjs-AWS-S3%EB%A5%BC-%ED%86%B5%ED%95%9C-%EC%A0%95%EC%A0%81-%EC%9B%B9-%EC%82%AC%EC%9D%B4%ED%8A%B8-%EB%B0%B0%ED%8F%AC-%EB%B0%8F-GitHub-Actions%E1%84%85%E1%85%B3%E1%86%AF-%E1%84%90%E1%85%A9%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB-CICD)
