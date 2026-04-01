
# 📌 Day 1: HTTP 요청 구조 이해

## 🎯 목표
- HTTP 요청/응답 구조를 직접 확인한다
- curl을 사용해 요청을 보낸다
- Header / Body 역할을 구분한다

---

## 📖 핵심 개념 (최소)

HTTP = 텍스트 기반 프로토콜

구성 요소:

- Method: GET / POST
- Header: 메타정보
- Body: 실제 데이터

---

## 🧪 실습

### 1. GET 요청 보내기

```bash
curl -v https://example.com
```

확인 포인트
> GET / HTTP/1.1 (요청)
< HTTP/1.1 200 OK (응답)
2. 헤더 확인

요청 헤더:

Host:
User-Agent:
Accept:

응답 헤더:

Content-Type:
Content-Length:
3. POST 요청 보내기
curl -v -X POST https://httpbin.org/post \
  -H "Content-Type: application/json" \
  -d '{"name":"test"}'
확인 포인트
Body(JSON)가 서버로 전달되는지 확인
4. 실패 케이스 확인
curl -v https://wrong.domain.test
확인 포인트
요청 실패 이유 분석 (DNS / 네트워크)
✅ 오늘 체크리스트

아래를 설명할 수 있어야 함:

 GET vs POST 차이
 Header 역할
 Body가 필요한 이유
 curl -v 옵션 의미
🤔 사고 질문
브라우저 없이 요청 보내도 서버는 왜 응답할까?
Content-Length 없으면 어떻게 될까?
서버는 왜 User-Agent를 받을까?
🔁 복습 방법 (15분)

노트 보지 말고 말로 설명:

"HTTP 요청은 이런 구조로 만들어지고, 서버는 이렇게 응답한다"

⚠️ 오늘의 리스크
1. "HTTP 아는 것 같다" 착각

→ 실제 요청 구조를 본 적 없으면 모르는 상태

2. 결과만 보고 넘어감

→ 반드시 요청/응답 구조 분석

3. POST를 외움

→ 왜 Body가 필요한지 이해해야 함

---


```
songhayeong@hachuui-MacBookPro ~ % curl -v https://example.com
* Host example.com:443 was resolved.
* IPv6: (none)
* IPv4: 104.18.26.120, 104.18.27.120
*   Trying 104.18.26.120:443...
* Connected to example.com (104.18.26.120) port 443
* ALPN: curl offers h2,http/1.1
* (304) (OUT), TLS handshake, Client hello (1):
*  CAfile: /etc/ssl/cert.pem
*  CApath: none
* (304) (IN), TLS handshake, Server hello (2):
* (304) (IN), TLS handshake, Unknown (8):
* (304) (IN), TLS handshake, Certificate (11):
* (304) (IN), TLS handshake, CERT verify (15):
* (304) (IN), TLS handshake, Finished (20):
* (304) (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / AEAD-CHACHA20-POLY1305-SHA256 / [blank] / UNDEF
* ALPN: server accepted h2
* Server certificate:
*  subject: CN=example.com
*  start date: Feb 13 18:53:48 2026 GMT
*  expire date: May 14 18:57:50 2026 GMT
*  subjectAltName: host "example.com" matched cert's "example.com"
*  issuer: C=US; O=SSL Corporation; CN=Cloudflare TLS Issuing ECC CA 3
*  SSL certificate verify ok.
* using HTTP/2
* [HTTP/2] [1] OPENED stream for https://example.com/
* [HTTP/2] [1] [:method: GET]
* [HTTP/2] [1] [:scheme: https]
* [HTTP/2] [1] [:authority: example.com]
* [HTTP/2] [1] [:path: /]
* [HTTP/2] [1] [user-agent: curl/8.7.1]
* [HTTP/2] [1] [accept: */*]
> GET / HTTP/2
> Host: example.com
> User-Agent: curl/8.7.1
> Accept: */*
> 
* Request completely sent off
< HTTP/2 200 
< date: Wed, 01 Apr 2026 12:13:17 GMT
< content-type: text/html
< server: cloudflare
< last-modified: Tue, 24 Mar 2026 22:06:31 GMT
< allow: GET, HEAD
< accept-ranges: bytes
< age: 10449
< cf-cache-status: HIT
< cf-ray: 9e5781ca9adf3109-ICN
< 
<!doctype html><html lang="en"><head><title>Example Domain</title><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{background:#eee;width:60vw;margin:15vh auto;font-family:system-ui,sans-serif}h1{font-size:1.5em}div{opacity:0.8}a:link,a:visited{color:#348}</style></head><body><div><h1>Example Domain</h1><p>This domain is for use in documentation examples without needing permission. Avoid use in operations.</p><p><a href="https://iana.org/domains/example">Learn more</a></p></div></body></html>
* Connection #0 to host example.com left intact
```


