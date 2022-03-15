# 변수 정의
- ! vs ?
  - ! : null이 아닌 assertion 연산자 혹은 확정 할당 assertion => 변수의 값이 무조건 존재한다고 확신할 때 사용
  - ? : optional 필수값이 아닌 옵셔널한 값
 
# 제네릭
- 정의 : 어떠한 클래스 혹은 함수에서 사용할 타입을 그 함수나 클래스를 사용할 때 결정하는 프로그래밍 기법
- any와 다른점 : any는 param, response의 타입을 미정으로 두는 반면 제네릭은 객체를 생성시 타입을 지정할 수 있어 type을 알 수 있다.
- 장점
  1. 제네릭을 사용하면 잘못된 타입이 들어올 수 있는 것을 컴파일 단계에서 방지할 수 있다.

  2. 클래스 외부에서 타입을 지정해주기 때문에 따로 타입을 체크하고 변환해줄 필요가 없다. 즉, 관리하기가 편하다.

  3. 비슷한 기능을 지원하는 경우 코드의 재사용성이 높아진다.
```
export class ApiService {
  buildApi<T, U>(apiSpec: ApiSpec<T, U>, store?: boolean) {
    let api: Api<T, U> = new Api(this.platformId, this.http, this.state, apiSpec, store);

    return api;
  }
}

getSessionApi: Api<void, ResponseModel<Session>>;
constructor(
    private apiService: ApiService
) {
  this.getSessionApi = this.apiService.buildApi(getSessionApiSpec, true);
}
```
```
  interface DropdownItem<T> {
    value: T
    selected: boolean
  }
  
  const emails: Dropdownitem<string> = {
    value: 'naver.com', selected: true
  }
```

# Union type
- 정의 : any 대신 쓸 수 있는 타입 별칭/ 하나 이상의 타입을 명시
- cf : intersection type : &로 묶여있음 (잘 안쓰임)
```
const age: string | number
```

# Enums 이넘
- 정의 : 특징 값들의 집합을 의미
```
  enum Shoes {
    Nike,
    Adidas
  }
  const nike = Shoes.Nike;
  console.log(nike); // 0 => 값에 대한 초기값을 설정하지 않은 경우
```
```
  enum Shoes {
    Nike = '나이키',
    Adidas = '아디다스'
  }
  const nike = Shoes.Nike;
  console.log(nike); // 나이키
```
```
"use strict";
var Shoes;
(function (Shoes) {
    Shoes["Nike"] = "\uB098\uC774\uD0A4";
    Shoes["Adidas"] = "\uC544\uB514\uB2E4\uC2A4";
})(Shoes || (Shoes = {}));
const nike = Shoes.Nike;
```
