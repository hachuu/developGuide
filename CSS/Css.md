# reference
- [css참고](https://poiemaweb.com/css3-syntax)
- [position](https://creamilk88.tistory.com/197)
- [css mozila](https://developer.mozilla.org/en-US/docs/Web/CSS/gradient/linear-gradient)

# css에서 link a tag 밑줄 지우기
```
    a:link {
      color: black;
    }
    a {
      text-decoration: none;
      text-decoration-line: none;
    }
    a:visited {
      color: black;
    }
```

# Image sprite 반응형
- background-position의 값을 %로 계산

# 기본 선택자
- *
- .
- #
- 타입 선택자 : div
- 속성 선택자 : input[type="text"]

# 복합 선택자
- 태그 선택자 : span.orange
- 자식 선택자 : ul > .orange 
