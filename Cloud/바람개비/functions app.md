# [VS Code] 로컬 환경에서 functions app 실행하기

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

## 6. 실행 및 배포

*---func start만 하면 에러 발생하므로 AzureStorageEmulator를 설치받아 에뮬레이터 실행 후 func start 해야함!!!---*


- 로컬에서 실행
```
func start
```

### 주의 사항
- func start만 실행하면 아래 에러 발생
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


- Azure Functions 배포

```
func azure functionapp publish <your-function-app-name>
```
