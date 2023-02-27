
1. $의 의미? cf : _의 의미?
```
_개인 인스턴스 속성용입니다.

Vue는 _ 접두사를 사용하여 자체 개인 속성을 정의합니다...

$공용 인스턴스 속성용입니다.

$ 접두사의 경우 Vue 생태계 내에서의 목적은 사용자에게 노출되는 특수 인스턴스 속성입니다

```
- $접두사는 Vue의 핵심 API에서만 사용되는 것이 아닙니다.
- 구성 요소에 속성을 추가하는 라이브러리에서도 일반적으로 사용됩니다.
```
예:

Vuex는 $store.
Vue 라우터는 $route및 $router.
```

2. store에서 mapActions
```
..mapActions([
  'increment' // this.increment()을 this.$store.dispatch('increment')에 매핑
]),
...mapActions({
  add: 'increment' // this.add()을 this.$store.dispatch('increment')에 매핑
})
```

3. watch
- watch 속성은 특정 데이터의 변화를 감지하여 자동으로 특정 로직을 수행해주는 속성

4. computed
- 컴퓨티드(computed) 속성은 템플릿의 데이터 표현을 더 직관적이고 간결하게 도와주는 속성

5. 동적 component 제어
```
<component 
  :is="{문자열이나 컴포넌트 이름}"
/>
<script>
components: { nonArtist, artist, Promotion }
</...>
```
6. router
- router에 params도 구상해서 작업할 수 잇음

|pattern|matched path|$route.params|
|---|-------|-------|
|/user/:username|/user/evan|{ username: 'evan' }|
|/user/:username/post/:post_id|/user/evan/post/123|{ username: 'evan', post_id: '123' }|

		
```
const User = {
  template: '<div>User {{ $route.params.id }}</div>'
}

// route 변경 감지 1. watch로 감지
const User = {
  template: '...',
  watch: {
    $route(to, from) {
      // react to route changes...
    }
  }
}

// route 변경 감지 2. beforeRouteUpdate 감지
const User = {
  template: '...',
  beforeRouteUpdate(to, from, next) {
    // react to route changes...
    // don't forget to call next()
  }
}

```

7. src 절대 경로
- @로 src내 파일 절대경로로 사용할 수 있다.
- 이미지 경로가  src/assets/img/sample.png 일때 vue 에서는 @/assets/img/sample.png 로 src를 절대경로로 사용 할 수 있다.
```
<!-- 이미지 삽입 -->
<img src = "@/assets/img/sample.png" />
```

8. directive
```
v-text
v-html
v-show
v-if
v-else
v-else-if
v-for
v-on
v-bind
v-model
v-slot
v-pre
v-once
v-memo
v-cloak
```

9. resolver
- Angular에 있던 개념인데.. Vue에는 따로 기능이 없어서 아래 예시문처럼 작업하면 된다.
- onBeforeRouteEnter : Vue Router and the Composition API
```
import { ref } from 'vue'
import { useRoute } from 'vue-router'

export default {
  setup() {
    const route = useRoute()
    const data = ref(null)

    onBeforeRouteEnter(async (to, from, next) => {
      const result = await fetchData(route.params.id)
      data.value = result
      next()
    })

    return { data }
  }
}
```
