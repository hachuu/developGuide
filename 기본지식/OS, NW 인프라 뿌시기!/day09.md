# Day 9: Thread vs Event Loop

## 1. 학습 목표
- Thread 기반 서버 구조 이해
- Event Loop 동작 원리 이해
- Node.js와 Python의 구조적 차이 파악
- 실무에서 어떤 상황에 어떤 모델을 선택해야 하는지 판단

## 2. 문제 정의
서버는 결국 하나의 문제를 해결한다.
| 여러 요청을 동시에 처리하는 방법 (Concurrency)
이를 해결하는 대표적인 방식은 두 가지다:
```
1. Thread 기반 모델
2. Event Loop 기반 모델
```


## 3. Thread 기반 모델
### 3.1 구조
```
요청 1 -> Thread 1
요청 2 -> Thread 2
요청 3 -> Thread 3
```

### 3.2 특징
- 요청마다 Thread 생성 또는 할당
- 병렬 처리 가능 (멀티코어 활용)

### 3.3 장점
- CPU 연산 작업에 강함
- 직관적인 코드 작성 (동기 방식)

### 3.4 단점
**Context Switching 비용**
- Thread 전환 시 CPU 오버헤드 발생

**메모리 사용 증가**
- Thread마다 Stack 메모리 필요

**동기화 문제**
- 공유 자원 접근 시 Lock 필요
- Race Condition / Deadlock 위험

### 3.5 한 줄 정리
| 이해하기 쉽지만 비용이 큰 구조

## 4. Event Loop 기반 모델 (Node.js)
### 4.1 구조
```
요청들 -> Queue -> Event Loop -> 순차 처리
```

### 4.2 핵심 개념
- Single Thread
- Non-blocking I/O
- 비동기 처리 (Callback / Promise / async-await)

### 4.3 동작 흐름
```
1. 요청 수신
2. 오래 걸리는 작업
3. Event Loop는 다음 작업 계속 수행
4. 작업 완료 시 Callback Queue에 등록
5. Event Loop가 Callback 실행
```

### 4.4 장점

**Context Switching 없음**
- Thread 전환 비용 없음
  
**낮은 메모리 사용**
- Thread 최소화
  
**I/O 처리 효율적**
- 대기 없이 다음 작업 처리

### 4.5 단점
**CPU 작업에 취약**
```JavaScript
whild(true) {}
```
-> Event Loop Block -> 서버 전체 멈춤

**단일 장애 영향**
- 하나의 Blocking 코드가 전체 서비스에 영향

### 4.6 한 줄 정리
| 기다리지 않지만, 막히면 전체가 멈춘다

## 5. Thread VS Event Loop 비교
| 항목     | Thread   | Event Loop |
| ------ | -------- | ---------- |
| 처리 방식  | 병렬 처리    | 비동기 순차     |
| CPU 작업 | 강함       | 약함         |
| I/O 작업 | 비효율적     | 매우 효율적     |
| 메모리 사용 | 높음       | 낮음         |
| 안정성    | 일부 장애 격리 | 전체 영향      |
| 구현 난이도 | 쉬움       | 설계 필요      |

## 6. Node.js vs Python 선택 기준
**Node.js**
- Event Loop 기반
- I/O 중심 작업에 적합

**사용 사례**
- API 서버
- 실시간 서비스
- 외부 API (LLM, RAG) 호출

**Python**
- Multi-thread / Multi-process 기반
- CPU 연산 작업에 적합

**사용 사례**
- AI / ML 처리
- 데이터 분석
- 배치 작업

**결론**
| 상황            | 선택      |
| ------------- | ------- |
| 네트워크 / API 중심 | Node.js |
| 연산 / 모델 처리    | Python  |

## 7. Node 확장 전략 (pm2)
Node.js는 Single Thread 구조이기 때문에 확장이 필요하다.

**해결 방법: Multi-process**
```
pm2 start app.js -i max
```

```
App 1 (Event Loop)
App 2 (Event Loop)
App 3 (Event Loop)
```

**핵심**
| Node는 싱글 스레드지만, 멀티 프로세스로 확장한다

## 8. 실무 장애 패턴
### 8.1 Blocking 코드 사용
```JavaScript
fs.readFileSync(...)
```
-> Event Loop Block

### 8.2 CPU-Heavy 작업
- 이미지 처리
- 암호화
- 대량 계산

-> Node에서 처리 시 성능 저하

### 8.3 잘못된 async 사용
```JavaScript
await heavyFunction()
```
-> 내부가 blocking이면 비동기 의미 없음

## 9. 성능 병목의 본질
```
CPU vs Memory vs I/O
```
하지만 실제 서버 명목은:
| I/O대기 + Event Loop 처리 방식

## 10. 핵심 요약
**Thread**
| 여러 작업을 동시에 처리 (병렬)
| -> 강력하지만 비용이 큼

**Event Loop**
| 하나의 흐름으로 빠르게 처리 (비동기)
| -> 효율적이지만 blocking에 취약

## 11. 결론
| 동시성은 반드시 멀티 스레드로 해결할 필요는 없다.
