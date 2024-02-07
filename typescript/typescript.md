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

# type 단언: 개발자가 타입을 알고 있으니 typescript에서 지정한 타입이 아닌 개발자가 지정한 타입으로 변수를 선언한다.
```
let div = document.querySelector('div') as HTMLDivElement;
div.innerText;
```

# type guard
```
function isDeveloper(target: Developer | Person): target is Developer {
  return ( target as Developer).skill !== undefined
}

if(isDeveloper(tony)){
  tony.skill
} else {
  tony.age
}
```

# 타입 호환
: 특정 타입이 다른 타입에 잘 맞는지를 의미

```
interface Developer {
  name: string;
  skill: string;
}
interface Person {
  name: string;
}
class Person {
  name: string;
}
var developer: Developer;
var person: Person;

developer = person; // 호환이 안됨 
person = developer; // 호환 됨 
developer = new Person(); // 호환 됨
```

- 구조적 타이핑 : interface나 class에 대한 차이를 비교하는 것이 아닌 {}값 안의 값을 호환될 수 있도록 하는 것
- 

# interface vs class
- 화면의 구현체는 class를 통해 작업
- 서버 단에 참조되는 것은 인터페이스 (인터페이스를 상속한 클래스로 변환시켜줌)

# TIL [extends implements](https://velog.io/@hkoo9329/%EC%9E%90%EB%B0%94-extends-implements-%EC%B0%A8%EC%9D%B4)
```
extends는 일반 클래스와 abstract 클래스 상속에 사용되고, implement는 interface 상속에 사용된다.
class가 class를 상속받을 땐 extends를 사용하고, interface가 interface를 상속 받을 땐 extends를 사용한다.
class가 interface를 사용할 땐 implements를 써야하고
interface가 class를 사용할 땐 implements를 쓸수 없다.
extends는 클래스 한 개만 상속 받을 수 있다.
extends 자신 클래스는 부모 클래스의 기능을 사용한다.
implements는 여러개 사용 가능하다.
implements는 설계 목적으로 구현 가능하다.
implements한 클래스는 implements의 내용을 다 사용해야 한다.
```

## How do you explicitly set a new property on `window` in TypeScript?
1. 방법1
```
declare global {
  interface Window { MyNamespace: any; }
}

window.MyNamespace = window.MyNamespace || {};
```
2. 방법2
```
    (window as any).tradlinx = this;
    (window as any).tradlinx.app = app;
```
