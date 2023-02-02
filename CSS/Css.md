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
- 자식 선택자 : ul > .orange {
- 하위 선택자 : div .orange { // 띄어쓰기도 선택자의 기호!!!
- 인접 형제 선택자 : .orange + li // + 다음 형제 요소 하나
- 일반 형제 선택자 : .orange ~ li // ~ 다음 형제 요소 모두 선택

# 선택자 가상 클래스
1. :focus / :active / :hover
2. 
    - .className div:first-child
    - .className div:last-child
    - .className *:not(span) // 부정 선택자
    - .className *:nth-child(2n) // 짝수, 괄호 안에 변수로 다양하게 선택 가능
    - .className *:nth-child(2n+1) // 홀수

# 가상 요소 선택자
1. .className::before 
```
// 선택자 요소의 내부 앞에 내용(content)을 삽입
.box:before {
    content: "앞!"
}
```
3. 
