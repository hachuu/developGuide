# Router
- routerLink vs href
- href: 서버로 페이지 요청이 이뤄짐
- routerLink: 자신의 값을 라우터에 전달, 해당 컴포넌트를 활성화, 뷰 출력

# SEO문제
- 서버 사이드 랜더링을 지원하는 SEO 대응 기술이 이미 존재

# 모듈
- 모듈 분리
- 기능 모듈: 특정 화면을 구성하는 구성요소
- 공유 모듈: 애플리케이션 전역에서 사용하는 컴포넌크, 디렉티브, 파이프 등
- 핵심 모듈: 애플리케이션 전역에서 사용하는 데이터 서비스, 인증 서비스, 인증 가드 등
- module provider 등록하는 경우 service의 Injdectable의 providedIn 메타데이터 삭제 (모듈에 등록된 서비스가 많은 경우 모듈의 프로바이더에서 서비스를 관리하는 것이 유리)

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

