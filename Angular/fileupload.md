``` html
<form [formGroup] = "uploadForm">
  <a class="upload-name" [ngClass]="{'hover': !!fileName}" (click)="downloadFile()" href="javascript:void(0)" (keyup.enter)="downloadFile()">
  {{fileName || '파일선택'}}</a>
  <label for="file" tabindex="0" (keyup.enter)="clickFileUpload()">업로드</label> 
  <input type="file" id="file" 
  accept="image/png, image/jpeg, image/jpg, application/pdf"
  (change)="onFileSelected(fileUpload.files)"
  #fileUpload> 
</form>
```

```
@ViewChild('fileUpload', { static: false }) fileUpload!: ElementRef;
uploadForm: FormGroup;
fileName: string = '';

constructor(private formBuilder: FormBuilder) {
  this.uploadForm = this.formBuilder.group({
    file: ['']
  });
}

onFileSelected(files: any) {
  if (files && files[0]) {
    this.uploadForm.get('file')?.setValue(files[0]);
    this.fileName = files[0].name;
  }
}

async onSubmit() {
  const formData = new FormData();
  formData.append('file', this.uploadForm.get('corpReg')?.value);
  // formData.append('param', this.param); : 추가 param
}
```
