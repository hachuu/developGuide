# Day 10:Connection Pool

## 1. Connection Pool이란?
Connection Pool은 **DB 연결을 미리 생성해두고 재사용하는 구조**다.

**잘못된 방식**
```
요청 -> DB 연결 생성 -> 쿼리 -> 연결 종료
```
문제 :
- 매 요청마다 TCP handshake
- 인증 과정 반복
- latency 증가

**올바른 방식**
```
서버 시작 -> DB 연결 여러 개 생성 -> Pool에 저장
요청 -> Pool에서 연결 꺼내 사용 -> 다시 반환
```

## 2. 왜 필요한가?

**성능**
- 연결 생성 비용 제거
- 응답 속도 개선

**안정성**
- DB connection 수 제한 가능
- DB 과부하 방지

**자원 관리**
- 무한 connection 생성 방지

## 3. 동작 구조
<img width="661" height="427" alt="image" src="https://github.com/user-attachments/assets/54567ea3-3fdf-4a41-ab6e-51f89b01e3ba" />

## 4. 핵심 설정값
**max (pool size)**
- 동시에 사용할 수 있는 connection 수

```JavaScript
const pool = new Pool({
  max: 10
});
```

**idle timeout**
- 일정 시간 미사용 시 connection 제거

**connection timeout**
= connection 획득 대기 시간

## 5. Pool이 없을 때 문제
**DB conenction 폭증**
- max_connections 초과 -> 장애
**latency 증가**
- 매 요청마다 handshake
**서버 다운**
- connection leak 발생 시 치명적

## 6. 가장 중요한 개념: "전체 Connection 수"
많이 하는 착각:
| max: 10 이면 DB도 10개만 쓰겠지?
=> 틀림

**실제 공식**
```
전체 DB 연결 수 = 서버 대수 x Node instance 수 (Pm2, cluster) x pool max
```

## 7. 실전 예시
**환경**
```
서버: 2대
PM2 instance: 서버당 4개
pool max: 10
```

## 8. DB 기준으로 pool 설계
**DB 상황**
```
DB max_conenctions = 100
여유 (관리/모니터링 등) = 20
앱 사용 가능 = 80
```
**서버 구성**
```
서버 2대
PM2 instance 4개

총 instance = 8
```

**pool max 계산**
```
80 / 8 = 10
```

**최종 코드**
```JavaScript
const pool = new Pool({
  host: 'db',
  user: 'app',
  password: 'pw',
  database: 'service',
  max: 10
});
```

## 9. 서버 확장 시 위험
**초기 상태**
```
서버 1대
instance 2개
pool 10

=> 20 connections
```

**확장 후**
```
서버 4대
instance 4개
pool 10

=> 160 connections
```
=> DB 터질 수 있음

## 10. Node 기준 구조
```
Node process 1개 = pool 1개
```
=> 따라서
```
전체 connection = 서버 수 x PM2 instance 수 x pool max
```

## 11. 절대 하면 안되는 패턴
**요청마다 pool 생성**
```JavaScript
app.get('/', () => {
  const pool = new Pool({ max: 10 });
});
```
=> 요청마다 DB 연결 생성 -> 장애

**올바른 패턴**
```JavaScript
const pool = new Pool({ max: 10 });

app.get('/', async (req, res) => {
  const result = await pool.query('SELECT 1');
  res.send(result.rows);
});
```

## 12. Connection Leak (치명적 문제)
**문제 상황**
- connection 반환 안 함
- pool 점점 고갈

**결과**
```
새 요청 -> connection 없음 -> 대기 -> 장애
```

## 13. Timeout과의 관계
timeout 없으면:
- connection 계속 점유
- pool 고갈
결과:
```
서비스 전체 지연 -> 장애
```

## 14. 실무 체크리스트
- ✔ pool max는 “전체 기준”으로 계산했는가
- ✔ DB max_connections 고려했는가
- ✔ 서버 확장 시 connection 증가 계산했는가
- ✔ connection leak 방지했는가
- ✔ timeout 설정했는가

## 15. 핵심 요약
```
1. DB 연결 생성은 비용이 크다
2. 그래서 connection pool로 재사용한다
3. pool max는 전체 시스템 기준으로 계산해야 한다
4. scale-out 시 connection 폭증을 항상 고려해야 한다
5. connection leak + timeout 미설정은 장애의 핵심 원인이다
```
