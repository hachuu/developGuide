[ReactJS | Firebase로 React 프로젝트 DB 연동 및 배포](https://pathas.tistory.com/214)

```
// firebase.js

import firebase from "firebase/app";
import "firebase/firestore";

const firebaseConfig = {
    // firebase 설정과 관련된 개인 정보
};

// firebaseConfig 정보로 firebase 시작
firebase.initializeApp(firebaseConfig);

// firebase의 firestore 인스턴스를 변수에 저장
const firestore = firebase.firestore();

export { firestore };
```


```
// App.js
import { firestore } from "./firebase";

const fetchData = useCallback(() => {
    
    let commentsData = [];

    // firestore.js에서 가져온 firestore 객체
    firestore
        .collection("comment-board") //  "comments" 컬렉션 반환
        .get() // "comments" 컬렉션의 모든 다큐먼트를 갖는 프로미스 반환
        .then((docs) => {
        // forEach 함수로 각각의 다큐먼트에 함수 실행
        docs.forEach((doc) => {
            // data(), id로 다큐먼트 필드, id 조회
            commentsData.push({ comment: doc.data().comment, id: doc.id });
        });
        // comments state에 받아온 데이터 추가
        setComments((prevComments) => prevComments.concat(commentsData));
    });
}, []);

// 최초 렌더링 이후에 실행하기 위해 useEffect 내부에서 함수 실행
useEffect(() => {
    fetchData();
}, [fetchData]);
```
