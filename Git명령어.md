# 자주 쓰는 git 명령어 정리

1. clone 
- git clone {url} => git repository clone

2. remote
- git remote –v 현재 원격 저장소 주소 확인
- git remote add 
- git remote set-url {url} url 변경

3. branch
- git branch {branchName} 브랜치 생성
- git checkout {branchName} 브랜치 변경
- git checkout -b {branchName} 브랜치 전환 (브랜치 작성 및 체크아웃 동시에)
- git branch feature/{기능이름} => feature branch 생성
- git checkout feature/{기능이름} => feature branch checkout

4. pull
- git pull
- git pull {URL} => git fetch 와 git merge

5. config: git 계정 확인
- git config user.name => 계정 확인
- git config user.email => 계정 메일 확인

## git commit 과정

1. add: 수정 파일 add
- git add .

2. commit
- git commit -m "commit하고 싶은 내용" => commit
- git commit --amend  => commit 메세지 변경

3. reset: commit 취소
- git reset --hard HEAD => 원격 저장소 마지막 commit 상태로 되돌림
- git reset HEAD^ 가장 최근의 commit 취소

4. push
- git push origin master
- git push origin feature/{기능이름}
- git push -f origin master => 강제 push

5. 상태 확인
- git status
- git log => 전체 log 확인 무한 enter 후 나가고 싶을 때 q를 누르면 됨
- git log -g => 가장 최근 log 확인

6. merge
- git merge feature/{기능이름}

# 기타
- git config --global gui.encoding utf-8 => utf-8 한글깨짐 문제
