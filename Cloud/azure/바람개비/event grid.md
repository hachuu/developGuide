# 날씨 변화 감지 시 Event Grid를 통해 확장성 있는 이벤트 트리거 생성🚀

## 🛠️ 기능 개요
1. OpenWeather API를 통해 현재 날씨를 확인
2. 이전 상태와 비교하여 비(Rain) 또는 눈(Snow) 변화 감지
3. Azure Event Grid에 이벤트 발행
4. Azure Event Grid의 구독자(Azure Functions, Logic Apps, Event Hubs 등)에서 이벤트 처리

### 1️⃣ Event Grid 주제(Topic) 생성
- Azure CLI를 사용하여 Event Grid 주제를 생성하세요.
- endpoint와 key1 값을 환경 변수로 설정해야 합니다.
```
az eventgrid topic create --name WeatherEventTopic --location eastus --resource-group YourResourceGroup
```
- Event Grid 주제의 끝점 가져오기
```
az eventgrid topic show --name WeatherEventTopic --resource-group YourResourceGroup --query "endpoint" --output tsv
```
- Event Grid 액세스 키 가져오기
```
az eventgrid topic key list --name WeatherEventTopic --resource-group YourResourceGroup --query "key1" --output tsv
```


### 2️⃣ index.js (Azure Functions 코드 업데이트)
- 이제 Azure Event Grid에 이벤트를 발행하도록 기존 함수를 업데이트합니다.

```javascript
const axios = require("axios");
require("dotenv").config();

const OPENWEATHER_API_KEY = process.env.OPENWEATHER_API_KEY;
const SLACK_WEBHOOK_URL = process.env.SLACK_WEBHOOK_URL;
const EVENT_GRID_TOPIC_ENDPOINT = process.env.EVENT_GRID_TOPIC_ENDPOINT;
const EVENT_GRID_ACCESS_KEY = process.env.EVENT_GRID_ACCESS_KEY;

const CITY = "Seoul";
let previousWeather = null; // 이전 날씨 상태 저장

async function getWeather() {
    try {
        const url = `http://api.openweathermap.org/data/2.5/weather?q=${CITY}&appid=${OPENWEATHER_API_KEY}&units=metric`;
        const response = await axios.get(url);
        return response.data;
    } catch (error) {
        console.error("OpenWeather API 요청 실패:", error.message);
        return null;
    }
}

async function sendSlackNotification(message) {
    try {
        await axios.post(SLACK_WEBHOOK_URL, { text: message });
        console.log("Slack 알림 전송 성공");
    } catch (error) {
        console.error("Slack 알림 전송 실패:", error.message);
    }
}

async function publishToEventGrid(eventType, data) {
    const event = [
        {
            id: new Date().getTime().toString(),
            eventType: eventType,
            subject: "weather/change",
            eventTime: new Date().toISOString(),
            dataVersion: "1.0",
            data: data
        }
    ];

    try {
        await axios.post(EVENT_GRID_TOPIC_ENDPOINT, event, {
            headers: {
                "Content-Type": "application/json",
                "aeg-sas-key": EVENT_GRID_ACCESS_KEY
            }
        });
        console.log("Event Grid 이벤트 발행 성공:", eventType);
    } catch (error) {
        console.error("Event Grid 이벤트 발행 실패:", error.message);
    }
}

module.exports = async function (context, myTimer) {
    context.log("Azure Function 실행: 날씨 확인 중...");

    const weatherData = await getWeather();
    if (!weatherData) return;

    const weatherConditions = weatherData.weather[0].main;
    const temp = weatherData.main.temp;
    const cityName = weatherData.name;

    // 날씨 변화 감지 (비 또는 눈이 새롭게 발생하거나 멈췄을 때)
    if (previousWeather !== weatherConditions && (weatherConditions === "Rain" || weatherConditions === "Snow")) {
        const message = `🚨 ${cityName}에서 ${weatherConditions}이(가) 감지되었습니다! 현재 온도: ${temp}°C 🌡️`;
        await sendSlackNotification(message);

        // Event Grid로 이벤트 발행
        await publishToEventGrid("Weather.Alert", {
            city: cityName,
            condition: weatherConditions,
            temperature: temp
        });
    }

    // 이전 상태 업데이트
    previousWeather = weatherConditions;
};
```

### 3️⃣ function.json (Azure Timer Trigger 설정)
- 기존과 동일하게 5분마다 실행되도록 설정합니다.

```json
{
  "bindings": [
    {
      "name": "myTimer",
      "type": "timerTrigger",
      "direction": "in",
      "schedule": "0 */5 * * * *"
    }
  ]
}
```

### 4️⃣ 환경 변수 설정 (local.settings.json)
- Azure Functions의 환경 변수(Application Settings)에서 Event Grid 설정 추가하세요.

```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "OPENWEATHER_API_KEY": "여기에_당신의_API_키",
    "SLACK_WEBHOOK_URL": "여기에_당신의_Slack_Webhook_URL",
    "EVENT_GRID_TOPIC_ENDPOINT": "여기에_당신의_Event_Grid_주제_엔드포인트",
    "EVENT_GRID_ACCESS_KEY": "여기에_당신의_Event_Grid_액세스_키"
  }
}
```

### 5️⃣ Azure Event Grid 구독 설정
- 이제 Event Grid 이벤트를 구독하여 처리할 수 있습니다.
- 예를 들어 Azure Functions에서 Event Grid 이벤트를 처리하려면, 아래와 같이 Event Grid 트리거를 추가하면 됩니다.
```
az eventgrid event-subscription create \
  --name WeatherEventSubscription \
  --source-resource-id "/subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/Microsoft.EventGrid/topics/WeatherEventTopic" \
  --endpoint-type azurefunction \
  --endpoint "/subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/Microsoft.Web/sites/{your-function-app}/functions/{your-eventgrid-function}"
