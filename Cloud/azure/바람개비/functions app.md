# [VS Code] 로컬 환경에서 functions app 실행하기

## 아키텍처 구성
- functions app에서 주기적으로 OpenWeather API를 호출하고, 날씨가 바뀌면 Slack Webhook을 호출하여 알림을 보냄

## 0. 사전 준비
- vscode 환경
  - extensions 설치 : Azure Functions Extension, Azure CLI, Azure Functions Core Tools
 
    ```
    func init --worker-runtime node --language javascript
    func new --name WeatherCheckFunction --template "Timer trigger"
    ```
    
  - 패키지 설치 : OpenWeather API 호출, 환경 변수 관리
    
    ```
    npm install axios dotenv
    ```

## 1. 필요한 설정
- OpenWeather API Key를 발급 필요
- Slack Webhook URL을 생성


## 2. 환경 변수 설정
- Azure Functions의 Application Settings 환경 변수를 추가
- OPENWEATHER_API_KEY → OpenWeather API 키
- SLACK_WEBHOOK_URL → Slack Webhook URL

  
## 3. 실행 방법
- Azure Functions에서 Timer Trigger를 사용하여 특정 시간마다 실행되도록 설정
- 예를 들어, 5분마다 실행하려면 0 */5 * * * * (CRON 표현식) 사용
- 눈(Snow) 또는 비(Rain) 감지 시 Slack에 푸시 알림 전송

