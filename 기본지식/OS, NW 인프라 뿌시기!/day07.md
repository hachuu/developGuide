# Day 7: 전체 흐름 정리 (Infra End-to-End)

## 0. 기존 학습 방식의 문제 (가정 깨기)
**사람들이 암묵적으로 믿는 가정**
- HTTP, DNS, TCP는 각각 독립 개념이다
- 요청은 단순히 서버에 가서 응답을 받는다
- 성능 문제는 서버 성능 문제다
- 로드 테스트는 마지막 단계다

**실제 구조**
- 이건 “단계별 개념”이 아니라 하나의 요청이 지나가는 파이프라인
- 병목은 항상 연결 지점(interface) 에서 발생

## 1. 전체 구조 한 줄 정의

> “사용자 입력 → 네트워크 경로 → 서버 처리 → 응답 반환”

**이걸 물리적으로 풀면:**
```
[User]
 → DNS 조회
 → TCP 연결
 → TLS handshake
 → HTTP 요청
 → 서버 처리
 → HTTP 응답
 → 렌더링
```

## 2. 단계별 흐름 (Day 1 ~ 6 통합)
1. DNS (Day 2)
<img width="975" height="419" alt="image" src="https://github.com/user-attachments/assets/99a518ca-04f3-4811-a389-cdf263926d85" />

- 역할
  - 도메인 → IP 변환
- 핵심 포인트
  - 브라우저 캐시 → OS 캐시 → DNS 서버 순으로 조회
  - 여러 IP 반환 가능 (로드 분산)
- 실무 포인트
  - DNS latency = 첫 번째 병목
  - TTL 설정이 중요

2. TCP 연결 (Day 3)
<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/faa60e75-e1e4-4d2a-887b-782374abaf42" />

- 역할
  - 신뢰성 있는 연결 생성
- 핵심
  - 3-way handshake
  - SYN → SYN-ACK → ACK
- 실무 포인트
  - RTT에 직접 영향
  - 연결 수 증가 = 서버 부담 증가

3. TLS Handshake (Day 1 확장)
<img width="2386" height="756" alt="image" src="https://github.com/user-attachments/assets/b9a2891f-2734-4b1e-b37d-16f3678b03ce" />

- 역할
  - 암호화 채널 생성 (HTTPS)
- 핵심
  - 인증서 검증
  - 세션 키 생성
- 실무 포인트
  - CPU 사용량 증가
  - TLS 재사용(session reuse) 중요

4. HTTP 요청/응답 (Day 1)
<img width="900" height="680" alt="image" src="https://github.com/user-attachments/assets/7b8e1281-c3b7-42a8-84e8-82c0e1b020c2" />

- 역할
  - 실제 데이터 전달
- 핵심
  - Request: Header + Body
  - Response: Status + Data
- 실무 포인트
  - HTTP/2 → multiplexing
  - 캐싱 전략 중요 (CDN)

5. 서버 처리 (Day 4, Day 5)
<img width="938" height="708" alt="image" src="https://github.com/user-attachments/assets/3725d15b-2b0e-4357-9372-63c62af745f8" />

- 역할
  - 요청 처리
- 내부 흐름
  - Port → Process → Thread → Application Logic → DB
- 실무 포인트
  - CPU vs I/O 병목 구분
  - connection pool 중요

6. 로드 테스트 (Day 6)
<img width="584" height="606" alt="image" src="https://github.com/user-attachments/assets/132561c2-7283-4102-b58d-c83246ffab14" />

- 역할
  - 시스템 한계 확인
- 핵심 지표
  - TPS / RPS
  - Latency
  - Error rate
- 실무 포인트
  - 병목은 항상 특정 구간에 집중됨
    - DNS?
    - TCP?
    - 서버?
    - DB?

## 3. 전체 흐름 재정의 (핵심)
**기존 관점 ❌**
- HTTP 따로
- TCP 따로
- DNS 따로
**재설계 관점 ✅**
>👉 “Latency Stack”으로 봐야 한다

```
Total Latency =
 DNS
 + TCP
 + TLS
 + Request Transfer
 + Server Processing
 + Response Transfer
```

## 4. 진짜 중요한 개념 (실무 기준)
1. 병목은 항상 한 곳이다
- 동시에 다 느려지지 않는다
2. 연결이 비싸다
- TCP + TLS = 비용 큼
- 그래서 keep-alive 사용
3. 서버보다 네트워크가 먼저 터진다
- 많은 경우 CPU보다 네트워크/connection 문제
4. 캐싱이 성능의 핵심이다
- CDN → origin 안 가게 만드는 구조
5. 실행 계획 (당신 기준)
- Step 1: 눈으로 흐름 확인
```
curl -v https://example.com
```
- 확인할 것:
```
DNS resolve
TCP connect
TLS handshake
HTTP response
```
- Step 2: 구간별 시간 측정
```
curl -w "@curl-format.txt" -o /dev/null -s https://example.com
```
- 분석:
```
time_namelookup
time_connect
time_starttransfer
```
- Step 3: 서버 띄워서 실험
  - Node / Python 서버 실행
  - 단일 요청 latency 확인
- Step 4: 부하 걸기
  - k6 / ab / wrk 사용

확인:

- 언제 latency 증가?
- 어디서 에러 발생?

- Step 5: 병목 추적
  - CPU?
  - DB?
  - 네트워크?
  - connection 수?


## 6. 실수 포인트 (중요)
1. HTTP만 보고 판단
→ 실제 문제는 TCP / TLS일 수 있음

2. 평균 latency만 봄
→ p95, p99 봐야 함

3. 로컬 테스트만 믿음
→ 실제는 네트워크 영향 큼

4. 서버 코드만 최적화
→ DB / connection pool이 문제일 가능성 큼

## 7. 최종 한 줄 정리

> 👉 “웹 요청은 단순한 API 호출이 아니라, 네트워크 + 연결 + 서버 처리의 합성 시스템이다”

## 8. 다음 단계 (진짜 실력 구간)

여기서 한 단계 올라가려면:
- CDN (Cloudflare)
- Keep-Alive / Connection reuse
- HTTP/2 vs HTTP/3
- Load Balancer
- 장애 상황 분석
