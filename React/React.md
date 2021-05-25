# React 정리

---
*스터디하면서 알게된 점들*


- 리액트 컴포넌트는 하위 컴포넌트에서 바뀐 내용이 없더라도 상위에서 리랜더링되는 경우 하위 컴포넌트도 리랜더링 됨.

1. JSX 조건부 연산자
  1. 조건부 연산자
  ```
  const name = '리액트'
  return (
    <div>
      {name === '리액트' ? (
        <h1>리액트입니다.</h1>
      ) : (
        <h2>리액트가 아닙니다.</h2>
      )}
    </div>
  )
  ```

  2. AND 연산자(&&) 조건부 렌더링
  - 조건을 만족할 때에만 랜더링 하고 싶을 때

  ```
  const name = '리액트'
  return (
    <div>
      {name === '리액트' && 
        <h1>리액트입니다.</h1>
      }
    </div>
  )
  ```
2. 특수 문자 쓸때 문법
  ```
  Traffic {' & '} Sales // Traffic & Sales
  ```

3. useParams: urlParam을 가져올 수 있음
:은 아무 문자가 오든 간에 이 페이지로 이동 시켜주세요
```
let { id } = useParam();
<Route path="/detail/:id">
```

4. useEffect 
- 처음 랜더링 할 때만 쓰고 싶을 때
```
() => ({
}, [])
```
- inputData state가 변경될때만 쓰고 싶을 때
```
() => ({
}, [inputData])
```

5. Axios
- 서버에서 주고 받는 응답 데이터는 JSON 형식이 default이지만 axios로 받는 경우 object로 변환해줌

