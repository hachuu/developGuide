# 알고리즘

* 어떠한 문제를 해결하기 위해 정해진 일련의 절차나 방법을 공식화한 형태로 표현한 것.



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

## 아스키 코드, 문자열 코드 character변환
- 'a'.charCodeAt: 문자열 코드를 아스키코드로 표현.
- String.fromCharCode(): 유니코드 또는 아스키 코드 번호를, 문자열 코드로 표현.

```javascript
'a'.charCodeAt(0); //97;
String.fromCharCode(97) //a;
String.fromCharCode(x.charCodeAt(0) + n);
```
