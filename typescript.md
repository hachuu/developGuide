# 제네릭
- 정의 : 어떠한 클래스 혹은 함수에서 사용할 타입을 그 함수나 클래스를 사용할 때 결정하는 프로그래밍 기법
- any와 다른점 : any는 param, response의 타입을 미정으로 두는 반면 제네릭은 객체를 생성시 타입을 지정할 수 있어 type을 알 수 있다.
```
export class ApiService {
  buildApi<T, U>(apiSpec: ApiSpec<T, U>, store?: boolean) {
    let api: Api<T, U> = new Api(this.platformId, this.http, this.state, apiSpec, store);

    return api;
  }
}

getSessionApi: Api<void, ResponseModel<Session>>;
constructor(
    private apiService: ApiService
) {
  this.getSessionApi = this.apiService.buildApi(getSessionApiSpec, true);
}
```

# Union type
- 정의 : any 대신 쓸 수 있는 타입 별칭/ 하나 이상의 타입을 명시
- cf : intersection type : &로 묶여있음 (잘 안쓰임)
```
const age: string | number
```

# Enums 이넘
- 정의 : 특징 값들의 집합을 의미
```
  enum Shoes {
    Nike,
    Adidas
  }
  const nike = Shoes.Nike;
  console.log(nike); // 0
```
