# Azure Networking Basics
- Azure 핵심 네트워크 인프라 정리

## 1. Azure Networking 전체 개념 지도
- Azure에서 VM/PaaS가 외부와 통신하려면 아래 흐름을 반드시 거친다.
- ```vbnet
  🌍 Internet
      ↓
  🔹 Public IP
        ↓
  🛡️ NSG (Inbound Rule 체크)
        ↓
  🔗 NIC (Private IP + Subnet + NSG 적용)
        ↓
  🏙️ VNet / Subnet
        ↓
  🖥️ VM / App / Function / Container

  ```

## 2. NSG (Network Security Group)
- **Azure의 방화벽** : 포트·IP·프로토콜 기반으로 접근을 허용/차단하는 보안 정책

### NSG 핵심 요약
|항목           |설명                                      |
|---------------|------------------------------------------|
|역할           |포트 및 IP 기반 접근 제어(방화벽)            |
|적용 위치      |Subnet, NIC                               |
|규칙 종류      |Inbound, Outbound                          |
|우선순위       |숫자가 낮을수록 먼저 실행                    |
|트러블슈팅 핵심 |Subnet NSG + NIC NSG 중 하나라도 Deny면 차단|

### NSG 관련 구조 3가지
1. NSG 없는 단순 구조
  ```vbnet
  🌍 Internet
     ↓
  🔹 Public IP
     ↓
  🖥️ VM:8080
  ```

2. NSG가 요청을 필터링하는 구조
  ```yaml
  🌍 Internet
      ↓
  🔹 Public IP
      ↓
  ┌─────────────────────────────────┐
  │  🛡️ NSG : 8080 허용 여부 체크    │
  └─────────────────────────────────┘
      ↓
  🖥️ VM:8080
  ```

3. Subnet NSG + NIC NSG 이중 방어
  ```objectivec
  🌍 Internet
      ↓
  🔹 Public IP
      ↓
  🛡️ Subnet NSG
      ↓
  🛡️ NIC NSG
      ↓
  🖥️ VM
  ```

## 3. NIC (Network Interface Card)
- **VM의 네트워크 카드** : 모든 네트워크 정보(Private IP, Subnet, NSG)가 NIC에 붙어 있다.

### NIC 핵심 요약
|항목            |설명                                                 |
|---------------|------------------------------------------------------|
|Private IP     |VNet/Subnet 내부 주소                                  |
|Public IP 연결 |가능 (권장 X)                                          |
|연결 위치       |Subnet                                                |
|주의점          |NIC에 붙은 NSG가 가장 직접적으로 트래픽을 필터링         |

### NIC 관련 구성
1. NIC 구성 요소
  ```objectivec
  🖥️ VM
     │
  🔗 NIC
   ├── 📮 Private IP
   ├── 🏙️ Subnet
   └── 🛡️ NSG
  ```

2. NIC이 흐름에서 차지하는 위치
  ```objectivec
  🌍 Internet
      ↓
  🔹 Public IP
      ↓
  🔗 NIC (IP/NSG/Subnet 판정)
      ↓
  🖥️ VM
  ```

3. Subnet NSG + NIC NSG 조합
  ```objectivec
  🛡️ Subnet NSG
        ↓
  🛡️ NIC NSG
        ↓
  🖥️ VM
  ```

## 4. NAT (Network Address Translation)
- **Public ↔ Private IP를 변환해주는 네트워크 변환기**

### NAT 핵심 요약
|종류     |설명                                                 |
|---------|------------------------------------------------------|
|SNAT     |VM → Internet 나갈 때 Private IP → Public IP          |
|DNAT     |Internet → VM 접근 시 Public IP → Private IP          |
|사용처    |Load Balancer 포트 매핑, VM outbound                  |

### NAT 관련 구조
1. SNAT - Private → Public
  ```
  🖥️ VM:10.0.0.4
        ↓
  🔄 NAT (10.0.0.4 → 203.x.x.x)
        ↓
  🌍 Internet
  ```

2. DNAT - Public → Private (포트 매핑 포함)
  ```
  🌍 Internet:203.x.x.x:9090
          ↓
  🔄 NAT (9090→8080 / 203.x → 10.0.0.4)
          ↓
  🖥️ VM:10.0.0.4:8080
  ```

3. Load Balancer NAT 구조
  ```
  🌍 Internet
        ↓
  🔄 Load Balancer (DNAT/SNAT)
        ↓                ↓
  🖥️ VM1:10.0.1.4   🖥️ VM2:10.0.1.5
  ```

## 5. VNet & Subnet
- VNet (Virtual Network)
  - Azure 내부의 독립 네트워크, 공간
  - 회사 LAN 같은 역할
- Subnet
  - VNet을 역할별로 분리한 네트워크
  - 아파트 동 개념
---
- VNet = 아파트 단지
- Subnet = 아파트 동
- Private IP = 각 세대호수
---

## 6. Public IP & Private IP
- Public IP
  - 인터넷 어디서든 접근 가능
  - 매우 위험 → NSG & LB로 보호 필요
  - VM에 직접 붙이는 것 비권장
- Private IP
  - VNet/Subnet 내부 통신용
  - DB/Redis 등은 반드시 Private IP만 사용
 
## 7. 전체 구조 통합도 (Full Flow)
```
🌍 Internet
    ↓
🔹 Public IP
    ↓
🛡️ NSG (Inbound Rule)
    ↓
🔗 NIC
    ├── Private IP
    ├── Subnet
    └── NSG
    ↓
🏙️ VNet/Subnet
    ↓
🖥️ VM / App / API / Agent
```

## 8. Troubleshooting 체크리스트
|체크               |설명                                                   |
|-------------------|-------------------------------------------------------|
|NSG Inbound 규칙   |해당 포트 허용?                                         |
|NIC NSG            |Subnet보다 NIC NSG 우선 적용됨                          |
|Public IP 연결 여부 |실제로 붙어있는지 확인                                  |
|Load Balancer 규칙 |Health Probe / NAT 룰                                  |
|OS 방화벽          |ufw / firewalld                                        |
|VM 내부 테스트      |curl localhost:8080                                   |
|Subnet 구조        |Dev와 Stg/Prd가 다르게 구성됨                           |
|Route Table        |특수 환경에서는 RT에 막힐 수 있음                        |
