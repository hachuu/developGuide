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
  - Q. origin을 꼭 써야 하는지?
  - A. 안써도 됨, git commit, push는 해야함

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

9. git remote update
- 원격 저장소의 git을 update해줌

10. git branch
- 로컬저장소의 브랜치 목록

11. git branch -r
- *원격저장소*의 브랜치 리스트

12. git branch -a
- 모든 브랜치의 리스트

13. git branch 삭제
  1. git branch 원격 삭제
```
방법 1
git push origin --delete estimate
방법 2
git branch -d estimate
git push origin estimate
```
  
  2. git 로컬 삭제
```
git branch -d estimate // commit, push할 내용이 없는 branch인 경우
git branch -D estimate // 병합되지 않은 branch의 경우
```

14. git fetch
```
git fetch -p origin // remote 서버 브랜치 정보를 다시 가져옴
```


## git commit 과정

0. git rm --cached
- git rm => 원격 저장소와 로컬 저장소에 있는 파일을 삭제한다.
- git rm --cached => 원격 저장소에 있는 파일을 삭제한다. 로컬 저장소에 있는 파일은 삭제하지 않는다.
- git rm --cached node_modules -r 
출처:[마이구미의 HelloWorld](https://mygumi.tistory.com/103)

1. add: 수정 파일 add
- git add .

2. commit
- git commit -m "commit하고 싶은 내용" => commit
- git commit --amend  => commit 메세지 변경

3. reset: commit 취소
- git reset --hard HEAD => 원격 저장소 마지막 commit 상태로 되돌림
- git reset HEAD^ 가장 최근의 commit 취소 (HEAD^는 git commit id 번호)
[git reset/revert](https://www.devpools.kr/2017/02/05/%EC%B4%88%EB%B3%B4%EC%9A%A9-git-%EB%90%98%EB%8F%8C%EB%A6%AC%EA%B8%B0-reset-revert/)

* git reset --hard gitversion
* git push -f origin master => 현재 소스 기준으로 강제 Push
* 원하는 git version으로 되돌릴때

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
- [git merge rebase 차이](https://firework-ham.tistory.com/12)

1. rebase? 두 개의 공통 Base를 가진 Branch에서 한 Branch의 Base를 다른 Branch의 최신 커밋으로 branch의 base를 옮기는 작업
2. [출처](https://backlog.com/git-tutorial/kr/stepup/stepup2_8.html)
```
$ git checkout issue3
Switched to branch 'issue3'
$ git rebase master
First, rewinding head to replay your work on top of it...
Applying: pull 설명을 추가
Using index info to reconstruct a base tree...
<stdin>:13: new blank line at EOF.
+
warning: 1 line adds whitespace errors.
Falling back to patching base and 3-way merge...
Auto-merging myfile.txt
CONFLICT (content): Merge conflict in myfile.txt
Failed to merge in the changes.
Patch failed at 0001 pull 설명을 추가

When you have resolved this problem run "git rebase --continue".
If you would prefer to skip this patch, instead run "git rebase --skip".
To check out the original branch and stop rebasing run "git rebase --abort".
```
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

5. git cherrypick: 
- [git cherry pick 예제](https://medium.com/react-native-seoul/git-cherry-pick-%EC%82%AC%EC%9A%A9%EB%B2%95-fe1a3346bd27)

6. 워킹 디렉토리, header, index 개념
- [Git 도구 - Reset 명확히 알고 가기](https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-Reset-%EB%AA%85%ED%99%95%ED%9E%88-%EC%95%8C%EA%B3%A0-%EA%B0%80%EA%B8%B0)

7. 서브모듈
[Git 도구 - 서브모듈](https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-%EC%84%9C%EB%B8%8C%EB%AA%A8%EB%93%88)
```
git clone --recurse-submodules {git url}
```

8. github 페이지 배포
- [[React] 프로젝트 GitHub Pages 배포하기](https://velog.io/@byjihye/react-github-pages)

9. git pull시 에러 fatal: refusing to merge unrelated histories
- [git push, pull (fatal: refusing to merge unrelated histories) 에러](https://jobc.tistory.com/177)

10. git commit 시 에러 Your branch is up to date with 'origin/master'
- [Your branch is up to date with 'origin/master'](https://log-laboratory.tistory.com/213)

11. gitHub repository 연결
- [GitHub Repository(원격저장소) 생성, GitBash로 연결, 초대하기](https://goddaehee.tistory.com/221)

12. git repository 해제
```
git remote remove origin
```

13. gitignore 적용 안될때
- .gitignore가 적용안되고 changes에 나오는 경우
- 원인 : git의 캐시가 문제
- 해결 : 캐시 내용을 전부 삭제후 다시 add All해서 커밋하시면 됩니다.
```
git rm -r --cached .
git add .
git commit -m "fixed untracked files"
```

14. git ssh key 생성
[Git 서버 - SSH 공개키 만들기](https://git-scm.com/book/ko/v2/Git-%EC%84%9C%EB%B2%84-SSH-%EA%B3%B5%EA%B0%9C%ED%82%A4-%EB%A7%8C%EB%93%A4%EA%B8%B0)

15. git log 확인
```
 git log : 현재 브랜치에 대한 로그 커밋만

 git log --branches : 모든 브랜치의 로그 출력

 git log  --branches --decorate : 모든 브랜치의 브랜치명 표시

 git log  --branches --decorate --graph : 로그 왼쪽에 그래프가 출력

 git log  --branches --decorate --graph --online : 간단하게 볼 수 있도록 표시
```

16. git remote repository 변경 방법
```
git remote set-url origin {git url}
git remote -v // 원격 주소 확인
git push origin master // git push
+ git remote update origin --prune // 원격 repository와 동기화 시키기
```

18. 특정 버전 clone하기
```
git reset --hard {git version}
```
19. 삭제된 원격 브랜치 vscode에서 업데이트 안되는 문제 해결
```
git remote prune origin
```

