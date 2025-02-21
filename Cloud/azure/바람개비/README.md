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

## 📂 전체 아키텍처 파일 구조 (Azure Notification Hubs 없는 구조)
```
/weather-alert
 ├── /functions
 │    ├── checkWeather.js   # 날씨 조회 및 이벤트 트리거
 │    ├── sendSlack.js      # Slack 알림 전송
 │    ├── publishEvent.js   # Event Grid 이벤트 발행
 │    ├── getLocations.js   # Cosmos DB에서 위치 조회
 │    ├── handleNotification.js  # Event Grid 이벤트 처리
 ├── index.js               # Azure Functions 엔트리 포인트
 ├── package.json           # 프로젝트 설정 및 의존성 관리
 ├── .env                   # 환경 변수 파일
```

### 1️⃣ checkWeather.js (날씨 조회 및 이벤트 트리거)
```javascript
const axios = require('axios');
const getLocations = require('./getLocations');
const publishToEventGrid = require('./publishEvent');
const sendSlackNotification = require('./sendSlack');

require('dotenv').config();
const OPENWEATHER_API_KEY = process.env.OPENWEATHER_API_KEY;

let lastWeatherStatus = {};

async function getWeather(latitude, longitude) {
    const url = `https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&appid=${OPENWEATHER_API_KEY}&units=metric`;
    const response = await axios.get(url);
    return response.data;
}

async function checkWeather() {
    const locations = await getLocations();
    for (const location of locations) {
        const weatherData = await getWeather(location.latitude, location.longitude);
        const weatherStatus = weatherData.weather[0].main;

        // 이전 상태와 비교하여 변경된 경우 Event Grid에 이벤트 발행
        if (!lastWeatherStatus[location.id] || lastWeatherStatus[location.id] !== weatherStatus) {
            lastWeatherStatus[location.id] = weatherStatus;
            await publishToEventGrid({ location, weatherStatus });
        }

        // 최초 실행 시 Slack 알림 전송
        if (!lastWeatherStatus[location.id]) {
            await sendSlackNotification(`📍 ${location.name} 날씨: ${weatherStatus}`);
        }
    }
}

module.exports = checkWeather;
```

