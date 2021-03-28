# React 정리

---
*스터디하면서 알게된 점들*

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
```
let { id } = useParam();
Router/:id
```

## react to do admin
- [React 041. Socket.IO로 실시간 채팅 구현
](https://m.blog.naver.com/PostView.nhn?blogId=bkcaller&logNo=221366361792&proxyReferer=https:%2F%2Fwww.google.co.kr%2F)
- 배포 [A3 CDN] (https://youtu.be/-DDGYzKtNwc)
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
