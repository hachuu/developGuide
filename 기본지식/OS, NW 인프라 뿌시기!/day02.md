# Day 2 - DNS와 연결 흐름 (실무 기준)

## 🎯 목표
- DNS → TCP → TLS → HTTP 흐름을 이해한다
- 각 단계에서 문제가 발생했을 때 위치를 구분할 수 있다

---

# 📌 전체 흐름
도메인 입력
→ DNS (IP 변환)
→ TCP 연결
→ TLS handshake
→ HTTP 요청/응답

---

# 🧠 1. DNS (Domain Name System)

## 정의
> 도메인을 IP 주소로 변환하는 시스템

## 비유
- 도메인 = 이름
- IP = 전화번호
- DNS = 전화번호부

---

## 🧪 실습

### nslookup
nslookup example.com

### dig
dig example.com

### DNS 서버 변경
dig @8.8.8.8 example.com
dig @1.1.1.1 example.com

### 실패 케이스

nslookup wrong-domain-test-123.com


---

## 핵심 개념

### A Record
- 도메인 → IPv4 주소

### TTL
- DNS 캐시 유지 시간

### Resolver
- DNS 요청 주체 (내 PC / 서버)

---

# 🔗 2. DNS 이후 흐름

DNS가 끝나면:


example.com → 104.18.xx.xx
→ 해당 IP로 연결 시도

---

# 🧪 연결 확인 방법

## ping (서버 생존 확인)

ping example.com


## curl (실제 요청)

curl -v https://example.com


## 포트 확인

nc -vz example.com 443


---

# ⚠️ 명령어 차이

| 명령어 | 의미 |
|------|------|
| ping | 서버 살아있나 (ICMP) |
| curl | 실제 서비스 요청 |
| nc | 포트 열려있나 |

---

# 🚨 장애 분석 흐름

## 1. DNS 실패
→ 도메인 문제

---

## 2. DNS OK + ping 실패
→ 네트워크 문제

---

## 3. DNS OK + ping OK + curl 실패
→ TCP / 포트 / TLS 문제

---

# 🔥 핵심 상황

## 상태
- DNS 정상
- ping 정상
- curl 실패

## 의미

서버는 살아있지만
웹 서비스 연결 불가


---

## 원인

### 1. 포트 차단
- 방화벽
- 보안 그룹

### 2. 서버 프로세스 문제
- 웹서버 죽음
- 포트 미오픈

### 3. TLS 문제
- 인증서 오류

---

# 🔐 3. TCP & TLS 이해

## TCP
> 연결 생성 (문 열기)

## TLS
> 신뢰 검증 + 암호화 (신분 확인)

---

## TLS 실패 원인

- 인증서 만료
- 도메인 불일치
- 신뢰되지 않는 인증서

---

## 흐름
TCP 성공 → TLS 시작 → 인증 실패 → 연결 종료


---

# 🌐 4. Cloudflare (CDN)

## 구조


Client → Cloudflare → Origin Server


---

## 캐시 HIT

- Cloudflare가 직접 응답
- origin 서버 안 감

---

## 캐시 MISS

- Cloudflare → origin 요청
- 응답 전달

---

# 🧠 실무 판단 기준

## 성능 문제

| 상황 | 원인 |
|------|------|
| HIT + 느림 | CDN / 네트워크 |
| MISS + 느림 | Origin 서버 |

---

# 🧠 핵심 사고 흐름


DNS → IP 확인
→ TCP 연결 확인
→ TLS 검증
→ HTTP 처리


---

# ✅ 체크리스트

- [ ] DNS 역할 설명 가능
- [ ] DNS 이후 흐름 설명 가능
- [ ] ping vs curl 차이 설명 가능
- [ ] TCP / TLS 차이 이해
- [ ] 장애 위치 구분 가능

---

# 📌 한 줄 정리

> DNS는 시작일 뿐이고, 실제 문제는 TCP/TLS/HTTP 단계에서 발생한다

# 🛠️ GitHub 정리를 위한 심화 섹션: "The Missing Link"

1. DNS & Network: 보이지 않는 위협 탐지
- 도메인을 IP로 바꾸는 과정은 '가로채기'에 취약합니다.

- DNS Spoofing/Poisoning: 공격자가 가짜 IP를 DNS 캐시에 심어 엉뚱한 사이트로 유도하는 기법입니다.
- 대응 기술: * DNSSEC: DNS 응답에 디지털 서명을 추가해 위변조를 방지합니다.
  - DoH (DNS over HTTPS): DNS 쿼리 자체를 암호화하여 중간에 누가 훔쳐보지 못하게 합니다.
- 핵심 개념: "신뢰할 수 있는 이름 해결(Name Resolution)이 모든 보안의 시작이다."
