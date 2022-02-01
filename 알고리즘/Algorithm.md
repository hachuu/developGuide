# 알고리즘

* 어떠한 문제를 해결하기 위해 정해진 일련의 절차나 방법을 공식화한 형태로 표현한 것.

## 동치 비교
[동치 비교 및 동일성](https://developer.mozilla.org/ko/docs/Web/JavaScript/Equality_comparisons_and_sameness)
- == 의 경우 null == undefined -> true

## Sort 개념

1. Quck Sort [퀵 정렬](https://gmlwjd9405.github.io/2018/05/10/algorithm-quick-sort.html)
2. Bubble Sort [버블 정렬](https://gmlwjd9405.github.io/2018/05/06/algorithm-bubble-sort.html)
3. Merge Sort [합병 정렬](https://gmlwjd9405.github.io/2018/05/08/algorithm-merge-sort.html)
4. Shell Sort [셸 정렬](https://gmlwjd9405.github.io/2018/05/08/algorithm-shell-sort.html)
5. Heap Sort [힙 정렬](https://gmlwjd9405.github.io/2018/05/10/algorithm-heap-sort.html)
   - [힙이란?](https://gmlwjd9405.github.io/2018/05/10/data-structure-heap.html)
6. Selection Sort [선택 정렬](https://gmlwjd9405.github.io/2018/05/06/algorithm-selection-sort.html)
7. Insertion Sort [삽입 정렬](https://gmlwjd9405.github.io/2018/05/06/algorithm-insertion-sort.html)

## 2진수, 10진수 변경, 16진수 변경
1. 10진수 => 2진수
- 예제
```javascript
const example = 1234;
example.toString(2);
```

2. 2진수 => 10진수
- 예제
```javascript
const example = '10010';
parseInt(example, 2);
```

3. 2진수 => 16진수
- 예제
```javascript
const example = '10010';
parseInt(example, 2);
parseInt(example, 2).toString(16);
```

## 최소공약수, 최대공배수
1. 최소공배수 =  n * m / 최대공약수;
2. 최대공약수
```javascript
function getMin(min, max) {
    if (min % max === 0) {
        return max;
    } else {
        return getMin(max, min%max);
    }
}
```
3. 배열의 최대공약수
```javascript
function nlcm(arr) {
 return arr.reduce((min, max) => min*max / gcd(min, max))  
}

function gcd(min, max) {
  return min % max ? gcd(max, min%max) : max
}
```

## 아스키 코드, 문자열 코드 character변환
- 'a'.charCodeAt: 문자열 코드를 아스키코드로 표현.
- String.fromCharCode(): 유니코드 또는 아스키 코드 번호를, 문자열 코드로 표현.

```javascript
'a'.charCodeAt(0); //97;
String.fromCharCode(97) //a;
String.fromCharCode(x.charCodeAt(0) + n);
```

## 형변환 string, number
- Number to String
   - +""; => String으로 변환
- String to Number
   - +"10"; => Number로 변환
```javascript
10+""; //"10"
+"10"; //10 string값에+를 붙여준다.
```

## 배열 apply를 활용한 Max, Min 값 구하기
```javascript
var numbers = [10, 20, 3, 16, 45];
var max = Math.max.apply(null, numbers);
var min = Math.min.apply(null, numbers);
console.log(max, min); //45 3
```

## 제곱근
```javascript
Math.sqrt(121) => 11
Math.pow(3, 2)=> 9
```

## 올림, 버림, 반올림
```javascript
Math.ceil() => 올림
Math.floor() => 버림
Math.round() => 반올림
```

## 중복 제거
- Set 객체는 자료형에 관계 없이 원시 값과 객체 참조 모두 유일한 값을 저장할 수 있다.
```javascript
const a = [1, 2, 3, 4, 3, 5, 6, 4];
const b = [...new Set(a)];
console.log(b); // [1, 2, 3, 4, 5, 6]
```

## 스택 큐 
- 큐: push와 shift
- 스택: push와 pop

- push와 pop
   1. push: 메서드는 배열의 끝에 하나 이상의 요소를 추가하고, 배열의 새로운 길이를 반환
   2. pop: 메서드는 배열에서 마지막 요소를 제거하고 그 요소를 반환
- shift와 unshift
   - 메서드는 pop과 push에 비해 많이 느림
   1. shift : pop 메서드와 비슷하며, 배열의 마지막 요소 대신 0번째 요소를 제거하고 반환
   2. unshift: 메서드는 새로운 요소를 배열의 맨 앞쪽에 추가하고, 새로운 길이를 반환

## length만 아는 array 생성하기
```
const testArr = Array.from({length: 5}, (x, i) => i+1);
//  [1, 2, 3, 4, 5]
```
