# Day 4 - 서버 확장 구조 (Load Balancing & Scaling)
## 1. 문제 정의

기존 구조:
```
Client → Server (1대)
```

문제:
- 트래픽 증가 시 성능 저하
- 서버 장애 시 전체 서비스 다운 (SPOF)
- 확장성 없음

## 2. 잘못된 가정 (First Principles)

| 가정               | 실제                 |
| ---------------- | ------------------ |
| 서버 성능 올리면 해결됨    | 한계 존재 (비용, 물리적 한계) |
| 서버는 1대면 충분       | SPOF 발생            |
| 요청은 한 곳에서 처리해야 함 | 분산 처리 가능           |

## 3. 해결 구조
```
Client
  ↓
Load Balancer
  ↓
App Server (N개)
```
## 4. 핵심 개념
### 4.1 Load Balancer
요청을 여러 서버로 분산

**대표 알고리즘**
- Round Robin
- Least Connections
- IP Hash
  
### 4.2 Horizontal Scaling

| 방식         | 설명      |
| ---------- | ------- |
| Vertical   | 서버 스펙 업 |
| Horizontal | 서버 수 증가 |


👉 실무에서는 Horizontal Scaling 사용

### 4.3 Stateless

서버가 상태를 가지지 않도록 설계

**문제**

- 로그인 세션
- 사용자 상태 유지

**해결**

- Redis
- DB
- JWT
  
## 5. 전체 아키텍처
```
Client
  ↓
CDN (Cloudflare)
  ↓
Load Balancer
  ↓
App Server (N개)
  ↓
DB / Redis
```

## 6. 실습 (로컬 환경)
### 6.1 서버 2개 실행
```
node app.js --port=3000
node app.js --port=3001
```

### 6.2 NGINX 설정

- NGINX
```Nginx
upstream backend {
    server localhost:3000;
    server localhost:3001;
}

server {
    listen 8080;

    location / {
        proxy_pass http://backend;
    }
}
```
### 6.3 테스트

```
curl localhost:8080
```

👉 요청이 번갈아 서버로 전달되는지 확인

---

## 7. 주요 리스크

**1. 세션 관리 실패**
- 서버 간 상태 불일치
- 로그인 유지 실패

**2. DB 병목**
- 서버 수 증가 → DB 부하 증가
**3. Load Balancer 단일 장애**
- LB 다운 시 전체 장애
**4. 캐시 없음**
모든 요청이 서버/DB로 감

---

## 8. 핵심 요약
- 서버는 “강화”가 아니라 “분산”한다
- Stateless 구조 필수
- Load Balancer는 필수 컴포넌트
- Horizontal Scaling이 기본 전략

# 🛠️ GitHub 정리를 위한 심화 섹션: "The Missing Link"

5. Load & Availability: 가용성이 곧 보안이다
- 공격자는 서버를 뚫지 못하면 '눕히려고' 합니다 (DoS/DDoS).
- Rate Limiting (속도 제한): 특정 IP에서 초당 요청 횟수를 제한하여 서버 자원을 보호합니다.
- Circuit Breaker: 특정 모듈이나 DB에 과부하가 걸리면 연결을 잠시 차단해 시스템 전체가 무너지는(Cascading Failure) 것을 방지합니다.
- 로드 테스트의 목적 변경: "내 서버는 얼마나 빠른가?"가 아니라, **"내 서버는 어느 지점에서 무너지는가?"**를 기록하세요.
