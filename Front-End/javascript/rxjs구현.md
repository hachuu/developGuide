# slide 작업
```
ngOnInit(): void {
  this.subscription = timer(0, 10000).pipe(
    ).subscribe(() => !this.focusSlide ? this.currentSlideIdx = (this.currentSlideIdx +1) % 4 : null);
}
```
```html
<div id="u_slideShowFade" class="slideshowfade" (mouseover)="focusSlide = true" (mouseout)="focusSlide = false;">
```

# count down 작업
```
this.remainTimes = '10:00';
const interval$ = interval(1000);
const duration = 599000//599000;
this.remainSubscription = interval$.pipe(takeUntil(timer(duration+2000))).subscribe(value => {
  const oneMin = 60000;
  const currentSec = duration - (value * 1000);
  const m = Math.floor(currentSec / oneMin);
  const s = (currentSec % oneMin)/1000;
  const format_m = (''+m).length < 2 ? `0${m}` : m;
  const format_s = (''+s).length < 2 ? `0${s}` : s;
  this.remainTimes = `${format_m}:${format_s}`;
});
// 10:00
// 09:59...
```
