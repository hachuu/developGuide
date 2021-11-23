- "buildOptimizer": false,
- "optimization": false,
  - 스크립트/스타일 파일을 압축할 것인지
  - 트리 셰이킹 할 것인지
  - 데드 코드를 제거할 것인지
  - 주요 CSS 파일을 인라인으로 변환할 것인지
  - 폰트를 인라인으로 포함할 것인지
  - 스타일 최적화 옵션을 true로 설정하고 Angular Universal을 함께 활용하면 HTML 페이지를 렌더링하기 위해 필요한 코드의 양을 줄일 수 있습니다.

|옵션   |설명                                     |타입   |기본값|
|-------|----------------------------------------|-------|------|
|scripts|스크립트 파일을 최적화할 것인지 지정합니다.	|boolean|true|
|styles|스타일 파일을 최적화할 것인지 지정합니다.	|boolean \| 스타일 최적화 옵션|true|
|fonts|폰트를 최적화할 것인지 지정합니다.참고: 인터넷 연결이 필요합니다.|boolean \| 폰트 최적화 옵션|true|

```
"optimization": {
  "scripts": true,
  "styles": {
    "minify": true,
    "inlineCritical": true
  },
  "fonts": true
}
```
- "vendorChunk": true,
```
vendorChunk true : 타사 라이브러리를 많이 변경하지 않고 클라이언트 코드를 자주 업데이트할 계획입니다.
vendorChunk false : 번들 크기가 크게 줄어듭니다. 또는 클라이언트 코드를 자주 변경하지 않을 것입니다.
```
- "extractLicenses": false,
- "sourceMap": true,

|옵션   |설명                                     |타입   |기본값|
|-------|----------------------------------------|-------|------|
|scripts|모든 스크립트 파일마다 소스맵을 생성합니다.|boolean|true|
|styles|모든 스타일 파일마다 소스맵을 생성합니다.|boolean|true|
|vendor|서드 파티 패키지용 소스맵을 생성합니다.|boolean|false|
|hidden|에러 확인툴 용으로 활용하는 소스맵을 생성합니다.|boolean|false|

```
"sourceMap": {
  "scripts": true,
  "styles": false,
  "hidden": true,
  "vendor": true
}
```

- "namedChunks": true,
- "budgets"
  - 빌드 결과물 용량 제한하기

|프로퍼티 |값                                                             |
|--------|--------------------------------------------------------------|
|type|용량을 제한하는 방식을 지정하며, 다음 항목 중 하나를 사용합니다. <br> bundle - 특정 번들 파일을 기준으로 합니다. <br>initial - 애플리케이션이 처음 실행될 때 필요한 용량을 기준으로 합니다. 기본 설정에서 500kb를 넘으면 경고 메시지가 출력되며 1mb를 넘으면 에러 메시지가 출력됩니다. <br>allScript - 스크립트 파일 전체를 기준으로 합니다. <br>all - 애플리케이션 전체 용량을 기준으로 합니다. <br>anyComponentStyle - 컴포넌트 스타일시트 파일 하나를 기준으로 합니다. 기본 설정에서 2kb를 넘으면 경고 메시지가 출력되며 4kb를 넘으면 에러 메시지가 출력됩니다. <br>anyScript - 개별 스크립트 파일을 기준으로 합니다. <br>any - 개별 파일을 기준으로 합니다.|
|name|번들 파일의 이름을 지정합니다. (`type=bundle`일 때 사용합니다.)|
|baseline|기준값으로 사용할 용량을 지정합니다.|
|maximumWarning|기준값보다 이 용량 이상으로 크면 경고 메시지를 출력합니다.|
|maximumError|기준값보다 이 용량 이상으로 크면 에러 메시지를 표시합니다.|
|minimumWarning|기준값보다 이 용량 이상으로 작으면 경고 메시지를 표시합니다.|
|minimumError|기준값보다 이 용량 이상으로 작으면 에러 메시지를 표시합니다.|
|warning|기준값보다 이 용량 이상으로 작거나 크면 경고 메시지를 표시합니다.|
|error|기준값보다 이 용량 이상으로 작거나 크면 에러 메시지를 표시합니다.|


```
"budgets": [
  {
    "type": "initial",
    "maximumWarning": "4mb",
    "maximumError": "5mb"
  },
  {
    "type": "anyComponentStyle",
    "maximumWarning": "4mb",
    "maximumError": "5mb"
  }
],
```
- "fileReplacements"
  - 빌드 환경에 맞게 환경설정 파일 교체 (컴파일 시점에 기본 옵션을 대체할 파일을 지정)
  - live 빌드하는 경우 : ng build --configuration production / test 빌드하는 경우 : ng build --configuration development
```
"fileReplacements": [
  {
    "replace": "src/environments/environment.ts",
    "with": "src/environments/environment.prod.ts"
  }
],
```
"outputHashing": "all"