# Day 1 - HTTP 요청 분석 (curl 실습 기반)

## 🎯 목표
- 실제 HTTP 요청 흐름을 단계별로 이해한다
- curl 로그를 해석할 수 있다
- 요청이 어디서 처리되는지 추론할 수 있다

---

# 📌 전체 흐름 요약

요청은 다음 순서로 진행된다:

> DNS → TCP → TLS → HTTP → Response

---

# 🔍 단계별 분석

## 1. DNS (도메인 → IP)

```bash
* Host example.com:443 was resolved.
* IPv4: 104.18.26.120, 104.18.27.120
```

- 의미
  - 도메인이 IP 주소로 변환됨
  - IP가 2개 → 로드밸런싱 또는 CDN 사용
2. TCP 연결
* Trying 104.18.26.120:443...
* Connected to example.com (104.18.26.120) port 443
- 의미
  - 서버와 연결 성공
  - 443 포트 → HTTPS 사용
- 실패 시 의미
  - 네트워크 문제
  - 방화벽 차단
  - 서버 다운
3. TLS Handshake (HTTPS 핵심)
* TLS handshake, Client hello
* TLS handshake, Server hello
* Certificate
- 의미
  - 암호화 통신을 위한 연결 수립 과정
* SSL connection using TLSv1.3
- 최신 TLS 버전 사용
인증서 검증
* subject: CN=example.com
* issuer: Cloudflare TLS Issuing ECC CA 3
* SSL certificate verify ok.
- 의미
  - 서버가 실제 example.com인지 확인
  - 신뢰된 인증기관(CA) 확인
4. HTTP/2 협상
* ALPN: server accepted h2
* using HTTP/2
- 의미
  - HTTP/2 사용
- 특징
  - 멀티플렉싱 (여러 요청 동시 처리)
  - 성능 향상
5. 실제 요청
> GET / HTTP/2
> Host: example.com
> User-Agent: curl/8.7.1
> Accept: */*
- 의미
  - 클라이언트가 서버로 보낸 실제 요청

- 구성 요소

| 항목         | 의미        |
| ---------- | --------- |
| GET        | 읽기 요청     |
| /          | 루트 경로     |
| Host       | 대상 서버     |
| User-Agent | 클라이언트 정보  |
| Accept     | 받을 데이터 타입 |



6. 응답
< HTTP/2 200
< content-type: text/html
< server: cloudflare
- 의미
  - 200 → 성공
  - HTML 반환
  - Cloudflare 서버에서 응답
7. 캐시 상태 (실무 핵심)
< cf-cache-status: HIT
< age: 10449
- 의미
  - HIT → 캐시에서 응답
  - age → 캐시된 시간 (초)
- 해석
  - 실제 origin 서버까지 요청이 가지 않았을 가능성 있음

🧠 실무 관점 해석
1. 구조
- Client → Cloudflare(CDN) → Origin Server
2. 성능이 빠른 이유
- CDN 사용
- 캐시 HIT
- HTTP/2 사용
3. 장애 발생 위치 추적 기준
  
| 구간   | 문제 유형     |
| ---- | --------- |
| DNS  | 도메인 해석 실패 |
| TCP  | 연결 실패     |
| TLS  | 인증서 오류    |
| HTTP | 4xx / 5xx |
| CDN  | 캐시 문제     |

✅ 오늘 체크리스트

- 다음 질문에 답할 수 있어야 한다:
```
 IP가 여러 개인 이유
 TLS handshake가 필요한 이유
 HTTP/2의 특징 (한 줄 설명)
 cf-cache-status: HIT 의미
 요청이 origin 서버까지 갔는지 여부
```
 
🧪 추가 실습
1. HTTP/1.1 강제
```
curl -v --http1.1 https://example.com
```

→ HTTP/2와 비교

2. 헤더만 확인
curl -I https://example.com
3. 캐시 우회
curl -H "Cache-Control: no-cache" -v https://example.com

→ cf-cache-status 변화 확인

📌 한 줄 정리

HTTP 요청은 DNS → TCP → TLS → HTTP 흐름 위에서 동작한다