## 4. Code
- node.js

  ```javascript
  const axios = require("axios");

  module.exports = async function (context, myTimer) {
      const OPENWEATHER_API_KEY = process.env.OPENWEATHER_API_KEY;
      const CITY = "분당"; // 원하는 도시 입력
      const SLACK_WEBHOOK_URL = process.env.SLACK_WEBHOOK_URL;
  
      try {
          // OpenWeather API 호출
          const response = await axios.get(`https://api.openweathermap.org/data/2.5/weather?lat=37.4&lon=127.1&appid=${OPENWEATHER_API_KEY}`);
  
          const weather = response.data.weather[0].main;
  
          // 응답 확인 로그
          context.log('Weather data received: ', response.data);
  
          // 눈 또는 비가 내리면 Slack 알림 전송
          if (weather === "Rain" || weather === "Snow") {
              await axios.post(SLACK_WEBHOOK_URL, {
                  text: `🚨 [날씨 알림] 현재 ${CITY}에 ${weather === "Rain" ? "비" : "눈"}가 내리고 있습니다. ☔❄`
              });
              context.log(`Slack 알림 전송: ${weather}`);
          } else if (weather === "Clear") {
              await axios.post(SLACK_WEBHOOK_URL, {
                  "text": ":sunny: *오늘은 맑고 화창한 날씨입니다!* :sunny: \n\n푸른 하늘과 부드러운 바람이 기분 좋게 해주는 하루입니다. 햇살을 만끽하세요! :sun_behind_small_cloud:"
              });
          } else {
              context.log(`날씨 상태: ${weather} (알림 없음)`);
  
          }
      } catch (error) {
          context.log(`오류 발생: ${error.message}`);
      }
  };
  
  ```
  
  - function.json (Azure Timer Trigger 설정)
 
  ```
  {
    "bindings": [
        {
          "name": "myTimer",
          "type": "timerTrigger",
          "direction": "in",
          "schedule": "0 */5 8-9 * * 1-5" // 평일 오전 8시에서 9시 사이 5분 간격
        }
    ]
  }
  ```

## 5. 환경 변수 설정 (local.settings.json)
- Azure Functions의 Application Settings에서 환경 변수를 설정

  ```
  {
    "IsEncrypted": false,
    "Values": {
      "AzureWebJobsStorage": "UseDevelopmentStorage=true", // 로컬에서 Functions 실행하려면 필요한 설정 : Azure Storage Emulator 활성화
      "OPENWEATHER_API_KEY": "API_키",
      "SLACK_WEBHOOK_URL": "Slack_Webhook_URL"
    }
  }
  ```

## 6. 실행

*---func start만 하면 에러 발생하므로 AzureStorageEmulator를 설치받아 에뮬레이터 실행 후 func start 해야함!!!---*


- 로컬에서 실행
```
func start
```

### 주의 사항
- func start만 실행하면 아래 에러 발생
  1. func 인지 못하는 문제
  ```
  npm install -g azure-functions-core-tools@4 --unsafe-perm true
  ```

  2. 연결 거부 문제
  ```
  대상 컴퓨터에서 연결을 거부했으므로 연결하지 못했습니다. (127.0.0.1:d in ClientOptions.Retry or by configuring a custom retry policy in ClientOptions.RetryPolicy. (대상 컴퓨터에서 연결을 거부했으므로 연결하지 못했습니다.
  Worker process started and initialized.
  
  Functions:
  
          WeatherCheckFunction: timerTrigger
  
  For detailed output, run func with --verbose flag.
  [2025-02-19T05:50:39.491Z] The listener for function 'Functions.WeatherCheckFunction' was unable to start.
  
  ```
- 원인
  - 127.0.0.1:10000에서 연결을 거부한 오류는 로컬 Azure Storage Emulator와 연결이 제대로 되지 않음을 의미
    
- 해결 방법
  - Azure Storage Emulator 실행

- Azure Storage Emulator가 제대로 실행 중인지 확인
  ```
  AzureStorageEmulator status
  AzureStorageEmulator start
  ```
  - AzureStorageEmulator 설치 필요
    - 아마 .. AzureStorageEmulator : 'AzureStorageEmulator' 용어가 cmdlet, 함수~ 이런 에러가 날듯.. => 설치 필요
    ```
    npm install -g azurite
    ```
    ```
    azurite
    ```


## 7. Azure Functions App에 배포

  1. Azure Functions App 생성
  - 먼저 Azure CLI를 이용해 배포할 Function App 생성
    ```
    az group create --name WeatherAlertRG --location eastus
  
    az storage account create --name weatheralertstorage --location eastus --resource-group WeatherAlertRG --sku Standard_LRS
    
    az functionapp create --resource-group WeatherAlertRG --consumption-plan-location eastus \
        --runtime node --runtime-version 18 \
        --name WeatherAlertFunctionApp --storage-account weatheralertstorage
  
    ```
  - WeatherAlertRG → 리소스 그룹 이름
  - WeatherAlertFunctionApp → Function App 이름
  - weatheralertstorage → 스토리지 계정

  2. Azure 에 배포
  ```
  func azure functionapp publish WeatherAlertFunctionApp
  // func azure functionapp publish <your-function-app-name>
  ```
  3. Azure에서 실행!!

## 8. Azure Functions App에서 실행 확인
  
  - Azure Portal에서 확인:
    1. Azure Portal 접속 → Function Apps → WeatherAlertFunctionApp
    2. WeatherCheckFunction 선택
    3. "Logs" 탭에서 실행 상태 확인
    4. Slack 알림이 정상적으로 도착하는지 체크



## 9. API 응답 데이터

```
Weather data received:  {
  coord: { lon: 127.1, lat: 37.4 },
  weather: [ { id: 800, main: 'Clear', description: 'clear sky', icon: '01d' } ],
  base: 'stations',
  main: {
    temp: 274.84,
    feels_like: 272.59,
    temp_min: 274.84,
    temp_max: 274.84,
    pressure: 1028,
    humidity: 29,
    sea_level: 1028,
    grnd_level: 1015
  },
  visibility: 10000,
  clouds: { all: 0 },
  dt: 1739945400,
  sys: {
    type: 1,
    id: 5509,
    country: 'KR',
  dt: 1739945400,
  sys: {
    type: 1,
    id: 5509,
    country: 'KR',
  sys: {
    type: 1,
    id: 5509,
    country: 'KR',
    id: 5509,
    country: 'KR',
    country: 'KR',
    sunrise: 1739916995,
    sunset: 1739956479
  },
  timezone: 32400,
  id: 1897000,
  name: 'Seongnam-si',
  cod: 200
}
```
## 10. 결과

![image](https://github.com/user-attachments/assets/c109a94b-e502-46c3-91b3-687134e50cad)

 
### 코멘트
- 로컬 실행은 비용 안듦 -> azure 배포 후 클라우드 환경에서 실행하는 경우 비용 발생
- Github Actions와 Event Grid 차이 비교
- 소스관리를 azure에서 할 지 github에서 할 지 고민

   
---


# Functions app 에서 Event grid 구독

## Azure Functions와 Azure Event Grid를 연계하여 이벤트 기반 애플리케이션 구조
### 1. Azure Event Grid와 연계하기 위한 기본 흐름:
- Azure Event Grid 주제 (Event Grid Topic)를 설정합니다.
- Azure Functions에서 이벤트를 트리거할 수 있도록 Event Grid 이벤트 핸들러를 작성합니다.
- Azure Event Grid와 Azure Functions 연결: Event Grid의 이벤트를 Azure Functions에서 수신하고, 이를 처리합니다.
### 2. Azure Event Grid와 Azure Functions 연계 설정
- Azure Event Grid Topic 생성: Azure Portal에서 Event Grid Topic을 생성합니다.

- Event Grid Topic은 이벤트를 발행하는 위치로, 다양한 서비스에서 발생하는 이벤트를 수신할 수 있습니다.
- Azure Event Grid Topic 만들기
- Azure Functions에서 Event Grid 트리거 사용: Azure Functions에서 Event Grid 트리거를 설정하여 Event Grid에서 발생한 이벤트를 처리하도록 합니다.

- Azure Functions에 Event Grid Trigger 추가: Node.js로 Azure Functions 앱을 작성한다고 가정할 때, Event Grid Trigger를 사용하여 이벤트를 수신합니다.

### Azure Functions에서 Event Grid 트리거 함수 설정
- function.json
```json
{
  "bindings": [
    {
      "name": "eventGridEvent",
      "type": "eventGridTrigger",
      "direction": "in"
    }
  ]
}
```
- Azure Functions 앱에서 Event Grid에서 발생한 이벤트를 처리하는 코드
```javascript
const axios = require('axios');

module.exports = async function (context, eventGridEvent) {
    context.log('Event Grid trigger function processed event:', eventGridEvent);

    // Event Grid에서 전달받은 이벤트 내용 로그
    context.log(`Event Type: ${eventGridEvent.eventType}`);
    context.log(`Event Data:`, eventGridEvent.data);

    // 예시: 날씨 변화 이벤트가 발생했을 경우 Slack으로 알림 전송
    if (eventGridEvent.eventType === 'WeatherChange') {
        const slackWebhookUrl = process.env.SLACK_WEBHOOK_URL;
        const slackMessage = {
            text: `Alert: Weather condition changed! Previous: ${eventGridEvent.data.previousWeather}, Current: ${eventGridEvent.data.currentWeather}`
        };

        // Slack 알림 전송
        await axios.post(slackWebhookUrl, slackMessage);
        context.log('Slack notification sent');
    }
};
```