### 2️⃣ sendSlack.js (Slack Webhook을 사용하여 알림 전송)
```javascript
const axios = require('axios');
require('dotenv').config();

const SLACK_WEBHOOK_URL = process.env.SLACK_WEBHOOK_URL;

async function sendSlackNotification(message) {
    try {
        await axios.post(SLACK_WEBHOOK_URL, { text: message });
        console.log("✅ Slack 알림 전송 완료:", message);
    } catch (error) {
        console.error("❌ Slack 알림 전송 실패:", error.message);
    }
}

module.exports = sendSlackNotification;
```
### 3️⃣ publishEvent.js (Event Grid에 이벤트 발행)
```javascript
const axios = require('axios');
require('dotenv').config();

const EVENT_GRID_ENDPOINT = process.env.EVENT_GRID_ENDPOINT;
const EVENT_GRID_KEY = process.env.EVENT_GRID_KEY;

async function publishToEventGrid(eventData) {
    const event = [{
        id: new Date().getTime().toString(),
        subject: `weather/update/${eventData.location.id}`,
        eventType: "WeatherUpdate",
        eventTime: new Date().toISOString(),
        data: eventData,
        dataVersion: "1.0"
    }];

    try {
        await axios.post(EVENT_GRID_ENDPOINT, event, {
            headers: {
                'aeg-sas-key': EVENT_GRID_KEY,
                'Content-Type': 'application/json'
            }
        });
        console.log("✅ Event Grid 이벤트 발행 성공:", eventData);
    } catch (error) {
        console.error("❌ Event Grid 이벤트 발행 실패:", error.message);
    }
}

module.exports = publishToEventGrid;
```
### 4️⃣ getLocations.js (Cosmos DB에서 위치 정보 조회)
```javascript
const { CosmosClient } = require("@azure/cosmos");
require('dotenv').config();

const COSMOS_DB_ENDPOINT = process.env.COSMOS_DB_ENDPOINT;
const COSMOS_DB_KEY = process.env.COSMOS_DB_KEY;
const DATABASE_ID = "WeatherDB";
const CONTAINER_ID = "Locations";

const client = new CosmosClient({ endpoint: COSMOS_DB_ENDPOINT, key: COSMOS_DB_KEY });

async function getLocations() {
    const { resources } = await client.database(DATABASE_ID).container(CONTAINER_ID).items.readAll().fetchAll();
    return resources.map(item => ({
        id: item.id,
        name: item.name,
        latitude: item.latitude,
        longitude: item.longitude
    }));
}

module.exports = getLocations;
```
### 5️⃣ handleNotification.js (Event Grid 이벤트 처리 및 Slack 알림 전송)
```javascript
const sendSlackNotification = require('./sendSlack');

async function handleNotification(event) {
    const eventData = event.data;
    const message = `🔔 날씨 변경 알림!\n📍 ${eventData.location.name} → ${eventData.weatherStatus}`;
    await sendSlackNotification(message);
}

module.exports = handleNotification;
```
### 6️⃣ index.js (Azure Functions 엔트리 포인트 - 타이머 트리거 & HTTP 핸들러 정의)
```javascript
const { app } = require('@azure/functions');
const checkWeather = require('./functions/checkWeather');
const handleNotification = require('./functions/handleNotification');

app.timer('WeatherTimerTrigger', {
    schedule: '0 */10 8-9 * * 1-5',  // 평일 오전 8시~9시 10분 간격 실행
    handler: async () => {
        console.log("🌦️ 날씨 체크 시작...");
        await checkWeather();
    }
});

app.http('WeatherEventHandler', {
    methods: ['POST'],
    authLevel: 'function',
    handler: async (request, context) => {
        const event = await request.json();
        console.log("📩 Event Grid 이벤트 수신:", event);
        await handleNotification(event);
        return { status: 200, body: "Event received successfully!" };
    }
});
```
### ✅ 설정 파일 (.env)
```ini
OPENWEATHER_API_KEY=YOUR_OPENWEATHER_API_KEY
SLACK_WEBHOOK_URL=YOUR_SLACK_WEBHOOK_URL
EVENT_GRID_ENDPOINT=YOUR_EVENT_GRID_ENDPOINT
EVENT_GRID_KEY=YOUR_EVENT_GRID_ACCESS_KEY
COSMOS_DB_ENDPOINT=YOUR_COSMOS_DB_ENDPOINT
COSMOS_DB_KEY=YOUR_COSMOS_DB_KEY
```

## ✨ Notification Hubs 추가 적용 아키텍처
- Event Grid → Notification Hubs → Slack Webhook 형태로 알림이 전송되도록 변경

### 📂 파일 구조
```bash
/weather-alert
 ├── /functions
 │    ├── checkWeather.js   # 날씨 조회 및 이벤트 트리거
 │    ├── sendSlack.js      # Slack Webhook 메시지 전송
 │    ├── publishEvent.js   # Event Grid에 이벤트 발행
 │    ├── getLocations.js   # Cosmos DB에서 위치 정보 조회
 │    ├── handleNotification.js  # Event Grid에서 이벤트 받아 Notification Hubs에 전송
 │    ├── sendNotification.js  # Notification Hubs를 통해 Slack Webhook 호출
 ├── index.js               # Azure Functions 엔트리 포인트 (타이머 트리거 및 HTTP 핸들러 정의)
 ├── package.json           # 프로젝트 설정 및 의존성 관리
 ├── .env                   # 환경 변수 파일
```

