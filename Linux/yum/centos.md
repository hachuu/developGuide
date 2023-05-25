# CentOS7 커널 업데이트 [출처](https://cjwoov.tistory.com/48)
1. 커널 버전 확인
```
- uname -r
- uname -msr
```

2. 운영체제 버전 확인
```
cat /etc/redhat-release
```

3.패키지 업데이트
```
yum -y update
```
4. elrepo 저장소 추가
```
rpm —import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
yum install https://www.elrepo.org/elrepo-release-7.0-4.el7.elrepo.noarch.rpm
```
5. elrepo 저장소 확인
```
yum repolist
```
6. 새로운 커널 설치
```
yum --enablerepo=elrepo-kernel install kernel-ml kernel-ml-devel
```