```

## 🔥 최종 흐름
1. Azure Functions (Timer Trigger) → OpenWeather API 호출
2. 비 또는 눈 감지 시
  - Slack에 메시지 전송
  - Azure Event Grid에 이벤트 발행
3. Azure Event Grid 구독자(Event Grid Trigger, Logic Apps, Event Hubs 등)에서 이벤트 처리

---

# Event Grid 필터링
- Azure **Event Grid 필터링(Event Filtering)**은 이벤트를 특정 조건에 맞는 경우에만 처리하도록 설정하는 기능
- 즉, 불필요한 이벤트를 걸러내서 비용 절감과 성능 최적화할 수 있음

## Event Grid 필터링이 필요한 이유
- 예시
```
✅ "맑음 → 비" 변화하면 Slack 알림 보내야 함
❌ "맑음 → 맑음" 같은 경우엔 알림을 보낼 필요 없음
👉 필터링을 적용하면 중복된 이벤트를 걸러내서 비용을 아낄 수 있음
```
## Event Grid 필터링 방식

### 1️⃣ 기본 속성 필터링 (Property Filtering)
- 이벤트 데이터에서 특정 필드 값을 기준으로 필터링
- 예를 들어, "비가 오거나 눈이 올 때만 이벤트를 처리"할 수 있음
```json
{
  "filter": {
    "subjectBeginsWith": "/weather/",
    "data": {
      "weather": {
        "in": ["Rain", "Snow"]
      }
    }
  }
}
```
- 🔹 설명:
    - subjectBeginsWith: "/weather/" → "weather"와 관련된 이벤트만 필터링
    - data.weather.in: ["Rain", "Snow"] → "비" 또는 "눈"이 포함된 이벤트만 처리
### 2️⃣ 고급 필터링 (Advanced Filtering)
- 숫자, 문자열, 존재 여부 같은 조건으로 필터링 가능
- 예를 들어, 강수량이 5mm 이상일 때만 알림을 보내려면?

```json
{
  "filter": {
    "data.precipitation": {
      "greaterThanOrEquals": 5
    }
  }
}
```
- 🔹 설명:
    - data.precipitation 값이 5mm 이상일 경우만 이벤트를 트리거함

### 3️⃣ Event Grid 구독 필터링 (Event Subscription Filtering)
- 특정 구독(Event Subscription)에 필터링 규칙을 추가해서 불필요한 이벤트를 받지 않도록 설정 가능
```
az eventgrid event-subscription create \
  --name WeatherAlertSubscription \
  --source-resource-id /subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/Microsoft.EventGrid/topics/{event-grid-topic} \
  --endpoint /subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/Microsoft.Web/sites/{function-app} \
  --advanced-filter data.weather StringIn 'Rain' 'Snow'