### 🔹 1️⃣ sendNotification.js (Azure Notification Hubs로 메시지 전송)
- Notification Hubs를 사용하여 이벤트를 푸시하고, Slack Webhook을 통해 최종 알림을 전송합니다.
```javascript
const { NotificationHubClient } = require("@azure/notification-hubs");
const sendSlackNotification = require("./sendSlack");
require("dotenv").config();

const NOTIFICATION_HUB_CONNECTION_STRING = process.env.NOTIFICATION_HUB_CONNECTION_STRING;
const NOTIFICATION_HUB_NAME = process.env.NOTIFICATION_HUB_NAME;

// Notification Hub 클라이언트 생성
const hubClient = new NotificationHubClient(NOTIFICATION_HUB_CONNECTION_STRING, NOTIFICATION_HUB_NAME);

async function sendNotification(eventData) {
    const message = `🔔 날씨 변경 알림!\n📍 ${eventData.location.name} → ${eventData.weatherStatus}`;

    try {
        // Notification Hubs에 알림 전송
        const response = await hubClient.sendFcmNativeNotification({
            notification: {
                title: "날씨 알림",
                body: message
            }
        });

        console.log("✅ Notification Hubs 푸시 전송 성공:", response);
        await sendSlackNotification(message);  // Slack으로도 알림 전송
    } catch (error) {
        console.error("❌ Notification Hubs 푸시 전송 실패:", error.message);
    }
}

module.exports = sendNotification;
```
### 🔹 2️⃣ handleNotification.js (Event Grid에서 이벤트 받아 Notification Hubs로 전달)
```javascript
const sendNotification = require('./sendNotification');

async function handleNotification(event) {
    const eventData = event.data;
    console.log("📩 Event Grid 이벤트 수신:", eventData);

    // Notification Hubs에 메시지 전송
    await sendNotification(eventData);
}

module.exports = handleNotification;
```
### 🔹 3️⃣ index.js (Azure Functions 엔트리 포인트)
```javascript
const { app } = require('@azure/functions');
const checkWeather = require('./functions/checkWeather');
const handleNotification = require('./functions/handleNotification');

app.timer('WeatherTimerTrigger', {
    schedule: '0 */10 8-9 * * 1-5',  // 평일 오전 8~9시 10분 간격 실행
    handler: async () => {
        console.log("🌦️ 날씨 체크 시작...");
        await checkWeather();
    }
});

app.http('WeatherEventHandler', {
    methods: ['POST'],
    authLevel: 'function',
    handler: async (request, context) => {
        const event = await request.json();
        console.log("📩 Event Grid 이벤트 수신:", event);
        await handleNotification(event);
        return { status: 200, body: "Event received successfully!" };
    }
});
```
### ✅ 환경 변수 설정 (.env)
```ini
OPENWEATHER_API_KEY=YOUR_OPENWEATHER_API_KEY
SLACK_WEBHOOK_URL=YOUR_SLACK_WEBHOOK_URL
EVENT_GRID_ENDPOINT=YOUR_EVENT_GRID_ENDPOINT
EVENT_GRID_KEY=YOUR_EVENT_GRID_ACCESS_KEY
COSMOS_DB_ENDPOINT=YOUR_COSMOS_DB_ENDPOINT
COSMOS_DB_KEY=YOUR_COSMOS_DB_KEY
NOTIFICATION_HUB_CONNECTION_STRING=YOUR_NOTIFICATION_HUB_CONNECTION_STRING
NOTIFICATION_HUB_NAME=YOUR_NOTIFICATION_HUB_NAME
```
### 🚀 실행 및 배포
- .env 파일을 프로젝트 루트에 생성하고 환경 변수를 설정
- 필요한 패키지 설치
```sh
npm install @azure/functions axios dotenv @azure/cosmos @azure/notification-hubs
```
- Azure Functions 로컬 실행
```sh
func start
```
- Azure에 배포
```sh
func azure functionapp publish <YOUR_FUNCTION_APP>
```

---


# Event Grid vs Functions App

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
- 다양한 **트리거(Trigger) 및 바인딩(Binding)** 을 지원하여 자동 실행 가능
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

### 🎯 예제: OpenWeather API와 연동
- ✅ Event Grid 없이 Azure Functions만 사용
  - **Azure Functions(Timer Trigger)** 가 주기적으로 OpenWeather API를 호출하고, 날씨가 바뀌면 Slack Webhook을 호출하여 알림을 보냄
  - 단점: 필요 없는 알림이 전송될 수 있음, 확장성이 떨어짐

- ✅ Event Grid + Azure Functions 조합
  - 1️⃣ Timer Trigger가 OpenWeather API를 호출 → 날씨 변화 감지 시 Event Grid로 이벤트 발행
  - 2️⃣ Event Grid Trigger가 이벤트를 감지하면 Azure Functions가 Slack Webhook을 호출하여 알림 전송
  - 장점: 이벤트가 발생한 경우에만 Slack 알림 전송, 더 효율적인 이벤트 기반 아키텍처 구현 가능

### 🚀 결론
- Event Grid는 이벤트를 전달하는 서비스 (이벤트 브로커 역할)
- Azure Functions는 이벤트를 처리하는 서비스 (이벤트 핸들러 역할)
