# 실시간 날씨 알림 서비스 (Slack Push)
## 🛠 아키텍처 구성
- 사용자가 원하는 지역을 등록 (ex: 서울, 뉴욕, 도쿄)
- Azure Functions가 OpenWeather API에서 날씨 정보 조회
- 날씨 변화 감지 시 Azure Event Grid를 통해 이벤트 트리거
- Azure Notification Hubs를 통해 Slack으로 푸시 알림 전송
## ⚙️ 기술 스택
- Backend: Azure Functions (Node.js or Python)
- Database: Azure Cosmos DB (사용자가 등록한 지역 저장)
- API 연동: OpenWeather API (날씨 데이터 조회)
- Event Processing: Azure Event Grid (날씨 변화 감지)
- Notification: Azure Notification Hubs → Slack Webhook



## 1. 🔹 [Azure Event Grid](https://github.com/hachuu/developGuide/blob/main/Cloud/%EB%B0%94%EB%9E%8C%EA%B0%9C%EB%B9%84/event%20grid.md)
### ✅ 역할: 이벤트 라우팅 서비스

- 이벤트를 수집하고 배포하는 서비스
- Publisher(이벤트를 보내는 서비스)와 Subscriber(이벤트를 받는 서비스) 간의 이벤트 전달 역할 수행
- 여러 Azure 서비스(Azure Storage, Azure Event Hub, Azure Functions 등) 또는 타사 서비스와 연동 가능
- Push 방식(이벤트 발생 시 자동 전달)으로 동작

### 🛠️ 주요 기능

- 이벤트 소스(Event Publisher): 이벤트를 생성하는 서비스 (예: Azure Blob Storage, Custom App 등)
- 이벤트 핸들러(Event Subscriber): 이벤트를 처리하는 서비스 (예: Azure Functions, Logic Apps 등)
- Topic & Subscription 모델 사용
- 1:N 이벤트 전달 가능 (하나의 이벤트를 여러 개의 Subscriber에게 전달 가능)

### 💡 언제 사용할까?

- 특정 이벤트 발생 시 다른 서비스나 애플리케이션을 자동으로 트리거하고 싶을 때
- 여러 개의 소비자(Subscriber)에게 동일한 이벤트를 전달해야 할 때
- 클라우드 네이티브 애플리케이션에서 이벤트 기반 아키텍처를 구축할 때

## 2. 🔹 [Azure Functions](https://github.com/hachuu/developGuide/blob/main/Cloud/%EB%B0%94%EB%9E%8C%EA%B0%9C%EB%B9%84/functions%20app.md)

### ✅ 역할: 서버리스 컴퓨팅 플랫폼

- 이벤트 기반으로 코드를 실행하는 서비스
- 다양한 **트리거(Trigger) 및 바인딩(Binding)**을 지원하여 자동 실행 가능
- 필요할 때만 실행되므로 비용 절감 가능 (서버리스 구조)
- 이벤트 핸들러 역할을 수행할 수 있음 (Event Grid, Queue, Timer, HTTP 요청 등 트리거 가능)

### 🛠️ 주요 기능

- 다양한 트리거(Trigger) 지원: Timer, HTTP, Event Grid, Blob Storage 등
- 서버 관리 불필요: 코드만 작성하면 자동 실행
- 자동 스케일링: 트래픽 증가 시 인스턴스가 자동으로 확장
- 다양한 언어 지원: Node.js, Python, C#, Java 등

### 💡 언제 사용할까?

- 특정 이벤트(파일 업로드, 데이터 변경, HTTP 요청 등)가 발생하면 자동으로 코드 실행이 필요할 때
- 서버를 관리하지 않고 클라우드에서 동적으로 확장되는 코드 실행이 필요할 때
- 특정 API를 만들어 특정 이벤트에 반응해야 할 때

## 📌 주요 차이점 정리
### Azure Event Grid vs Azure Functions 차이점
|  | **Azure Event Grid** | **Azure Functions** |
|---|---|---|
| **역할** | 이벤트 **라우팅 및 배포** | 이벤트 **처리 및 실행** |
| **동작 방식** | 이벤트를 **발행(Publish) 및 구독(Subscribe)** | 트리거(Trigger)에 의해 **코드 실행** |
| **사용 예시** | 여러 개의 서비스에 **이벤트 전달** | 이벤트 발생 시 **코드 실행** (Slack 알림 전송, 데이터 처리 등) |
| **트리거 방식** | **Push 방식** (이벤트가 발생하면 자동 전달) | 다양한 트리거 지원 (Timer, Event Grid, HTTP 등) |
| **확장성** | **1:N 이벤트 전달** 가능 (하나의 이벤트를 여러 곳에 전달) | 코드 실행 수요에 따라 자동 확장 |
| **사용 요금** | 이벤트 수에 따라 과금 (`per event`) | 실행 시간과 사용량에 따라 과금 (`pay-per-execution`) |



## 🎯 예제: OpenWeather API와 연동
### ✅ Event Grid 없이 Azure Functions만 사용
- **Azure Functions(Timer Trigger)**가 주기적으로 OpenWeather API를 호출하고, 날씨가 바뀌면 Slack Webhook을 호출하여 알림을 보냄
- 단점: 필요 없는 알림이 전송될 수 있음, 확장성이 떨어짐

### ✅ Event Grid + Azure Functions 조합
- 1️⃣ Timer Trigger가 OpenWeather API를 호출 → 날씨 변화 감지 시 Event Grid로 이벤트 발행
- 2️⃣ Event Grid Trigger가 이벤트를 감지하면 Azure Functions가 Slack Webhook을 호출하여 알림 전송
- 장점: 이벤트가 발생한 경우에만 Slack 알림 전송, 더 효율적인 이벤트 기반 아키텍처 구현 가능

## 🚀 결론
- Event Grid는 이벤트를 전달하는 서비스 (이벤트 브로커 역할)
- Azure Functions는 이벤트를 처리하는 서비스 (이벤트 핸들러 역할)
