# Day 8: Blocking vs Non-blocking + Node vs Python (OS 관점)

## 1. 본질 질문
> "CPU가 기다리는 시간을 어떻게 처리할 것인가?"
모든 성능 차이는 여기서 시작된다.

## 2. Blocking vs Non-blocking (재정의)
### Blocking
- 작업이 끝날 때까지 다른 일을 못함
- CPU가 대기 상태 (Idle)
```
요청1 → DB 요청 → 기다림 → 응답 → 요청2
```
### Non-blocking
- 기다리는 동안 다른 요청 처리
- CPU가 계속 일함
```
요청1 → DB 요청 (OS 위임)
→ 요청2 처리
→ 요청3 처리
→ 완료되면 callback 처리
```
### 핵심 차이
|구분	|Blocking	|Non-blocking|
|---|---|---|
|CPU 사용	|낭비	|효율|
|처리 방식	|직렬	|동시성|
|성능	|낮음	|높음|

## 3. Node.js 구조 (OS 관점)
![alt text](https://images.openai.com/static-rsc-4/pP46HF1js2NgYN3tRIZZtUQrxPu_JUAsvFd5sIzjRF3kq7S6gIirgsCZUlqGxA96qjfuB0jhs2szkv2Gu_RfpaHarbiTN8e90dj5JKKCGrXT9KwpMqJ7IGZ6kaNo2G-NOxyZGldJCDbMut2mgFlIESgw7NmLpkFopdEY62RW-jaRYSoaQu9DVP2MJHaQHX8d?purpose=fullsize)

![alt text](https://images.openai.com/static-rsc-4/oO0rEC4tbD4-qvGl0R6bSYCucunPn4kQ6pBnhf0KKJ7lvIyLHI3_5MDJJsZrRne3RkMDHwq9hpB9oABTohHE9u-343jJVGmzSx-OmfGhaNx7oSDyi1kTsV5VsOvoAtyHZZ-L4VJlGfrsaXYFYz6720KG2gzv_eCdfcIhtgDICVMs86pK0n4se32RO8jwGjfB?purpose=fullsize)
![alt text](https://images.openai.com/static-rsc-4/nNwV6oK2ZakIRQdxLTq2DfPxsd4QtXDQTydnEJ2n9S2Dimdp7GJC2hTp62olMz0hseB5jnsC9w5gUZ_LdMFBUl6fdEYm-qS2xR3ykVUz2eN-BxBBdZFrY6c9lOhqTwrdmtCDlHYRujXQGS22GSuARu0rLN9WimjsLu4bqMd_eW-JeZE4GaC8xc-Kg08SVHPk?purpose=fullsize)
![alt text](https://images.openai.com/static-rsc-4/R4eUXTjpJ_-i1bX5TQjXCl11OZQN_Dm1FBCkyBABmCw0wr9eS0XclJD2fC77xHlFRlnuRdy_Knly_P_Z4fd_rBDqXbmd56o_xmEhGZptRya5IQVhrvzyeNJghLUf_v8K7hoUx405AuK-zICLl-xn_xw09Nlv2U8GNl0H9tog-lWa_8Usz3UWEUxk_cBy87V6?purpose=fullsize)
**구조**
1. Event Loop (싱글)
2. I/O 작업 → OS 또는 libuv에 위임
3. 완료 → callback queue
4. 다시 처리

## 핵심 정의
> Node.js는 직접 작업하지 않고, I/O를 OS에 위임한다

## 4. 싱글 스레드의 오해
**잘못된 이해**
> "Node는 싱글 스레드라서 느리다"

## 실제 구조
- JS 실행 → 싱글 스레드
- I/O 처리 → OS / thread pool

## 결론
> Node는 싱글 스레드가 아니라 "싱글 이벤트 루프 기반"

## 5. PM2를 통한 확장
**PM2**
> Node의 싱글 한계를 프로세스로 확장

### 실행
```
pm2 start app.js -i max
```
## 내부 구조
```
프로세스1 → event loop 1
프로세스2 → event loop 2
프로세스3 → event loop 3
프로세스4 → event loop 4
```

## 핵심
> 프로세스 수 = 이벤트 루프 수

## OS 관점
![alt text](https://images.openai.com/static-rsc-4/OkefOsK7vxiTO_7vbgq_TV1y1A1q-yn9Avc7LVgGDeKbeZyULUgdAdcpVhEVvavIRQQXGqlCjo1ljztLJosDkYx2KlYIEvD0q3HJsTXtGxu7l-BcaidhZImXGOZjikF0jZJyYl01J-UgsXCbxplnzsD4tml-TuPE5zzXdI_Q1bo?purpose=inline)

![alt text](https://images.openai.com/static-rsc-4/fr1ObFlWHPS0G-lowvvJcVfIFAkOi2m0Fb-aJFC1v5W8pDfIB73M6gpJOGFmcAISEXCLeK3pf0ew8s7x088zhzjPVRAzqHv9hlsLpvtOmFNt_ZWPRiTFqquABhkcXvkr3sMtYBuaff4sih11O6jn-Tkm1tLLRJRwUWbkTEbC2SoIlPLPanXpt43YEP3xIReP?purpose=fullsize)
- 각 프로세스는 독립
- OS가 CPU 코어에 분산 실행

## 정리
|항목	|설명|
|---|---|
|Node 기본	|1 process = 1 event loop|
|PM2	|멀티 프로세스|
|결과	|멀티 코어 활용 가능|

## 6. Python vs Node (본질 비교)
|항목	|Node|	Python|
|---|---|---|
|구조	|Event loop	|Thread / Async 혼합|
|I/O 처리	|매우 효율적	|구조에 따라 다름|
|컨텍스트 스위칭	|적음	|상대적으로 많음|
|생태계	|웹/서버	|AI/ML|

## 핵심	
> 언어가 아니라 실행 모델이 중요하다

## 7. Agent 구조에 따른 언어 선택
### 1) Node가 적합한 경우
- API orchestration
- LLM API 호출
- 실시간 요청 처리
- I/O 중심 서비스
### 2) Python이 적합한 경우
- RAG
- 임베딩 생성
- 모델 실행 (GPU)
- 데이터 처리 / 실험
### 핵심 구조
```
Node → 오케스트레이션 (요청/응답, 라우팅)
Python → 모델/데이터 처리
```
## 8. 왜 Python Agent가 많은가
**이유**
- LangChain
- LlamaIndex
- PyTorch

👉 대부분 Python 기반

## 본질
> Python은 모델과 가깝고, Node는 서비스와 가깝다

## 9. 실무 리스크
### Node
- CPU 작업 → event loop block
- pm2로 성능 개선 착각
### Python
- async 구조 잘못 쓰면 blocking 유지
- thread 남용 → context switching 증가
## 10. 재설계 (제1원칙)
기존 생각:
> Node는 편해서 선택

재정의:
> Node는 I/O 대기 제거 + OS 위임 구조 때문에 선택된 것

## 핵심 3줄 요약
1. Blocking vs Non-blocking의 차이는 CPU가 기다리느냐 아니냐
2. Node는 event loop + OS 위임 구조로 I/O를 효율적으로 처리
3. 실무에서는 Node(오케스트레이션) + Python(모델) 구조가 가장 자연스럽다

## 마지막 체크
> pm2로 4개 실행하면 event loop는 몇 개인가?
👉 정답: 4개