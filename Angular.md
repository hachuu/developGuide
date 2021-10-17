# angular cli project 생성
ng new my-project
cd my-project
ng serve --open

# angular component 생성
ng g c new-component => Error: More than one module matches. Use skip-import option to skip importing the component into the closest module에러가 나는 경우

ng g c new-component --module app => 실행하는 경우 app.module.ts에 자동 component import가 된다.

# HttpClient async/await화
- [Angular HttpClient의 프로미스화, 그리고 HttpInterceptor](https://blog.eunsatio.io/develop/Angular-HttpClient%EC%9D%98-%ED%94%84%EB%A1%9C%EB%AF%B8%EC%8A%A4%ED%99%94,-%EA%B7%B8%EB%A6%AC%EA%B3%A0-HttpInterceptor)

# Router
- routerLink vs href
  - href: 서버로 페이지 요청이 이뤄짐
    ```
    Window.open()
    ```
  - routerLink: 자신의 값을 라우터에 전달, 해당 컴포넌트를 활성화, 뷰 출력
  - * a태그 상위에 (click) event가 있는 경우 href 이동이 되지 않으므로 click event에 function으로 이동할 수 있도록 작업한다.
  - [URL을 통해 GET 통신으로 특정 페이지화면으로 접근하면 404 에러가 발생](https://jamong-icetea.tistory.com/214)
- [external url redirection](https://stackoverflow.com/questions/40150393/how-to-redirect-to-an-external-url-from-angular2-route-without-using-component/40421975)
- hook
  1. canActivate: canActivate 메서드를 구현하여 Route 이동시 먼저 체크하는 guard 기능
  2. canDeactivate: 페이지를 떠나는 경우 활성화되는 method
- 
# 속도 최적화
- [Angular 앱 성능 최적화를 위한 14가지 방법](https://dev.grapecity.co.kr/bbs/board.php?bo_table=Insight&wr_id=2&sca=IT%EF%BC%86%EA%B0%9C%EB%B0%9C+%EC%A0%95%EB%B3%B4&page=1)

# SEO문제
- 서버 사이드 랜더링을 지원하는 SEO 대응 기술이 이미 존재 -> [angular universal](#angular-universal)
- [universal.interceptor.ts](https://gist.github.com/UserGalileo/1c1241ed150cc86f309bef92a1811eea)
- [Angular Server Side Rendering State Transfer For HTTP Requests](https://hackernoon.com/angular-server-side-rendering-state-transfer-for-http-requests-wu263t3h)
- [Angular Universal + Caching (TransferState)](https://itnext.io/angular-universal-caching-transferstate-96eaaa386198)
- [angular - can't run rxjs interval with angular universal](https://stackoverflow.com/questions/55370609/angular-cant-run-rxjs-interval-with-angular-universal)

# 모듈
- 모듈 분리
- 기능 모듈: 특정 화면을 구성하는 구성요소
- 공유 모듈: 애플리케이션 전역에서 사용하는 컴포넌크, 디렉티브, 파이프 등
- 핵심 모듈: 애플리케이션 전역에서 사용하는 데이터 서비스, 인증 서비스, 인증 가드 등
- module provider 등록하는 경우 service의 Injdectable의 providedIn 메타데이터 삭제 (모듈에 등록된 서비스가 많은 경우 모듈의 프로바이더에서 서비스를 관리하는 것이 유리)
- [angular module(component 및 module 만들기)](https://kamang-it.tistory.com/entry/Angular-08angular-modulecomponent-%EB%B0%8F-module-%EB%A7%8C%EB%93%A4%EA%B8%B0)

# Form
  - FormControl
  - FormGroup
  - (ngSubmit)

1. FormControl 클래스와 formControlName

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

2. 리액티브 폼
- 컴포넌트 클래스에서 폼 요소의 값 및 유효성 검증 상태를 관리하는 자바스크립트 객체인 폼 모델(FormGroup, FormControl, FormArray)을 직접 정의/생성
- form* 접두사가 붙은 디렉티브(formGroup, formGroupName, formControlName, formArrayName)를 사용하여 템플릿의 폼 요소와 컴포넌트 클래스의 폼 모델을 프로퍼티 바인딩으로 연결

3. FormBuilder
- 더 간편한 방법으로 리액티브 폼을 구성 (객체 공장 개념)
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

# 양방향 바인딩

```html
<counter [count]="value" (countChange)="value=$event"></counter>
```

# Ag-grid
- [guide 문서](https://www.ag-grid.com/documentation/angular/status-bar/)

# Ag-map
- [guide 문서](https://angular-maps.com/api-docs/agm-core/components/agmmap#zoom)



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
- [Angular RU Universal Starter](https://github.com/Angular-RU/universal-starter)
  
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
- [click event is not working in innerhtml string angular 6](https://stackoverflow.com/questions/58641615/click-event-is-not-working-in-innerhtml-string-angular-6)
```
public ngAfterViewInit() {
  // Solution for catching click events on anchors using querySelectorAll:
  this.anchors = this.elementRef.nativeElement.querySelectorAll('a');
  this.anchors.forEach((anchor: HTMLAnchorElement) => {
    anchor.addEventListener('click', this.handleAnchorClick)
  })
}
```
- 방법 찾음[click event is not working in innerhtml string angular 6](https://stackoverflow.com/questions/58641615/click-event-is-not-working-in-innerhtml-string-angular-6)
```
  constructor(
    ...
    private elementRef: ElementRef
  ) {
  }

  mouseOverFunc() {
    console.log('hello    ', e.fromElement.children[0].attributes.href.nodeValue); // To-do children 중에 a태그만 찾아서 추출하는 방법을 찾아보자
  }

  ngAfterViewChecked() {
    const aTags = this.elementRef.nativeElement.querySelectorAll('a');
    aTags.forEach((anchor: HTMLAnchorElement) => {
      anchor.addEventListener('mouseover', this.mouseOverFunc)
    })
  }
```

## 모듈 등록
- a router 사용 => RouterModule
- ngIf 사용 => CommonModule
- ngModel, ngForm 사용 => FormsModule
- FormGroup, FormControl 사용 => ReactiveFormsModule

## 내장 지시자
- ngNonBindable속성
- This is what {{ item }} 으로 화면에 출력
```
<div>
  <span>{{ item }}</span>
  <span ngNonBindable>This is what {{ item }}</span>
</div>
```

## selecbox binding ul li 만들어주기
- [Display form fields based on dropdown selection](https://www.xspdf.com/resolution/54748676.html)
- [Creating a Dynamic Select with Angular Forms](https://coryrylan.com/blog/creating-a-dynamic-select-with-angular-forms)
1. 상위 셀렉트 선택할 시 Li 태그를 추가로 넣어줘보기=> library사용
- directive사용 ngviewinit 할때 생성
2. ngif를 다시 걸어서 하위 데이터를 그릴 수 있도록 해보기

## jquery fadein
- [In Angular 2, is it possible to fadeIn / fadeout instead of [hidden='xxx]?](https://stackoverflow.com/questions/34422022/in-angular-2-is-it-possible-to-fadein-fadeout-instead-of-hidden-xxx/45838232)
```
import { trigger, state, transition, style, animate } from '@angular/animations';

@Component({
  selector: 'some-selector',
  templateUrl: 'my-template.html',
  animations: [
    trigger('visibilityChanged', [
      state('shown', style({ opacity: 1 })),
      state('hidden', style({ opacity: 0 })),
      transition('shown => hidden', animate('600ms')),
      transition('hidden => shown', animate('300ms')),
    ])
  ]
})
export class MyComponent {
  visiblityState = 'hidden';
  toggle() {
    if (this.visiblityState === 'hidden')
      this.visiblityState = 'shown';
    else
      this.visiblityState = 'hidden';
  }
}

```

## viewChild input value
```
@ViewChild('myname') input:ElementRef; 
this.input.nativeElement.value
```
- input debouncing 처리 (input valuechanged debouncing 작업) [출처](https://stackoverflow.com/questions/32051273/angular-and-debounce)
```
import { Subscription } from 'rxjs/internal/Subscription';
import 'rxjs/add/operator/debounceTime';

formCtrlSub: Subscription;

this.formCtrlSub = this.dtlAddressControl.valueChanges
      .debounceTime(500)
      .subscribe( value=>{
        console.log('delayed key press value',value);
    });
```

## 모든 페이지 열릴 경우 scrollTop
- scrollPositionRestoration: 'enabled'
```
@NgModule({
  imports: [RouterModule.forRoot(routes,{
    scrollPositionRestoration: 'enabled'
  })],
  exports: [RouterModule]
})
```

## remove element by renderer2

```
const childElements = this.el.nativeElement.children;
for (let child of childElements) {
  this.renderer.removeChild(this.el.nativeElement, child);
}
```
```
/**
 * Implement this callback to remove a child node from the host element's DOM.
 * @param parent The parent node.
 * @param oldChild The child node to remove.
 * @param isHostElement Optionally signal to the renderer whether this element is a host element
 * or not
 */
abstract removeChild(parent: any, oldChild: any, isHostElement?: boolean): void;
```

## download excel file as an API response
- [출처](https://stackoverflow.com/questions/58335807/how-to-download-an-excel-file-in-angular-8-as-an-api-response)
- Add header { responseType: 'blob'}
```
this.http.post<any>(apiEndpoint,request,{ responseType: 'blob'} )
```
```
downloadFile(data: Response) {
  const blob = new Blob([data], { type: 'application/octet-stream' });
  const url= window.URL.createObjectURL(blob);
  window.open(url);
}
```

## SPA 공통 사항
1. router이동시 이미 받아진 라이브러리는 다시 받지 않는다.
2. a 태그 or url 직접 입력해서 진입하는 경우 라이브러리를 다시 로드한다.
3. 브라우저 닫을 때 이벤트 감지 HostListener: beforeunload
```
@HostListener("window:beforeunload", ["$event"])
beforeUnloadHander(event: Event) {
}
```
4. 다른 페이지로 이동 이벤트 감지 => 브라우저 닫을 시에 ngOnDestroy는 태우지 않는다.
```
ngOnDestroy() {
}
```
5. SSR 처리 할 시 
```
this.router.navigate() // 문제
window.replace // 로 해결
```
## Infinite scroll
[Infinite Virtual Scroll with the Angular CDK](https://fireship.io/lessons/infinite-virtual-scroll-angular-cdk/)


## ngcc 에러..
- Angular 9 - NGCC fails with an unhandled exception
[Angular 9-처리되지 않은 예외로 NGCC가 실패합니다.](https://stackoverflow.com/questions/61222467/angular-9-ngcc-fails-with-an-unhandled-exception)

## angular 12 release
[angular12](https://blog.angular.io/angular-v12-is-now-available-32ed51fbfd49)

## Angular input ngmodel setcomma해서 보여주기
```
[ngModel]="value | setCommaPipe" (ngModelChange)="value = $event"
```

## IE Polyfills 문제 해결
```
npm i -S core-js@2.5.7
```
```
/**
 * This file includes polyfills needed by Angular and is loaded before the app.
 * You can add your own extra polyfills to this file.
 *
 * This file is divided into 2 sections:
 *   1. Browser polyfills. These are applied before loading ZoneJS and are sorted by browsers.
 *   2. Application imports. Files imported after ZoneJS that should be loaded before your main
 *      file.
 *
 * The current setup is for so-called "evergreen" browsers; the last versions of browsers that
 * automatically update themselves. This includes Safari >= 10, Chrome >= 55 (including Opera),
 * Edge >= 13 on the desktop, and iOS 10 and Chrome on mobile.
 *
 * Learn more in https://angular.io/docs/ts/latest/guide/browser-support.html
 */

/***************************************************************************************************
 * BROWSER POLYFILLS
 */

/** IE9, IE10 and IE11 requires all of the following polyfills. **/
import 'core-js/es6/symbol';
import 'core-js/es6/object';
import 'core-js/es6/function';
import 'core-js/es6/parse-int';
import 'core-js/es6/parse-float';
import 'core-js/es6/number';
import 'core-js/es6/math';
import 'core-js/es6/string';
import 'core-js/es6/date';
import 'core-js/es6/array';
import 'core-js/es6/regexp';
import 'core-js/es6/map';
import 'core-js/es6/weak-map';
import 'core-js/es6/set';
import 'core-js/fn/array/includes';

/** IE10 and IE11 requires the following for the Reflect API. */
import 'core-js/es6/reflect';


/** Evergreen browsers require these. **/
// Used for reflect-metadata in JIT. If you use AOT (and only Angular decorators), you can remove.



/**
 * Required to support Web Animations `@angular/platform-browser/animations`.
 * Needed for: All but Chrome, Firefox and Opera. http://caniuse.com/#feat=web-animation
 **/
/**
 * By default, zone.js will patch all possible macroTask and DomEvents
 * user can disable parts of macroTask/DomEvents patch by setting following flags
 */

 // (window as any).__Zone_disable_requestAnimationFrame = true; // disable patch requestAnimationFrame
 // (window as any).__Zone_disable_on_property = true; // disable patch onProperty such as onclick
 // (window as any).__zone_symbol__BLACK_LISTED_EVENTS = ['scroll', 'mousemove']; // disable patch specified eventNames

 /*
 * in IE/Edge developer tools, the addEventListener will also be wrapped by zone.js
 * with the following flag, it will bypass `zone.js` patch for IE/Edge
 */

/***************************************************************************************************
 * Zone JS is required by default for Angular itself.
 */
import 'zone.js/dist/zone';  // Included with Angular CLI.
import 'zone.js';


/***************************************************************************************************
 * APPLICATION IMPORTS
 */
```

### @Output childEvent not initialized 에러
```
import { EventEmitter } from 'events'; => 삭제
import { EventEmitter } from '@angular/core'; => 변경
```

### aggrid infinite scroll
[handleScroll method](https://github.com/ag-grid/ag-grid/issues/3089)


### object key string 변수로 가지고 오고 싶을때 에러나는 현상
```
getErrorMsg(errorCode: string) {
  const msg: ObjType = {
    'WRONG_USER': '비밀번호가 맞지 않습니다. 확인 후 다시 입력해 주세요.'
  }
  return msg[errorCode];
}
```
- 발생: return msg[errorCode]; 부분에서 Element implicitly has an 'any' type because expression of type 'string' can't be used to index type '{ WRONG_USER: string; }'.
  No index signature with a parameter of type 'string' was found on type '{ WRONG_USER: string; }'
- 원인: typescript에서 type을 지정해주지 않았기 때문에 발생한 문제

```
// typescript에서는 Object의 string key 타입 선언을 해줘야함
type ObjType = {
  [index: string]: string
}
```
```
// 수정된 method
getErrorMsg(errorCode: string) {
  type ObjType = {
    [index: string]: string
  }
  const msg: ObjType = {
    'WRONG_USER': '비밀번호가 맞지 않습니다. 확인 후 다시 입력해 주세요.'
    // '존재하지 않는 아이디 입니다.'
  }
  return msg[errorCode];
}
```

### file upload 공식 문서 확인하기
[angular-file-upload](https://blog.angular-university.io/angular-file-upload/)
[How to Post/Upload FormData (multipart/form-data) with Angular 10, TypeScript and HttpClient](https://www.techiediaries.com/angular-formdata/)
```
<form [formGroup] = "uploadForm" (ngSubmit)="onSubmit()">
  <input class="upload-name" value="파일선택">
  <label for="file">업로드</label> 
  <input type="file" id="file" 
  (change)="onFileSelected(fileUpload.files)"
  #fileUpload> 
</form>
```
```
@ViewChild('fileUpload', { static: false })
fileUpload!: ElementRef;

// formbuilder를 통한 form 생성 후 post 전달
this.uploadForm = this.formBuilder.group({
  corpReg: ['']
});

onFileSelected(files: any) {
  if (files && files[0]) {
    this.uploadForm.get('corpReg')?.setValue(files[0]);
    this.onSubmit();
  }
}
onSubmit() {
  const formData = new FormData();
  formData.append('corpRegFile', this.uploadForm.get('corpReg')?.value);
  formData.append('corpRegNo', '');
}
```

### file drop event
[hosteventlistener drop이벤트를 통한 작업](https://medium.com/@tarekabdelkhalek/how-to-create-a-drag-and-drop-file-uploading-in-angular-78d9eba0b854)

### pipe에 따른 form 값 변경 인지 로직
```
<form [formGroup]="myForm">
  <input 
    [value]="myForm.get('amount').value | udpCurrency"
    formControlName="amount" 
    placeholder="Amount">
</form>
```


