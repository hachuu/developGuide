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

6. git init
- 새로운 Git 저장소(repository)를 생성

7. git 생성, 삭제
- [Git Branch(1) - 기초(Branch 생성 및 사용)](https://goddaehee.tistory.com/274)

8. git repository 변경
- git remote set-url origin https://github.com/hachuu/react-blog.git

## git commit 과정

1. add: 수정 파일 add
- git add .

2. commit
- git commit -m "commit하고 싶은 내용" => commit
- git commit --amend  => commit 메세지 변경

3. reset: commit 취소
- git reset --hard HEAD => 원격 저장소 마지막 commit 상태로 되돌림
- git reset HEAD^ 가장 최근의 commit 취소
[git reset/revert](https://www.devpools.kr/2017/02/05/%EC%B4%88%EB%B3%B4%EC%9A%A9-git-%EB%90%98%EB%8F%8C%EB%A6%AC%EA%B8%B0-reset-revert/)
4. push
- git push origin master
- git push origin feature/{기능이름}
- git push -f origin master => 강제 push
- git push만 하고 싶을 때 [출처](https://www.daleseo.com/git-push/)
  1. git push -u origin master
  2. git config --global push.default current

5. 상태 확인
- git status
- git log => 전체 log 확인 무한 enter 후 나가고 싶을 때 q를 누르면 됨
- git log -g => 가장 최근 log 확인

### git merge
- git merge feature/{기능이름}

# 기타
1. 한글깨짐 문제
- git config --global gui.encoding utf-8 => utf-8 한글깨짐 문제
2. 임시 저장
- commit 말고 임시 저장 [git stash](https://m.blog.naver.com/PostView.nhn?blogId=lucy9211&logNo=221453954198&proxyReferer=https:%2F%2Fwww.google.com%2F)
3. git push 권한 문제 생길 때
```
git remote remove origin
git remote add origin https://hachuu@github.com/hachuu/angular_page.git
```
4. 코드 변경 이력 덮어쓰기
- [출처](https://www.daleseo.com/git-push/)
- git push -f origin my-feature

5. git cherrypick
- [git cherry pick 예제](https://medium.com/react-native-seoul/git-cherry-pick-%EC%82%AC%EC%9A%A9%EB%B2%95-fe1a3346bd27)

6. 워킹 디렉토리, header, index 개념
- [Git 도구 - Reset 명확히 알고 가기](https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-Reset-%EB%AA%85%ED%99%95%ED%9E%88-%EC%95%8C%EA%B3%A0-%EA%B0%80%EA%B8%B0)

7. 서브모듈
[Git 도구 - 서브모듈](https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-%EC%84%9C%EB%B8%8C%EB%AA%A8%EB%93%88)
