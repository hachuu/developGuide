# javascript 개념 정리

## ProtoType과 Instance
- Prototype : 객체를 만드는 기본 틀, 객체의 원형 속성과 기능(함수)이 들어있다.
- Instance : 프로토타입을 통해 새로 만들어진 객체. 객체의 속성과 함수를 사용할 수 있다.
  - object가 자신의 prototype chain으로 접근할 수 있는 모든 prototype.constructor는 자신을 인스턴스로 가지고 있다.

## javascript prototype
- javascript는 프로토타입기반 언어
- ![img](https://github.com/hachuu/developGuide/blob/main/image/prototype.PNG)
- 프로토타입 객체는 constructor 프로퍼티를 갖는다. 이 constructor 프로퍼티는 객체의 입장에서 자신을 생성한 객체를 가리킨다.

```javascript
function Person(name) {
  this.name = name;
}

var foo = new Person('Lee');

// Person() 생성자 함수에 의해 생성된 객체를 생성한 객체는 Person() 생성자 함수이다.
console.log(Person.prototype.constructor === Person); //true

// foo 객체를 생성한 객체는 Person() 생성자 함수이다.
console.log(foo.constructor === Person); //true

// Person() 생성자 함수를 생성한 객체는 Function() 생성자 함수이다.
console.log(Person.constructor === Function); // true
```

- __proto__속성은 모든 객체가 빠짐없이 가지고 있는 속성
- __proto__는 객체가 생성될 때 조상이었던 함수의 Prototype Object를 가리킴
- ![img](https://github.com/hachuu/developGuide/blob/main/image/prototype%20Object.PNG)

- 이렇게 __proto__속성을 통해 상위 프로토타입과 연결되어있는 형태를 프로토타입 체인(Chain)이라고 함

```javascript
var student = {
  name: 'Lee',
  score: 90
}
console.dir(student);
console.log(student.hasOwnProperty('name')); // true
console.log(student.__proto__ === Object.prototype); // true
console.log(Object.prototype.hasOwnProperty('hasOwnProperty')); // true
```

```javascript
function Person(name, gender) {
  this.name = name;
  this.gender = gender;
  this.sayHello = function(){
    console.log('Hi! my name is ' + this.name);
  };
}

var foo = new Person('Lee', 'male');

console.dir(Person);
console.dir(foo);

console.log(foo.__proto__ === Person.prototype);                // ① true
console.log(Person.prototype.__proto__ === Object.prototype);   // ② true
console.log(Person.prototype.constructor === Person);           // ③ true
console.log(Person.__proto__ === Function.prototype);           // ④ true
console.log(Function.prototype.__proto__ === Object.prototype); // ⑤ true
```

- __proto__ is deprecated in ES6. Object.getPrototypeOf 와 Object.setPrototypeOf


- ES5에서 프로토타입 기반 프로그래밍은 클래스가 필요없는(class-free) 객체지향 프로그래밍 스타일로 프로토타입 체인과 클로저 등으로 객체 지향 언어의 상속, 캡슐화(정보 은닉) 등의 개념을 구현할 수 있다.

**자바스크립트의 모든 객체는 프로토타입이라 불리는 또다른 객체를 내부적으로 참조할 수 있다. 객체는 프로토타입의 프로퍼티들을 자신의 프로퍼티로 가져온다**
**결국 자바스크립트의 객체는 자신의 프로토타입에 있는 프로퍼티들을 상속받는다.**

## javascript Class
- ECMA6 표준에서는 Class 문법이 추가

- 오버라이딩(Overriding)
상위 클래스가 가지고 있는 메소드를 하위 클래스가 재정의하여 사용하는 방식이다.
- 오버로딩(Overloading)
매개변수의 타입 또는 갯수가 다른, 같은 이름의 메소드를 구현하고 매개변수에 의해 메소드를 구별하여 호출하는 방식이다. 자바스크립트는 오버로딩을 지원하지 않지만 arguments 객체를 사용하여 구현할 수는 있다.

- 프로토타입과의 차이
- 자식 클래스의 정적 메소드 내부에서도 super 키워드를 사용하여 부모 클래스의 정적 메소드를 호출할 수 있다. 이는 자식 클래스는 프로토타입 체인에 의해 부모 클래스의 정적 메소드를 참조할 수 있기 때문이다.

- 하지만 자식 클래스의 일반 메소드(프로토타입 메소드) 내부에서는 super 키워드를 사용하여 부모 클래스의 정적 메소드를 호출할 수 없다. 이는 자식 클래스의 인스턴스는 프로토타입 체인에 의해 부모 클래스의 정적 메소드를 참조할 수 없기 때문이다.

## console 찍을 때 [object, object] 로 찍히는 경우 
```
JSON.stringify(data) // 에러 발생시
for (let val in data){
  console.log("키: "+JSON.stringify(val));
  console.log("값: "+data[val]);
}

```

## 호이스팅

- 정의 : 인터프리터가 변수와 함수의 메모리 공간을 선언 전에 미리 할당하는 것
- var vs let, const
*둘 다 호이스팅을 함 *
```
var 로 선언한 변수의 경우 호이스팅 시 undefined로 변수를 초기화
반면 let과 const로 선언한 변수의 경우 호이스팅 시 변수를 초기화하지 않습니다.
```
## 비동기처리
1. promise await 차이
- promise.then().catch()로 에러를 잡으면 되지만 await의 경우 try catch문으로 reject를 체크
2. 비동기처리에 따른 컨퍼런스
- [우아하게 비동기처리하기](https://m.youtube.com/watch?v=FvRtoViujGg&list=PL1DJtS1Hv1PiGXmgruP1_gM2TSvQiOsFL&index=15)

## 화살표 함수 [출처](https://ko.javascript.info/arrow-functions)
- this를 가지지 않는다.
```javascript
let foo = (x) => console.log(arguments);
foo(1, 2);
  VM170:1 Uncaught ReferenceError: arguments is not defined
      at foo (<anonymous>:1:30)
      at <anonymous>:1:1
      
foo.hasOwnProperty('arguments'); // false
```

```javascript
let foo = function () { console.log(arguments);};
foo(1, 2);
  Arguments(2) [1, 2, callee: ƒ, Symbol(Symbol.iterator): ƒ]
  0: 1
  1: 2
  callee: ƒ ()
  length: 2
  Symbol(Symbol.iterator): ƒ values()
  __proto__: Object
  
foo.hasOwnProperty('arguments'); // true
```

- arguments를 지원하지 않는다.
- new와 함께 호출할 수 없다.
-  화살표 함수는 super가 없다.

## Spread 연산자
- 함수의 인자로 사용하는 경우
```javascript
function foo(x, y, z) {
  console.log(x); // 1
  console.log(y); // 2
  console.log(z); // 3
}
const arr = [1, 2, 3];
foo(...arr); // 배열 요소를 개별 요소로 분리한다.
```

```javascript
// ...rest는 분리된 요소들을 함수 내부에 배열로 전달한다.
function foo(param, ...rest) {
  console.log(param); // 1
  console.log(rest); // [2, 3]
}
foo(1, 2, 3);
```

- 배열에서 사용하는 경우
1. concat
```javascript
var arr = [1, 2, 3];
console.log(arr.concat([4, 5, 6])); // [1, 2, 3, 4, 5, 6]
```
2. push
```javascript
var arr1 = [1, 2, 3];
var arr2 = [4, 5, 6];
Array.prototype.push.apply(arr1, arr2);
console.log(arr1); // [1, 2, 3, 4, 5, 6]
```
3. splice
```javascript
var arr1 = [1, 2, 3, 6];
var arr2 = [4, 5];

Array.prototype.splice.apply(arr1, [3, 0].concat(arr2));

// 같은 표현
arr1.splice(3, 0, ...arr2); // arr1.splice(3, 0, 4, 5);와 같다.

console.log(arr1); // [1, 2, 3, 4, 5, 6]
```
4. copy
```javascript
var arr = [1, 2, 3];
var copy = arr.slice();
console.log(copy); // [1, 2, 3]

// copy 변경
copy.push(4);
console.log(copy); // [1, 2, 3, 4]
// arr은 변경되지 않음
console.log(arr); // [1, 2, 3]
```

```javascript
const arr = [1, 2, 3];
const copy = [...arr];
console.log(copy); // [1, 2, 3]

// copy 변경
copy.push(4);
console.log(copy); // [1, 2, 3, 4]
// arr은 변경되지 않음
console.log(arr); // [1, 2, 3]
```
- 객체에서 사용하는 경우
- - Spread 연산자를 사용하여 객체를 손쉽게 병합 또는 변경 가능
- - Object.assign 메소드를 사용하여 동일하게 작업 가능
```javascript
const merged = Object.assign({}, {x: 1, y: 2}, {g: 10, z: 3});
console.log(merged); // {x: 1, y: 10, z: 3}
```
- - Spread 연산자를 사용하면 유사 배열 객체를 배열로 손쉽게 변환 가능
```javascript
const htmlCollection = document.getElementsByTagName('li');
// 유사 배열인 HTMLCOLLECTION을 배열로 변환한다.
const newArray = [...htmlCollection]; // Spread 연산자
// ES6의 Array.from 메소드를 사용할 수도 있다.
const newArray = Array.from(htmlCollection);
```

## 자바스크립트 타입 + (타입스크립트 타입)
|타입|JS|TS|설명|
|---|--|--|--|
|boolean|O|O|true와 false|
|null|O|O|값이 없다는 것을 병시|
|undefined|O|O|값을 할당하지 않은 변수의 초기값|
|number|O|O|숫자(정수와 실수, infinity, NaN|
|string|O|O|문자열|
|symbol|O|O|고유하고 수정 불가능한 데이터 타입이며 주로 객체 프로퍼티이 식별자로 사용(ES6)|
|object|O|O|객체형(참조형)|
|array||O|배열|
|tuple||O|고정된 요소 수만큼의 자료형을 미리 선언 후 배열을 표현|
|enum||O|열거형, 숫자 값 집합에 이름을 지정한 것|
|any||O|타입 추론할 수 없거나 타입 체크가 필요 없는 변수에 사용, var 키워드로 선언한 변수와 같이 어떤 타입의 값이라도 할당 가능|
|void||O|일반적으로 함수에서 반환값이 없을 때 사용|
|never||O|결코 발생하지 않는 값|
___

## 배열 map, forEach등 새로운 배열 변환하는 아이들/ 아닌 것
- 새로운 배열 변환
  1. splice
  ```
  d // [2, 4, 6, 8]
  const p = d.splice(0,2);
  p // [2, 4]
  d // [6, 8]
  ```
  
  ```
  a = [1, 2, 3];
  a.splice(a.indexOf(2), 1);
  a // [1, 3]
  ```
  
- 그대로 유지
  1. filter
  ```
  const a = [1, 2, 3, 4];
  const b = a.filter(x=>x>2)
  a // [1, 2, 3, 4]
  b // [3, 4]
  ```
  2. concat
  ```
  const a = [1,2,3];
  const b = [4,5,6];
  const c = a.concat(b);
  c // [1, 2, 3, 4, 5, 6]
  a // [1, 2, 3]
  ```
  3. slice
  ```
  const c = a.slice(0,3)
  c // [1, 2, 3]
  a // [1, 2, 3, 4]
  ```
  
  4. map
  ```
  a // [1, 2, 3, 4]
  const d = a.map(x=>x*2)
  d // [2, 4, 6, 8]
  a // [1, 2, 3, 4]
  ```
  - array => json array
  ```
  const a = [1,2,3,4];
  const b = a.map(x => {return {value: x}});
  /*
  0: {value: 1}
  1: {value: 2}
  2: {value: 3}
  3: {value: 4}
  */
  ```
  
- 참조 
  1. [[Javascript] Set 객체를 배열(Array)로 변환하는 3가지 방법](https://hianna.tistory.com/421)

### Symbol
- Symbols 는 'new' 키워드를 사용하지 못함
- Symbol은 
[Symbol은 왜 쓰는가](https://medium.com/@hyunwoojo/javascript-symbol-%EC%97%90-%EB%8C%80%ED%95%B4%EC%84%9C-6aa5903fb6f1)

### tuple
- 고정된 요소 수만큼의 타입을 미리 선언 후 배열을 표현
```javascript
let tuple: [string, number];
tuple = ['hello', 10];
```

### enum
- 열거형은 숫자 값 집합에 값 집합에 이름을 지정한 것
```javascript
enum Color1 {Red, Green, Blue};
```

### void
- 함수에서 반환값이 없을 때 사용
```javascript
function warnUser(): void{
  console.log("This is my warning message");
}
```

### never
- 결코 발생하지 않는 값
```javascript
function infiniteLoop(): never {
  while (true) {}
}
```

### string vs String
- string: 기본 자료형 문자열 타입
- String: String 생성자 함수로 생성된 String 래퍼 객체 타입
```javascript
let primiteveStr: string;
primiteveStr = 'hello'; // Correct
primiteveStr = new String('hello'); // Incorrect
```
```javascript
let objectStr: String;
objectStr = 'hello'; // Correct
objectStr = new String('hello'); // Correct
```

### 암호화 복호화
```
window.btoa(''); // 암호화
window.atob(''); // 
```

### 객체 생성시 key값이 variable인 경우
```
const parmKey = Object.keys(paramObj)[0];
const reqBody = {
  params: { [parmKey] : paramObj[parmKey]}
  // 예제 params: { blNo : 'ALL'}
  // blNo이나 cntrNo나 po라는 key값이 올 수 있으므로 [parmKey]로 
}
```

### Object 중 해당하는 property가 존재하는지 안하는지 검색
```
.hasOwnProperty
```
___

## export default
- 단일 값을 내보내거나 모듈의 기본 값이 필요한 경우, 기본 내보내기를 사용한다.
```javascript
let cube = function cube(x) {
  return x * x * x;
};
export default cube;
```
- 같은 표현
```javascript
export default function (x) {
  return x * x * x;
};
```

## for await of
- [for await...of](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/for-await...of)
```
async function* asyncGenerator() {
  let i = 0;
  while (i < 3) {
    yield i++;
  }
}

(async function() {
  for await (let num of asyncGenerator()) {
    console.log(num);
  }
})();
// 0
// 1
// 2
```

## window.open() 도메인 다른 경우
[window.opener에 권한 문제로 접근할 수 없는 경우 해결방법](https://noritersand.github.io/javascript/javascript-window.opener%EC%97%90-%EA%B6%8C%ED%95%9C-%EB%AC%B8%EC%A0%9C%EB%A1%9C-%EC%A0%91%EA%B7%BC%ED%95%A0-%EC%88%98-%EC%97%86%EB%8A%94-%EA%B2%BD%EC%9A%B0-%ED%95%B4%EA%B2%B0%EB%B0%A9%EB%B2%95/)
- 로그인 새창열기
```
openLogin() {
    window.open('https://local.test.com:4222/login', 'name', 'width=410, height=700, resizable=0, scrollbars=no, status=0, titlebar=0, toolbar=0, left=300, top=200');
   }
```

## garbage collector
- [javascript ](https://developer.mozilla.org/ko/docs/Web/JavaScript/Memory_Management)

## bfcache
- 이슈 : submit 날리는 페이지에서 뒤로가기 했을 경우 브라우저 캐싱이 되어 input에 값은 표기되지만 실질적으로 값매핑은 안된 케이스
- 참조 : [Back Forward Cache(bfcache) 해결(?)한 이야기(https://dev-t-blog.tistory.com/9)
```
window.onpageshow = (event) => {
      if ( event.persisted || (window.performance && window.performance.navigation.type == 2)) {
        this.loginForm.reset();
      }
    }
```

### 일시적 사각 지대 (Temporal Dead Zone; TDZ)
- var 변수의 경우 선언 단계 - 초기화 가 동시에 이루어지는 반면, let/const 변수의 경우 선언 단계와 초기화 단계가 나누어서 이루어짐
- let/const 변수의 선언 단계와 초기화 단계 사이를 일시적 사각 지대 (Temporal Dead Zone; TDZ)라고 부름
- 실제 코드에서 let 변수의 선언 또는 const 변수의 선언 및 할당 (const 의 경우 선언과 동시에 값 할당이 되어야 함)이 나오기 전까지는 해당 변수는 TDZ에서 관리 한다고 생각하면 됨
- 해당 코드가 나오기 전에 미리 사용을 하려고 할 경우 TDZ에서 ReferenceError를 발생 시킴

### HTML 특수기호 변환
```javascript
const unescape = str => str.replace(/&/g , '&').replace(/&lt;/g  , '<').replace(/&gt;/g  , '>').replace(/&#0*39;/g , "'").replace(/&quot;/g, '"');
```

### eventListener
- [Event Binding Mechanism in Angular](https://blog.bitsrc.io/event-binding-mechanism-in-angular-b38f0e46d2ed)

### Debounce Throttle
- [디바운스(Debounce)와 스로틀(Throttle ) 그리고 차이점](https://webclub.tistory.com/607)

### Navigator - geolocation
- [Navigator - geolocation](https://developer.mozilla.org/ko/docs/Web/API/Navigator/geolocation)
- 

### [#JvaScript #ES12](https://levelup.gitconnected.com/top-5-javascript-es12-features-you-should-start-using-now-b16a8b5353b1)
- Top 5 JavaScript ES12 Features You Should Start Using Now
- 지금 사용하기 시작해야 하는 JavaScript ES12 기능

### 드래그 특정영역 활성화
- css에 작업
```
// 드래그 방지
-webkit-user-drag: none;
-webkit-user-select: none;
-moz-user-select: none;
-ms-user-select: none;
user-select: none;
// 드래그 활성화
-webkit-user-select: all;
-moz-user-select: all;
-ms-user-select: all;
user-select: all;
```


### [브라우저 닫기 새로고침 이벤트 리스너](https://taewooblog.tistory.com/m/75) - 둘의 독립 처리는 어려움..
### 출처
1. [[Javascript ] 프로토타입 이해하기](https://medium.com/@bluesh55/javascript-prototype-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-f8e67c286b67)
2. [출처 poiemaweb](https://poiemaweb.com/js-prototype)
3. [화살표 함수](https://ko.javascript.info/arrow-functions)
4. [[Javascript] Symbol 에 대해서](https://medium.com/@hyunwoojo/javascript-symbol-%EC%97%90-%EB%8C%80%ED%95%B4%EC%84%9C-6aa5903fb6f1)
