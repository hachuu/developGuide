# 정규식 검사

[출처 https://poiemaweb.com/js-regexp](https://poiemaweb.com/js-regexp)
![img](https://github.com/hachuu/developGuide/blob/main/image/6F0B9C2C-65B6-4BA6-8E92-B85DB7DFDF6B.jpeg)

[자바스크립트 정규식 질문(괄호 문자 찾기)](https://okky.kr/article/428993)

- 세 자리 콤마찍기
```
num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
```
 
- 콤마 지우기
```
return num.replace(/,/g, "");
```

- Angular formbuild (회원가입) 정규식 체크 구현
```
// email, password, passwordConfirm, name, phone, typing input text, 비밀번호 같은지 여부
formBuilderSetting() {
  this.signupForm = this.signupFormBuilder.group({
    email:  ['', Validators.compose([Validators.required, Validators.pattern(/^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/)])],
    password: 
    ['', Validators.compose([Validators.required, Validators.minLength(8), Validators.maxLength(16), Validators.pattern(/((?=.*\d)(?=.*[a-zA-Z]))/)])],
    passwordConfirm: ['', Validators.compose([Validators.required])],
    firstName: ['', Validators.compose([Validators.required, Validators.pattern(/^[가-힣a-zA-Z]*$/)])],
    lastName: ['', Validators.compose([Validators.required, Validators.pattern(/^[가-힣a-zA-Z]*$/)])],
    // phone: ['', Validators.compose([Validators.required, Validators.pattern(/^0+[0-9]{8,10}$/g)])],
    phone: ['', Validators.compose([Validators.required, Validators.pattern(/^[0]+[0-9]*$/), Validators.minLength(9)])],
    // company: ['', Validators.required],
    company: ['', Validators.required],
    companyType: ['', []],
    companyTypeInput: ['', Validators.compose([Validators.required, Validators.pattern(/^[가-힣a-zA-Z]*$/)])],
    position: ['', []],
    positionInput: ['', Validators.compose([Validators.required, Validators.pattern(/^[가-힣a-zA-Z]*$/)])],
  }, {
    validator: this.isSamePassword()
  });
}

isSamePassword() {
  return (formGroup: FormGroup) => {
    const password = formGroup.controls['password'];
    const passwordConfirm = formGroup.controls['passwordConfirm'];
    if (passwordConfirm.errors && !passwordConfirm.errors.confirmedValidator) {
        return;
    }
    if (password.value !== passwordConfirm.value) {
      passwordConfirm.setErrors({'samePassword': true});
    } else {
      passwordConfirm.setErrors(null);
    }
  }
}
```

