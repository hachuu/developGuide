# Day 3 - HTTP / CDN / Cache (요청 흐름 해부)

## 🎯 목표
> 요청 하나가 어디까지 갔는지 판단할 수 있는 상태 만들기

---

# 1. 전체 흐름 (Day 1~3 통합)

```
[User]
↓
[DNS]
↓
[TCP 연결]
↓
[TLS 보안 연결]
↓
[HTTP 요청]
↓
[CDN]
↓
[Server (Origin)]

```
---

# 2. HTTP 구조 이해

## 2.1 Request (요청)

```
GET /api/user?id=1 HTTP/1.1
Host: example.com
User-Agent: Chrome
Cookie: session=abc
```

### 핵심 요소
- Method: GET / POST
- Path: /api/user
- Query: id=1
- Header: 추가 정보 (브라우저, 인증 등)
- Cookie: 자동으로 포함되는 사용자 정보

---

## 2.2 Response (응답)

```
HTTP/1.1 200 OK
Content-Type: application/json
Cache-Control: max-age=3600
{ "name": "hayoung" }
```

### 핵심 요소
- Status Code: 200, 404, 500
- Header: 캐시 정책, 데이터 타입
- Body: 실제 데이터

---

# 3. HTTP/1.1 vs HTTP/2

| 항목 | HTTP/1.1 | HTTP/2 |
|------|---------|--------|
| 연결 방식 | 요청마다 | 하나의 연결 |
| 처리 방식 | 순차 처리 | 병렬 처리 |
| 속도 | 느림 | 빠름 |

### 한 줄 정리
> HTTP/2는 하나의 연결에서 여러 요청을 동시에 처리

---

# 4. CDN (Content Delivery Network)

## 4.1 개념

- 서버 앞에 있는 "중간 캐시 서버"
- 자주 요청되는 데이터를 미리 저장

---

## 4.2 비유

| 역할 | 의미 |
|------|------|
| 공장 | 서버 (Origin) |
| 편의점 | CDN |
| 손님 | 사용자 |

---

# 5. Cache 상태 (핵심)

## 5.1 HIT
```
cf-cache-status: HIT
```

### 의미
- CDN에 데이터 있음
- 서버까지 요청 안 감

### 특징
- 빠름
- 서버 로그 없음

---

## 5.2 MISS

```
cf-cache-status: MISS
```

### 의미
- CDN에 데이터 없음
- 서버까지 요청 감

### 흐름

```
Client → CDN → Server → CDN 저장 → Client
```

### 특징
- 느림
- 서버 로그 있음

---

## 5.3 BYPASS

### 의미
- 캐시 사용 안 함

### 이유
- 로그인
- 개인 데이터
- 보안

---

# 6. curl로 흐름 확인

## 명령어

```
curl -v https://example.com
```

## 확인 포인트

- Connected IP
- TLS handshake 여부
- HTTP 버전
- 응답 코드
- cf-cache-status

---

# 7. 핵심 판단 질문 (중요)

## 1. 서버까지 갔는가?
- HIT → ❌ 안 감
- MISS → ⭕ 감

---

## 2. 왜 느린가?

### 가능한 원인:
- DNS
- TCP 연결
- TLS handshake
- CDN MISS
- 서버 처리

---

## 3. 지금 어느 레이어인가?

```
DNS → TCP → TLS → HTTP → CDN → Server
```

---

# 8. 자주 하는 실수

## ❌ 캐시 무시
→ 잘못된 분석

---

## ❌ HIT인데 서버 디버깅
→ 시간 낭비

---

## ❌ HTTP만 보고 판단
→ TLS / TCP 문제 놓침

---

# 9. 핵심 요약

- CDN은 단순 속도 개선이 아니라 서버를 대신함
- HIT이면 서버까지 요청이 가지 않는다
- MISS일 때만 실제 서버 동작 확인 가능
- 문제 해결은 항상 "어느 레이어인지"부터 판단

---

# 10. 한 줄 정리

> 요청은 항상 서버로 가지 않는다  
> 대부분 CDN에서 끝난다
