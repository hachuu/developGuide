- formArrayName
```
export class FormArrayExampleComponent {

    form = this.fb.group({
        ... other form controls ...
        lessons: this.fb.array([])
    });

    constructor(private fb:FormBuilder) {}
  
    get lessons() {
      return this.form.controls["lessons"] as FormArray;
    }

    addLesson() {
      const lessonForm = this.fb.group({
        title: ['', Validators.required],
        level: ['beginner', Validators.required]
      });
      this.lessons.push(lessonForm);
    }

    deleteLesson(lessonIndex: number) {
      this.lessons.removeAt(lessonIndex);
    }
}
```
```
<div class="add-lessons-form" [formGroup]="form">
    <ng-container formArrayName="lessons">
        <ng-container *ngFor="let lessonForm of lessons.controls; let i = index">
            <div class="lesson-form-row" [formGroup]="lessonForm">
                <mat-form-field appearance="fill">
                    <input matInput
                           formControlName="title"
                           placeholder="Lesson title">
                </mat-form-field>
                <mat-form-field appearance="fill">
                    <mat-select formControlName="level"
                            placeholder="Lesson level">
                        <mat-option value="beginner">Beginner</mat-option>
                        <mat-option value="intermediate">Intermediate</mat-option>
                        <mat-option value="advanced">Advanced</mat-option>
                    </mat-select>
                </mat-form-field>
                <mat-icon class="delete-btn" (click)="deleteLesson(i)">
                    delete_forever</mat-icon>
            </div>
        </ng-container>
    </ng-container>
  
    <button mat-mini-fab (click)="addLesson()">
        <mat-icon class="add-course-btn">add</mat-icon>
    </button>

</div>
```