# 정규식 검사

[출처 https://poiemaweb.com/js-regexp](https://poiemaweb.com/js-regexp)
![img](https://github.com/hachuu/developGuide/blob/main/image/6F0B9C2C-65B6-4BA6-8E92-B85DB7DFDF6B.jpeg)

[자바스크립트 정규식 질문(괄호 문자 찾기)](https://okky.kr/article/428993)

- 세 자리 콤마찍기
```
num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
```
 
- 콤마 지우기
```
return num.replace(/,/g, "");
```
