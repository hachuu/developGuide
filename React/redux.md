# ref
- [Redux](https://developerntraveler.tistory.com/144)
1. dispatch: action을 발생시키는 것
2. store: reducer를 통해 저장되는 state값
3. action: event들
4. reducer: 이벤트를 처리하는 리스너

## Redux ducks 패턴
- 정의 : Ducks 패턴은 구조중심이 아니라 기능중심으로 파일을 나눈 것
- 장점 : 기능을 수정할 때 하나의 파일만 다루면 되므로 직관적인 코드작성이 가능
- redux-toolkit의 createSlice

## createSlice
- redux-toolkit
- 간소한 코드작성 가능
- [Ducks 패턴](https://velog.io/@dolarge/React-Redux-Ducks-%ED%8C%A8%ED%84%B4)을 사용할 수 있음
