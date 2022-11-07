1. 출처 [promise](https://brunch.co.kr/@skykamja24/670)

---

1. Promise.all([])
- 다중으로 처리하는 비동기 처리
- 모든 비동기처리가 끝나야 다음 로직을 실행 할 수 있음
- 하나라도 문제가 생기는 경우 처리하기 곤란함

2. Promise.allSettled([])
- 각 프로미스의 이행 여부를 결과로 리턴
- 개별 프로미스 처리 가능 => 에러처리 용이
- .all보다 코드량이 많음

3. Promise.race([])
- 가장 빠른 프로미스에 대해서만 return
