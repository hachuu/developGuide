useCallback
- [useCallback 을 사용하여 함수 재사용하기](https://react.vlpt.us/basic/18-useCallback.html)

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
*함수 안에서 사용하는 상태 혹은 props 가 있다면 꼭, deps 배열안에 포함시켜야 된다*
```

4. useReducer 패턴: 
- reducer 는 현재 상태와 액션 객체를 파라미터로 받아와서 새로운 상태를 반환해주는 함수
- 컴포넌트의 상태 업데이트 로직을 컴포넌트에서 분리할 수 있음

## 참조 url
https://react.vlpt.us/