```
- 🔹 설명:
    - StringIn 'Rain' 'Snow' → "비" 또는 "눈"이 올 때만 이벤트 구독

## 📌 결론: 필터링을 활용한 최적화 전략

---
# 이미 생성된 Azure Functions App에 Event Grid 추가하기
- 부제 : 현재 Timer Trigger로 동작하는 WeatherCheckFunction이 있는 상태에서 Event Grid를 연동하는 방법

## ✅ 1. Event Grid 트리거 추가 (CLI 명령어)
- 먼저, Event Grid 트리거를 새로운 함수로 추가
- EventGridHandler/ 폴더가 생성되면서 Event Grid 트리거가 포함된 새로운 함수가 만들어짐
```sh
func new --name EventGridHandler --template "Azure Event Grid trigger"
```
- func new --name EventGridHandler --template "Event Grid trigger" error 처리
  1. powershell에서 'npm update -g azure-functions-core-tools@4 --unsafe-perm true' 명령어 실행
  2. func --version 확인 후 최신버전인지 확인필요
  3. func templates list로 template 네이밍 확인 필요
  ```sh
  func new --name EventGridHandler --template "Azure Event Grid trigger"
    Use the up/down arrow keys to select a template:Event Grid trigger
    Can't find template "Event Grid trigger" in "javascript"
  ```


## ✅ 2. 새로 생성된 함수의 구조
- 새로 생성된 EventGridHandler/ 폴더 안의 구조
```pgsql
EventGridHandler/
│── function.json       # 트리거 및 바인딩 설정 파일
│── index.js            # 이벤트를 처리하는 코드
📌 index.js (기본 코드)
```

```javascript
module.exports = async function (context, eventGridEvent) {
    context.log("Event Grid event received: ", eventGridEvent);

    // 이벤트 데이터 추출
    const eventData = eventGridEvent.data;
    context.log("Event Data: ", JSON.stringify(eventData));

    // 필요한 작업 수행
};
```
- eventGridEvent → Event Grid에서 수신한 이벤트 데이터를 담고 있어요.
- context.log(...) → 이벤트 로그를 출력하는 코드.
## ✅ 3. function.json (Event Grid 트리거 설정)
- 함수 생성 시 자동으로 function.json 파일이 생성

```json
{
  "bindings": [
    {
      "type": "eventGridTrigger",
      "direction": "in",
      "name": "eventGridEvent"
    }
  ]
}
```
- type: "eventGridTrigger" → Event Grid에서 발생한 이벤트를 수신하는 트리거
- name: "eventGridEvent" → index.js에서 사용할 이벤트 객체 이름
## ✅ 4. Event Grid가 Azure Functions에 이벤트를 보낼 수 있도록 권한 부여
- Event Grid가 Azure Functions를 호출할 수 있도록 권한을 설정

### ① Azure CLI로 Event Grid 구독 생성
- Azure CLI를 사용해서 Event Grid 구독을 추가
- 특정 이벤트가 발생할 때 Event Grid가 Azure Functions로 이벤트를 전송할 수 있게 됨
```sh
az eventgrid event-subscription create \
  --name MyEventGridSubscription \
  --source-resource-id /subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/Microsoft.Storage/storageAccounts/{storage-account} \
  --endpoint https://{your-function-app-name}.azurewebsites.net/runtime/webhooks/eventgrid?functionName=EventGridHandler \
  --included-event-types Microsoft.Storage.BlobCreated Microsoft.Storage.BlobDeleted
```
- 🔹 {your-function-app-name}: Azure Functions App 이름
- 🔹 {resource-group}: 리소스 그룹 이름
- 🔹 {subscription-id}: Azure Subscription ID
- 🔹 {storage-account}: Event Grid를 구독할 대상 리소스 (예: Storage Account)

## ✅ 5. 로컬 테스트 (Event Grid 이벤트 모의 전송)
- Azure에서 Event Grid 트리거를 실제로 테스트하려면, Event Grid에 직접 이벤트를 보낼 수도 있음.
- 실제 테스트 이벤트를 보내는 명령어
```sh
curl -X POST -H "Content-Type: application/json" \
     -d '[{
           "id": "1234567890",
           "eventType": "Microsoft.Storage.BlobCreated",
           "subject": "/blobServices/default/containers/my-container/blobs/myfile.txt",
           "eventTime": "2024-03-04T12:00:00Z",
           "data": {
               "api": "PutBlob",
               "clientRequestId": "1234",
               "requestId": "5678",
               "eTag": "0x8D4BCC2E4835CD0",
               "contentType": "text/plain",
               "contentLength": 524288
           },
           "dataVersion": "2.0",
           "metadataVersion": "1"
     }]' \
     http://localhost:7071/runtime/webhooks/eventgrid?functionName=EventGridHandler
```
- 🚀 Event Grid 트리거가 정상적으로 작동하는지 확인할 수 있음

## 🎯 정리
- Event Grid 트리거 추가
```sh
func new --name EventGridHandler --template "Event Grid trigger"
```
- index.js에서 이벤트 처리 코드 작성
- Event Grid 트리거 설정 확인 (function.json)
- Azure CLI로 Event Grid와 Functions 연동
- 로컬에서 curl로 테스트 이벤트 전송
