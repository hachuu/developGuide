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


### 출처
1. [[Javascript ] 프로토타입 이해하기](https://medium.com/@bluesh55/javascript-prototype-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-f8e67c286b67)
2. [출처 poiemaweb](https://poiemaweb.com/js-prototype)
