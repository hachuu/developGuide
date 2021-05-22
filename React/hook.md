

1. useEffect 패턴: 마운트/언마운트/업데이트시 할 작업

```
useEffect(() => {
    console.log('컴포넌트가 화면에 나타남');
    return () => {
      console.log('컴포넌트가 화면에서 사라짐');
    };
}, []);
```
- []에 값을 비우면 컴포넌트가 처음 나타나는 경우에만 useEffect안의 method가 실행됨.
- useEffect 안의 return으로 반환하는 것을 cleanup 함수 : deps 가 비어있는 경우에는 컴포넌트가 사라지는 경우 cleanup 함수가 호출된다.

```
useEffect(() => {
    console.log('user 값이 설정됨');
    console.log(user);
    return () => {
      console.log('user 가 바뀌기 전..');
      console.log(user);
    };
  , [user]);
```
- deps 안에 값이 있는 경우 언마운트시에도 호출, 값이 바뀌기 직전에도 호출

2. useMemo 패턴: 연산한 값 재사용
```
const countActiveUsers = () => {
    console.log('count active users..');
    return users.filter(user => user.active).length;
}
const count = useMemo(() => countActiveUsers(users), [users]);
```

- 'memoized' 를 의미, 이전에 계산 한 값을 재사용

3. useCallback 패턴: 함수 재사용
- useCallback 은 특정 함수를 새로 만들지 않고 재사용하고 싶을때 사용
- 함수들은 컴포넌트가 리렌더링 될 때 마다 새로 만들어짐
```
const onChange = useCallback(
    e => {
      const { name, value } = e.target;
      setInputs({
        ...inputs,
        [name]: value
      });
    },
    [inputs]
);
```
- [useCallback 을 사용하여 함수 재사용하기](https://react.vlpt.us/basic/18-useCallback.html)
*함수 안에서 사용하는 상태 혹은 props 가 있다면 꼭, deps 배열안에 포함시켜야 된다*

4. useReducer 패턴: 
- reducer 는 현재 상태와 액션 객체를 파라미터로 받아와서 새로운 상태를 반환해주는 함수
- 컴포넌트의 상태 업데이트 로직을 컴포넌트에서 분리할 수 있음

    4-1. action
    ```
    // 카운터에 1을 더하는 액션
    {
        type: 'INCREMENT'
    }
    // 카운터에 1을 빼는 액션
    {
    t   ype: 'DECREMENT'
    }
    // input 값을 바꾸는 액션
    {
        type: 'CHANGE_INPUT',
        key: 'email',
        value: 'tester@react.com'
    }
    // 새 할 일을 등록하는 액션
    {
        type: 'ADD_TODO',
        todo: {
            id: 1,
            text: 'useReducer 배우기',
            done: false,
        }
    }
    ```
    - type 값을 대문자와 _ 로 구성하는 관습이 존재하기도 하지만, 꼭 따라야 할 필요는 없음
    ```
    const [state, dispatch] = useReducer(reducer, initialState);
    // state: 컴포넌트에서 사용 할 수 있는 상태
    // dispatch: 액션을 발생시키는 함수
    ```
    ```
    dispatch({ type: 'INCREMENT' })
    ```
    - Reducer 예시 (지긋지긋한 Counter..)
    ```
    import React, { useReducer } from 'react';

    function reducer(state, action) {
    switch (action.type) {
        case 'INCREMENT':
        return state + 1;
        case 'DECREMENT':
        return state - 1;
        default:
        return state;
    }
    }

    function Counter() {
    const [number, dispatch] = useReducer(reducer, 0);

    const onIncrease = () => {
        dispatch({ type: 'INCREMENT' });
    };

    const onDecrease = () => {
        dispatch({ type: 'DECREMENT' });
    };

    return (
        <div>
        <h1>{number}</h1>
        <button onClick={onIncrease}>+1</button>
        <button onClick={onDecrease}>-1</button>
        </div>
    );
    }

    export default Counter;
    ```
    [useReducer 를 사용하여 상태 업데이트 로직 분리하기](https://react.vlpt.us/basic/20-useReducer.html)

    4-2. useReducer vs useState
    - 컴포넌트에서 관리하는 값이 여러개가 되어서 상태의 구조가 복잡해진다면 useReducer로 관리하는 것이 좋을 수도 있음

5. Custom hook
- 커스텀 Hooks 를 만드는 방법: 
useState, useEffect, useReducer, useCallback 등 Hooks 를 사용하여 원하는 기능을 구현해주고, 컴포넌트에서 사용하고 싶은 값들을 반환
```
function useInputs(initialForm) {

 ...(생략)
 return [form, onChange, reset];

 export default useInputs;
}
```

## 참조 url
https://react.vlpt.us/
