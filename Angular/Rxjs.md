# Rxjs 요청에 따른 에러 처리

```
import { Observable, of } from 'rxjs';
import { ajax } from 'rxjs/ajax';
import { map, retry, catchError } from 'rxjs/operators';

const apiData = ajax('/api/data').pipe(
  map((res: any) => {
    if (!res.response) {
      console.log('Error occurred.');
      throw new Error('Value expected!');
    }
    return res.response;
  }),
  retry(3), // 옵저버블에 에러가 발생하면 3번 재시도합니다. => 아니 이런 것도 된다고?
  catchError(() => of([]))
);

apiData.subscribe({
  next(x: T) { console.log('data: ', x); },
  error() { console.log('errors already caught... will not run'); }
});
```
- '사용자 인증이 필요한 요청은 재시도하지 마세요. 이 동작은 사용자에 의해서만 수행되어야 합니다. 사용자가 요청하지 않은 상태에서 계속 로그인 시도가 된다면 비정상적인 공격 시도로 처리될 수 있습니다.'
- 옵저버블 변수 명명 규칙: 구독할 수 있는 변수는 이름 뒤에 $를 붙여줌
