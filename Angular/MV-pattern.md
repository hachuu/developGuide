# [MVVM modal in Angular](https://malcoded.com/posts/angular-2-components-and-mvvm/)

## Model / View / ViewModel

## Model 
- 정의: 개체의 구조를 정의하는 컨테이너
- plain-old javascript object
- 모델은 로직을 포함시키지 않음 (VM에서만 포함)

## View
- 정의: 애플리케이션의 시각적 계층을 의미
- 모든 시각적 요소 포함, 유저의 스크린을 담당
- Angular에서 template을 담당
- 구성: HTML + CSS
- 데이터 바인딩을 통해 VM과 연결된 template
- 템플릿은 component에 소속됨


## ViewModel
- 정의: View의 축약된 파트
- model을 managing하고 화면에 보여줄 속성을 정의함
- page에 필요한 로직 전체를 포함
- View와 ViewModel은 데이터 바인딩을 통해 연결됨
- VM에서 데이터 변경이 일어나며, 속성, 화면 들이 적용됨
- Angular에서는 component의 typescript로 속함


* component: building bblock of the application / designing, building하는 Angular의 필수적인 요소
- component의 구성 요소
  1. Template (View)
  2. Class (ViewModel)

- angular의 기본 component의 구성
  1. @Component({})
  2. 로직이 심어질 class이 해당
    - class는 정의된 로직과 같은 파일, 맨 아래에 위치함
    ```
    export class NavBar{
    }
    ```
- component는 혼자서 view에 적용될 수 없음
- 한 모듈에 무조건 기입이 되어 있어야만 사용이 가능
- 루트 모듈은 AppModule이며, 기입한 component를 사용하기 위해서는 부모 모듈의 declaration 섹션에 등록을 해야함


