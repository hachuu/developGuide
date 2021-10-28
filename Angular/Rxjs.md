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


