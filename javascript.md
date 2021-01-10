# javascript 개념 정리

## ProtoType과 Instance
- Prototype : 객체를 만드는 기본 틀, 객체의 원형 속성과 기능(함수)이 들어있다.
- Instance : 프로토타입을 통해 새로 만들어진 객체. 객체의 속성과 함수를 사용할 수 있다.

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


## promise await 차이
- promise.then().catch()로 에러를 잡으면 되지만 await의 경우 try catch문으로 reject를 체크

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

## Symbol
- Symbols 는 'new' 키워드를 사용하지 못함
- Symbol은 
[Symbol은 왜 쓰는가](https://medium.com/@hyunwoojo/javascript-symbol-%EC%97%90-%EB%8C%80%ED%95%B4%EC%84%9C-6aa5903fb6f1)


## export default
- 단일 값을 내보내거나 모듈의 기본 값이 필요한 경우, 기본 내보내기를 사용한다.
```javascript
let cube = function cube(x) {
  return x * x * x;
};
export default cube;
```

### 일시적 사각 지대 (Temporal Dead Zone; TDZ)
- var 변수의 경우 선언 단계 - 초기화 가 동시에 이루어지는 반면, let/const 변수의 경우 선언 단계와 초기화 단계가 나누어서 이루어짐
- let/const 변수의 선언 단계와 초기화 단계 사이를 일시적 사각 지대 (Temporal Dead Zone; TDZ)라고 부름
- 실제 코드에서 let 변수의 선언 또는 const 변수의 선언 및 할당 (const 의 경우 선언과 동시에 값 할당이 되어야 함)이 나오기 전까지는 해당 변수는 TDZ에서 관리 한다고 생각하면 됨
- 해당 코드가 나오기 전에 미리 사용을 하려고 할 경우 TDZ에서 ReferenceError를 발생 시킴


### 출처
1. [[Javascript ] 프로토타입 이해하기](https://medium.com/@bluesh55/javascript-prototype-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-f8e67c286b67)
2. [출처 poiemaweb](https://poiemaweb.com/js-prototype)
3. [화살표 함수](https://ko.javascript.info/arrow-functions)
4. [[Javascript] Symbol 에 대해서](https://medium.com/@hyunwoojo/javascript-symbol-%EC%97%90-%EB%8C%80%ED%95%B4%EC%84%9C-6aa5903fb6f1)
