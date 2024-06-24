1. 단독 컴포넌트
- [standalone: true](https://www.angular.kr/guide/standalone-components)
- 단독(standalone) 컴포넌트는 Angular 애플리케이션을 간단하게 구성하기 위해 도입되었습니다. 단독 컴포넌트, 단독 디렉티브, 단독 파이프는 모두 NgModule을 생략하기 위한 것입니다. NgModule 방식으로 개발된 애플리케이션이라면 단독 컴포넌트 스타일을 점진적으로 적용할 수 있습니다.
```typescript
import {Component} from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    Hello
  `,
  styles: `
    :host {
      color: blue;
    }
  `,
  standalone: true,
})
export class AppComponent {}

```
- 단독 컴포넌트에서 NgModule 활용하기
```typescript
@Component({
  standalone: true,
  selector: 'photo-gallery',
  // 단독 컴포넌트에 모듈을 직접 로드합니다.
  imports: [MatButtonModule],
  template: `
    ...
    <button mat-button>Next Page</button>
  `,
})
export class PhotoGalleryComponent {
  // logic
}
```
- NgModule 기반 애플리케이션에서 단독 컴포넌트 사용하기
```typescript
@NgModule({
  declarations: [AlbumComponent],
  exports: [AlbumComponent], 
  imports: [PhotoGalleryComponent],
})
export class AlbumModule {}
```
- 라우터 API는 단독 컴포넌트가 도입되면서 더 단순해졌습니다. 이제는 지연 로딩 하는 경우에 NgModule을 사용하지 않습니다.

2. @If / @else
```typescript
template: `
  @if (isServerRunning) { ... }
  @else { ... }
`;
```
3. @for
```
template: `
  @for (os of operatingSystems; track os.id) {
    {{ os.name }}
  }

  @for (user of users; track user.id) {
    <p>{{ user.name }}</p>
  }
`,
```
4. 
5. 




