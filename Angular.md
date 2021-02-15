# Router
- routerLink vs href
- href: 서버로 페이지 요청이 이뤄짐
- routerLink: 자신의 값을 라우터에 전달, 해당 컴포넌트를 활성화, 뷰 출력

# 속도 최적화
- [Angular 앱 성능 최적화를 위한 14가지 방법](https://dev.grapecity.co.kr/bbs/board.php?bo_table=Insight&wr_id=2&sca=IT%EF%BC%86%EA%B0%9C%EB%B0%9C+%EC%A0%95%EB%B3%B4&page=1)

# SEO문제
- 서버 사이드 랜더링을 지원하는 SEO 대응 기술이 이미 존재 -> [angular universal](#angular-universal)
- [universal.interceptor.ts](https://gist.github.com/UserGalileo/1c1241ed150cc86f309bef92a1811eea)
- [Angular Server Side Rendering State Transfer For HTTP Requests](https://hackernoon.com/angular-server-side-rendering-state-transfer-for-http-requests-wu263t3h)
- [Angular Universal + Caching (TransferState)](https://itnext.io/angular-universal-caching-transferstate-96eaaa386198)

# 모듈
- 모듈 분리
- 기능 모듈: 특정 화면을 구성하는 구성요소
- 공유 모듈: 애플리케이션 전역에서 사용하는 컴포넌크, 디렉티브, 파이프 등
- 핵심 모듈: 애플리케이션 전역에서 사용하는 데이터 서비스, 인증 서비스, 인증 가드 등
- module provider 등록하는 경우 service의 Injdectable의 providedIn 메타데이터 삭제 (모듈에 등록된 서비스가 많은 경우 모듈의 프로바이더에서 서비스를 관리하는 것이 유리)
- [angular module(component 및 module 만들기)](https://kamang-it.tistory.com/entry/Angular-08angular-modulecomponent-%EB%B0%8F-module-%EB%A7%8C%EB%93%A4%EA%B8%B0)

# 양방향 바인딩

```html
<counter [count]="value" (countChange)="value=$event"></counter>
```

# Form

## FormControl 클래스와 formControlName

```html
<form [formGroup]="userForm" novalidate>
  <div>
    <input type="text" formControlName="userid" placeholder="user id">
  </div>
  <div formGroupName="passwordGroup">
    <div>
      <input type="password" formControlName="password" placeholder="password">
    </div>
    <div>
      <input type="password" formControlName="confirmPassword" placeholder="confirmpassword">
    </div>
  </div>
</form>
```

```typescript
ngOnInit() {
  this.userForm = new FormGroup({
    userid: new FormControl(''),
    passwordGroup: new FormGroup({
      password: new FormControl(''),
      confirmPassword: new FormControl('')
    })
  })
}
```

## 리액티브 폼
- 컴포넌트 클래스에서 폼 요소의 값 및 유효성 검증 상태를 관리하는 자바스크립트 객체인 폼 모델(FormGroup, FormControl, FormArray)을 직접 정의/생성
- form* 접두사가 붙은 디렉티브(formGroup, formGroupName, formControlName, formArrayName)를 사용하여 템플릿의 폼 요소와 컴포넌트 클래스의 폼 모델을 프로퍼티 바인딩으로 연결

## FormBuilder
- 더 간편한 방법으로 리액티브 폼을 구성
```typescript

  passwordGroup: new FormGroup({
    password: new FormControl('', Validators.required),
    confirmPassword: new FormControl('', Validators.required)
  }, PasswordValidator.match),

```

```typescript

  passwordGroup: this.fb.group({
    password: ['', Validators.required],
    confirmPassword: ['', Validators.required]
  }, { validator: PasswordValidator.match }),

```

## 빌트인 구조 디렉티브
- ngFor
 1. index 이외에도 first, last, even, odd도 가능
 2. trackBy 제공: 퍼포먼스를 향상하기 위해
```html
<li *ngFor="let user of users; let i=index; trackBy: trackByUserId">
 {{i}}: {{user.name}}
 <button (click)="removeUser(user.id)">X</button>
</li>
```
```typescript
trackByUserId(index: number, user: User) {
 // user.id를 기준으로 변경을 트래킹한다.
 return user.id;
}
```

## angular universal
- Angular에서 SSR을 사용하는 방법
- Angular Universal is a toolkit that allows us to do server-side rendering (SSR) and pre-rendering for our Angular applications.
1. Improve Search Engine Optimization (SEO)
2. Show the first page quickly
3. Improve performance for low-powered devices

- 빌드 방법
  - npm run dev:ssr

- 서버 구동
  - npm run serve:ssr 또는 dist> node server
  - [실습예제](https://ksrae.github.io//angular/angular-universal/)
  - [바닐라 Node.js를 사용한 Angular SSR](https://dev.to/igorfilippov3/angular-ssr-with-vanilla-node-js-15pj)
  - [Angular universal 실전 상](https://m.blog.naver.com/kitepc/221380895021)
  - [Angular universal 실전 하](https://m.blog.naver.com/kitepc/221380916242)
  
## Observable, BehaviorSubject 차이
  - [Angular Observable과 BehaviorSubject로 구독, 갱신하기](https://blog.eunsatio.io/develop/Angular-Observable%EA%B3%BC-BehaviorSubject%EB%A1%9C-%EA%B5%AC%EB%8F%85,-%EA%B0%B1%EC%8B%A0%ED%95%98%EA%B8%B0)
  
## declare: 외부 라이브러리 사용하기 
  - [외부 라이브러리 사용하기 (카카오예시)](https://rottk.tistory.com/entry/Angular-%EC%99%B8%EB%B6%80-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)
  
## google map api
- 출처: [angular + google map](https://velog.io/@noyo0123/angular-google-map)

## angular mouseover mouseleave
- 출처: [How to use mouseover and mouseout in Angular 6](https://stackoverflow.com/questions/51491225/how-to-use-mouseover-and-mouseout-in-angular-6)

## eventListener
- [Event Binding Mechanism in Angular](https://blog.bitsrc.io/event-binding-mechanism-in-angular-b38f0e46d2ed)
- [angular eventManager](https://angular.io/api/platform-browser/EventManager)
- [hostlistener](https://angular.io/api/core/HostListener)
