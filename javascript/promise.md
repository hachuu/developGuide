1. 출처 [promise](https://brunch.co.kr/@skykamja24/670)

---

1. Promise.all([])
- 다중으로 처리하는 비동기 처리
- 모든 비동기처리가 끝나야 다음 로직을 실행 할 수 있음
- 하나라도 문제가 생기는 경우 처리하기 곤란함
  - 예시 : promise.all시 모든 []에 대한 resolve() 처리가 하나라도 누락되는 경우 function이 먹통됨
    ```
            if (!this.isActiveModal) {
                return Promise.resolve(); // Promise를 즉시 완료하고 반환
            }

            const refsArr = [
                'service1',
                'service2',
                'service3',
                'service4',
                'service5',
                'service6'
            ];

            // Promise를 사용하여 각 모달을 차례로 닫기
            const closePromises = refsArr.map(refName => {
                return new Promise(resolve => {
                    if (this.$refs[refName].isActive) {
                        this.$refs[refName].hide();
                        resolve();
                    } else {
                        resolve();
                    }
                });
            });

            // 모든 Promise가 완료될 때까지 기다린 후 계속 진행
            return Promise.all(closePromises);
    ```

2. Promise.allSettled([])
- 각 프로미스의 이행 여부를 결과로 리턴
- 개별 프로미스 처리 가능 => 에러처리 용이
- .all보다 코드량이 많음

3. Promise.race([])
- 가장 빠른 프로미스에 대해서만 return
