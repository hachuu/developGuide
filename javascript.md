# javascript 개념 정리

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
- - ![img](https://github.com/hachuu/developGuide/blob/main/image/prototype%20Object.PNG)

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

## javascript Class
- ECMA6 표준에서는 Class 문법이 추가

- 오버라이딩(Overriding)
상위 클래스가 가지고 있는 메소드를 하위 클래스가 재정의하여 사용하는 방식이다.
- 오버로딩(Overloading)
매개변수의 타입 또는 갯수가 다른, 같은 이름의 메소드를 구현하고 매개변수에 의해 메소드를 구별하여 호출하는 방식이다. 자바스크립트는 오버로딩을 지원하지 않지만 arguments 객체를 사용하여 구현할 수는 있다.

- ㅍㅡㄹㅗㅌㅗㅌㅏㅇㅣㅂㄱㅗㅏㅇㅡㅣ ㅊㅏㅇㅣ
- 자식 클래스의 정적 메소드 내부에서도 super 키워드를 사용하여 부모 클래스의 정적 메소드를 호출할 수 있다. 이는 자식 클래스는 프로토타입 체인에 의해 부모 클래스의 정적 메소드를 참조할 수 있기 때문이다.

- 하지만 자식 클래스의 일반 메소드(프로토타입 메소드) 내부에서는 super 키워드를 사용하여 부모 클래스의 정적 메소드를 호출할 수 없다. 이는 자식 클래스의 인스턴스는 프로토타입 체인에 의해 부모 클래스의 정적 메소드를 참조할 수 없기 때문이다.


### 일시적 사각 지대 (Temporal Dead Zone; TDZ)
- var 변수의 경우 선언 단계 - 초기화 가 동시에 이루어지는 반면, let/const 변수의 경우 선언 단계와 초기화 단계가 나누어서 이루어짐
- let/const 변수의 선언 단계와 초기화 단계 사이를 일시적 사각 지대 (Temporal Dead Zone; TDZ)라고 부름
- 실제 코드에서 let 변수의 선언 또는 const 변수의 선언 및 할당 (const 의 경우 선언과 동시에 값 할당이 되어야 함)이 나오기 전까지는 해당 변수는 TDZ에서 관리 한다고 생각하면 됨
- 해당 코드가 나오기 전에 미리 사용을 하려고 할 경우 TDZ에서 ReferenceError를 발생 시킴


### 출처
1. [[Javascript ] 프로토타입 이해하기](https://medium.com/@bluesh55/javascript-prototype-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-f8e67c286b67)
2. [출처 poiemaweb](https://poiemaweb.com/js-prototype)
