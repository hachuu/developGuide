# 날씨 변화 감지 시 Event Grid를 통해 확장성 있는 이벤트 트리거 생성🚀

🛠️ 기능 개요
1. OpenWeather API를 통해 현재 날씨를 확인
2. 이전 상태와 비교하여 비(Rain) 또는 눈(Snow) 변화 감지
3. Azure Event Grid에 이벤트 발행
4. Azure Event Grid의 구독자(Azure Functions, Logic Apps, Event Hubs 등)에서 이벤트 처리

1️⃣ Event Grid 주제(Topic) 생성
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


2️⃣ index.js (Azure Functions 코드 업데이트)
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
3️⃣ function.json (Azure Timer Trigger 설정)
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
4️⃣ 환경 변수 설정 (local.settings.json)
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
5️⃣ Azure Event Grid 구독 설정
- 이제 Event Grid 이벤트를 구독하여 처리할 수 있습니다.
- 예를 들어 Azure Functions에서 Event Grid 이벤트를 처리하려면, 아래와 같이 Event Grid 트리거를 추가하면 됩니다.
```
az eventgrid event-subscription create \
  --name WeatherEventSubscription \
  --source-resource-id "/subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/Microsoft.EventGrid/topics/WeatherEventTopic" \
  --endpoint-type azurefunction \
  --endpoint "/subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/Microsoft.Web/sites/{your-function-app}/functions/{your-eventgrid-function}"
```
🔥 최종 흐름
1. Azure Functions (Timer Trigger) → OpenWeather API 호출
2. 비 또는 눈 감지 시
  - Slack에 메시지 전송
  - Azure Event Grid에 이벤트 발행
3. Azure Event Grid 구독자(Event Grid Trigger, Logic Apps, Event Hubs 등)에서 이벤트 처리
