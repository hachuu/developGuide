1. shift+enter check
```
function handleEnter(evt) {
    if (evt.keyCode == 13 && evt.shiftKey) {
        if (evt.type == "keypress") {
        }
        evt.preventDefault();
    }
}
```
2. textarea 현재 커서의 위치를 찾는다
```
  // 입력받은 @의 index를 찾는다.
  // 현재 커서의 위치를 찾는다.
  // @의 위치와 커서의 위치를 비교한다.
  // @의 위치가 커서의 위치보다 작으면 자동완성을 띄운다.
  this.indexOfAt = event.target.selectionStart;
```

3. [mac에서 input file할때 한글 깨짐 현상](https://gemimi.tistory.com/43)
  ```
  fileName = Normalizer.normalize(fileName, Normalizer.Form.NFC)
  ```
---

```
ngAfterViewInit() {
    window.onpageshow = (event) => {
      if ( event.persisted || (window.performance && window.performance.navigation.type == 2)) {
        this.loginForm.reset();
      }
    }
  }
```
4. [아이폰 사파리 script ](https://orangeheeya.tistory.com/entry/%EB%AA%A8%EB%B0%94%EC%9D%BC-%EC%95%84%EC%9D%B4%ED%8F%B0-%EC%86%8C%EC%8A%A4%EC%BD%94%EB%93%9C%EB%B3%B4%EA%B8%B0)

5. frontend
```
  a tag에서 keyup.enter 이벤트는 (click)과 동일한 이벤트로 인지하여 둘다 선언하는 경우 이벤트가 중복되어 사용됨

  => (keyup.enter)를 삭제 해줘야함
```

6. IE => edge로 연결
```
<script>
  var agent = navigator.userAgent.toLowerCase();
  if ( (navigator.appName == 'Netscape' && agent.indexOf('trident') != -1) || (agent.indexOf("msie") != -1)) {
    window.location = 'microsoft-edge:' + window.location;
    setTimeout(function () {
    //window.close();
    window.open('','_self').close();
  }, 1000);
  }
</script>
```
7. javascript 퍼포먼스 속도 체크하기
```
const t0 = performance.now()
for (let i = 0; i < array.length; i++) {
  // some code.......
}
const t1 = performance.now()
console.log(t1 - t0, 'milliseconds')
```

8. device나 mobile/pc 판별
```
  /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
```


9. SEO canonical 기존 link rel 삭제, 새로 등록하는 script
```
const headerDoc = this.document.head;
const bodyDoc = this.document.body;
for (let i = 0; i < bodyDoc.children.length; i++) {
  if (bodyDoc.children[i].localName === 'link' && bodyDoc.children[i].rel === 'canonical') bodyDoc.children[i].remove();
}
for (let i = 0; i < headerDoc.children.length; i++) {
  if (headerDoc.children[i].localName === 'link' && headerDoc.children[i].rel === 'canonical') headerDoc.children[i].remove();
}

const domain = 'www....';

var link = document.createElement('link');
link.setAttribute('rel', 'canonical');
link.setAttribute('href', 'https://' + domain + window.location.pathname);
document.head.appendChild(link);
```
