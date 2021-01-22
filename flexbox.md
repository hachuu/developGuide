
# FlexBox 개념 정리 - 출처: [Flexbox Froggy](https://flexboxfroggy.com/#ko)

## justify-content: inline 영역 위치 변경(가로 영역만)
- flex-start: 요소들을 컨테이너의 왼쪽으로 정렬합니다.
- flex-end: 요소들을 컨테이너의 오른쪽으로 정렬합니다.
- center: 요소들을 컨테이너의 가운데로 정렬합니다.
- space-between: 요소들 사이에 동일한 간격을 둡니다.
- space-around: 요소들 주위에 동일한 간격을 둡니다.

## align-items: block 영역 위치 변경(세로 포함)
- flex-start: 요소들을 컨테이너의 꼭대기로 정렬합니다.
- flex-end: 요소들을 컨테이너의 바닥으로 정렬합니다.
- center: 요소들을 컨테이너의 세로선 상의 가운데로 정렬합니다.
- baseline: 요소들을 컨테이너의 시작 위치에 정렬합니다.
- stretch: 요소들을 컨테이너에 맞도록 늘립니다.
### align-self
- 개별 요소에 적용할 수 있는 또 다른 속성입니다. 이 속성은 align-items가 사용하는 값들을 인자로 받으며, 그 값들은 지정한 요소에만 적용됩니다.
```css
#pond {
  display: flex;
  align-items: flex-start;
}

.yellow {
  align-self: flex-end;
}
```

## flex-direction: 정렬 순서 변경
- row: 요소들을 텍스트의 방향과 동일하게 정렬합니다.
- row-reverse: 요소들을 텍스트의 반대 방향으로 정렬합니다.
- column: 요소들을 위에서 아래로 정렬합니다.
- column-reverse: 요소들을 아래에서 위로 정렬합니다.

## order (상대 index로 표기, 현재 위치로 앞으로 표기하고 싶은 경우 음수값 사용)
- 때때로 컨테이너의 row나 column의 순서를 역으로 바꾸는 것만으로는 충분하지 않습니다. 이러한 경우에는 order 속성을 각 요소에 적용할 수 있습니다. order의 기본 값은 0이며, 양수나 음수로 바꿀 수 있습니다.
```css
.yellow {
  order: 2
}
```

## flex-wrap: 넓게하는 속성 (같은 줄에 표현할 것이냐 or 아니냐...)
- nowrap: 모든 요소들을 한 줄에 정렬합니다.
- wrap: 요소들을 여러 줄에 걸쳐 정렬합니다.
- wrap-reverse: 요소들을 여러 줄에 걸쳐 반대로 정렬합니다.

flex-direction과 flex-wrap이 자주 같이 사용되기 때문에, 

## flex-flow: flex-direction과 flex-wrap를 대신
- 이 속성은 공백문자를 이용하여 두 속성(flex-direction과 flex-wrap)의 값들을 인자로 받습니다.
- flex-flow: row wrap을 사용할 수 있습니다.
```css
#pond {
  display: flex;
  flex-flow: column wrap;
}
```

## align-content: 여러 줄 사이의 간격을 지정
- flex-start: 여러 줄들을 컨테이너의 꼭대기에 정렬합니다.
- flex-end: 여러 줄들을 컨테이너의 바닥에 정렬합니다.
- center: 여러 줄들을 세로선 상의 가운데에 정렬합니다.
- space-between: 여러 줄들 사이에 동일한 간격을 둡니다.
- space-around: 여러 줄들 주위에 동일한 간격을 둡니다.
- stretch: 여러 줄들을 컨테이너에 맞도록 늘립니다.
- align-content는 여러 줄들 사이의 간격을 지정하며, align-items는 컨테이너 안에서 어떻게 모든 요소들이 정렬하는지를 지정합니다. 한 줄만 있는 경우, align-content는 효과를 보이지 않습니다.

### froggy 24번 문제 answer
```css
flex-flow: column-reverse wrap-reverse;
justify-content: center;
align-content: space-between;
```