6. Suspense
- Suspense를 사용하면 컴포넌트가 렌더링되기 전까지 기다릴 수 있습니다. 이 예시에서는 두 컴포넌트가 데이터를 불러오는 비동기 API 호출을 기다립니다.
```
const resource = fetchProfileData();

function ProfilePage() {
  return (
    <Suspense fallback={<h1>Loading profile...</h1>}>
      <ProfileDetails />
      <Suspense fallback={<h1>Loading posts...</h1>}>
        <ProfileTimeline />
      </Suspense>
    </Suspense>
  );
}
```
- 출처: [데이터를 가져오기 위한 Suspense](https://ko.reactjs.org/docs/concurrent-mode-suspense.html)

7. PWA
*세팅파일* (CRA 사용하면 굳이 만들지 않아도 됨)
- manifest.json
- service-worker.js

- index.js 에서 serviceWorker.register();
- yarn build후 빌드 파일을 배포하면 됨

8. Memo
- 데이터 재 할당시 페이지 리로드가 일어나는데 memo로 불필요한 랜더링을 줄일 수 있다
```
export default React.memo(CreateUser);
```

9. [hook 정리](https://github.com/hachuu/developGuide/blob/main/React/hook.md)

10. Redux
- [React-redux 이해하기](https://www.howdy-mj.me/redux/react-redux-intro/)
- connect를 사용하여 dispatch, state를 가져옴

11. custom hook

12. container & presenter pattern
- [Presentational & Container 컴포넌트는 이제 그만](https://ridicorp.com/story/how-to-use-redux-in-ridi/)

13. React index.html의 설정값 확인
```
short_name: 사용자 홈 화면에서 아이콘 이름으로 사용
name: 웹앱 설치 배너에 사용
icons: 홈 화면에 추가할때 사용할 이미지
start_url: 웹앱 실행시 시작되는 URL 주소
display: 디스플레이 유형(fullscreen, standalone, browser 중 설정)
theme_color: 상단 툴바의 색상
background_color: 스플래시 화면 배경 색상
orientation: 특정 방향을 강제로 지정(landscape, portrait 중 설정)
```
- [초기 환경 세팅하기, create-react-app으로 앱 만들기](https://imki123.github.io/posts/29)
- [웹앱 매니페스트 & 서비스워커(Web App Manifest & Service Worker)](https://altenull.github.io/2018/03/09/%EC%9B%B9%EC%95%B1-%EB%A7%A4%EB%8B%88%ED%8E%98%EC%8A%A4%ED%8A%B8-%EC%84%9C%EB%B9%84%EC%8A%A4%EC%9B%8C%EC%BB%A4-Web-App-Manifest-Service-Worker/)

14. react 배포
14-1. 배포시 Loading chunk n failed. 에러 
- 원인: 이중 router 선언 시 baseurl을 설정하지 않아서 cdn js, css 경로를 못 불러옴
- 해결: index.html에 <base href="%PUBLIC_URL%/" /> 추가
  

## react to do admin
- [React 041. Socket.IO로 실시간 채팅 구현
](https://m.blog.naver.com/PostView.nhn?blogId=bkcaller&logNo=221366361792&proxyReferer=https:%2F%2Fwww.google.co.kr%2F)
- 배포 [A3 CDN] (https://youtube/-DDGYzKtNwc)
- [웹팩설정](https://ideveloper2.tistory.com/m/75)
- [CRA webpack setting](https://maxkim-j.github.io/posts/cra-webpack-config)
- production 모드로 빌드된 번들링 결과물에 해쉬코드를 붙이는 이유가 뭘까요? 브라우저에는 캐싱 기능이 존재하기 때문에 예전에 배포되었던 번들링 파일들의 일부를 저장하고 있습니다. 따라서 앱을 수정하고 다시 배포할 경우 캐싱되는 대상이 바뀌어야 하므로, 파일의 내용이 바뀌었다고 브라우저에게 알려줘야 할 필요가 생깁니다. 가장 쉽게 파일의 변경을 알려주는 방법은 이전과 다른 이름의 번들링 파일을 배포하는 것입니다. 그래서 수정해서 빌드할 때마다 바뀌는 해쉬코드를 번들링 결과물에 추가하면 브라우저에게 파일이 변경되었음을 쉽게 알려줄 수 있는 것이죠.
- [[React Router] react-router-dom의 HashRouter과 BrowserRouter의 차이 (BrowserRouter 를 사용하자!)](https://wonit.tistory.com/299)

- [React app Amazon s3에 배포하기](https://bongster88.blogspot.com/2019/08/welcome-file.html)
- [리액트 앱 AWS S3, CloudFront 에 배포하기](https://react-etc.vlpt.us/08.deploy-s3.html)
- [Java에서 OTP 인증하기 (w/ Google OTP)](https://medium.com/@eungook/java에서-otp-인증하기-w-google-otp-3f93d670f37b)
- [프론트에서 안전하게 로그인 처리하기 (ft. React)](https://velog.io/@yaytomato/%ED%94%84%EB%A1%A0%ED%8A%B8%EC%97%90%EC%84%9C-%EC%95%88%EC%A0%84%ED%95%98%EA%B2%8C-%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EC%B2%98%EB%A6%AC%ED%95%98%EA%B8%B0)
- hash router dom router hash는 서버내 호출하여 불안정할 수 있음

## React 개발시 참고할만한 reference

1. [30-Days-Of-React (1day: javascript)](https://github.com/Asabeneh/30-Days-Of-React/blob/master/01_Day_JavaScript_Refresher/01_javascript_refresher.md)
2. [강좌 7편 Component LifeCycle API](https://velopert.com/1130) => [리액트의 Hooks 완벽 정복하기](https://velog.io/@velopert/react-hooks) 이게 읽기 좀 더 편한듯..
3. [Api 연동하기](https://react.vlpt.us/integrate-api/01-basic.html)
4. [react-use gitHub](https://github.com/streamich/react-use)
5. [Context 와 함께 사용하기](https://react.vlpt.us/integrate-api/05-using-with-context.html#)
6. [React Router 제한적 경로 접근](https://velog.io/@public_danuel/Restrict-Route)

---

- [함수형 컴포넌트 클래스형 컴포넌트 차이](https://xiubindev.tistory.com/107)
- [React v17.0](https://reactjs.org/blog/2020/10/20/react-v17.html)
- [React version up & webpack version up](https://marlom.dev/upgrade-to-react-17-and-webpack-5)
- [[번역] useEffect 완벽 가이드](https://rinae.dev/posts/a-complete-guide-to-useeffect-ko)
- 상태 라이브러리 NgRx Store provides reactive state management for <b>Angular apps<b> inspired by Redux(React).
  - RxJS with React Hooks for state management
  - Rxjs를 store개념에 접근하여 상태를 관리하는 라이브로서 combineLatest map filter Observable등이 있다 [참조](https://blog.logrocket.com/rxjs-with-react-hooks-for-state-management/)
- [React-query](https://react-query.tanstack.com/docs/overview)
- [Jest를 이용해 Snapshot testing하기](https://wkdtjsgur100.github.io/jest-snapshot-testing/)
- [React-router-dom에서 Link 태그를 사용하는 법](https://codeameba.netlify.app/blog/how-to-use-link-tag)
- [몽고 db 연동 및 연결 3강](https://www.inflearn.com/course/%EB%94%B0%EB%9D%BC%ED%95%98%EB%A9%B0-%EB%B0%B0%EC%9A%B0%EB%8A%94-%EB%85%B8%EB%93%9C-%EB%A6%AC%EC%95%A1%ED%8A%B8-%EA%B8%B0%EB%B3%B8)
- [combinereducer](https://redux.js.org/api/combinereducers)

## React Native
1. Window로 react native 세팅
[Window로 react native 세팅](http://blog.eightbox.net/143)
