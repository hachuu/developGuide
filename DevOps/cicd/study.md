[Azure DevOps CI/CD](https://zerobig-k8s.tistory.com/59)


## Firebase 배포
```
npm run build
firebase init hosting
firebase deploy --only hosting
firebase serve --only hosting
```
```
yarn build
firebase deploy
```
[Firebase로 배포하기(yarn 명령어)](https://velog.io/@mygomi/Firebase%EB%A1%9C-%EB%B0%B0%ED%8F%AC%ED%95%98%EA%B8%B0yarn-%EB%AA%85%EB%A0%B9%EC%96%B4)

### Firebase 규칙 수정
- 읽기 데이터 수정
- [출처](https://fomaios.tistory.com/entry/Firebase-%EB%B3%B4%EC%95%88-%EA%B7%9C%EC%B9%99%EC%97%90-%EB%8C%80%ED%95%B4-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90)
  
## Azure 배포
### Storage, CDN 구조
- Storage 실 소스가 반영
  1. 스토리지 생성
  2. 정적 웹 사이트 사용 활성화 => 엔드포인트 활성화
- CDN 도메인 변경...
  1. 프로필 생성
- Storage - CDN 연결 작업
  1. 엔드포인트 추가
  2. 스토리지 생성에서 생긴 엔드포인트 연결
