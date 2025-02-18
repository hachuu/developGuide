1. 필요한 설정
- OpenWeather API Key를 발급받아야 합니다.
- Slack Webhook URL을 생성해야 합니다.

2. 환경 변수 설정
- Azure Functions의 Application Settings에서 다음 환경 변수를 추가하세요.
- OPENWEATHER_API_KEY → OpenWeather API 키
- SLACK_WEBHOOK_URL → Slack Webhook URL
3. 실행 방법
- Azure Functions에서 Timer Trigger를 사용하여 특정 시간마다 실행되도록 설정
- 예를 들어, 5분마다 실행하려면 0 */5 * * * * (CRON 표현식) 사용
- 눈(Snow) 또는 비(Rain) 감지 시 Slack에 푸시 알림 전송

4. example
- python
  ```python
  import os
  import requests
  import json
  import logging
  import azure.functions as func
  
  # 환경 변수에서 API 키 및 Slack Webhook URL 가져오기
  OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
  SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
  CITY = "Seoul"  # 원하는 도시 설정
  
  def get_weather():
      """OpenWeather API를 호출하여 현재 날씨 정보를 가져옴"""
      url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={OPENWEATHER_API_KEY}&units=metric"
      response = requests.get(url)
      
      if response.status_code == 200:
          return response.json()
      else:
          logging.error(f"OpenWeather API 요청 실패: {response.status_code}")
          return None
  
  def send_slack_notification(message):
      """Slack Webhook을 사용하여 메시지를 보냄"""
      payload = {"text": message}
      headers = {"Content-Type": "application/json"}
      
      response = requests.post(SLACK_WEBHOOK_URL, data=json.dumps(payload), headers=headers)
      if response.status_code == 200:
          logging.info("Slack 알림 전송 성공")
      else:
          logging.error(f"Slack 알림 전송 실패: {response.status_code}")
  
  def main(mytimer: func.TimerRequest) -> None:
      logging.info("Azure Function 실행: 날씨 확인 중...")
  
      weather_data = get_weather()
      if not weather_data:
          return
  
      weather_conditions = weather_data["weather"][0]["main"]
      temp = weather_data["main"]["temp"]
      city_name = weather_data["name"]
  
      if weather_conditions in ["Rain", "Snow"]:
          message = f"🚨 {city_name}에서 {weather_conditions}이(가) 감지되었습니다! 현재 온도: {temp}°C 🌡️"
          send_slack_notification(message)
  ```
- node.js
  ```javascript
  const axios = require("axios");
  require("dotenv").config();
  
  const OPENWEATHER_API_KEY = process.env.OPENWEATHER_API_KEY;
  const SLACK_WEBHOOK_URL = process.env.SLACK_WEBHOOK_URL;
  const CITY = "Seoul"; // 원하는 도시 설정
  
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
  
  module.exports = async function (context, myTimer) {
      context.log("Azure Function 실행: 날씨 확인 중...");
  
      const weatherData = await getWeather();
      if (!weatherData) return;
  
      const weatherConditions = weatherData.weather[0].main;
      const temp = weatherData.main.temp;
      const cityName = weatherData.name;
  
      if (weatherConditions === "Rain" || weatherConditions === "Snow") {
          const message = `🚨 ${cityName}에서 ${weatherConditions}이(가) 감지되었습니다! 현재 온도: ${temp}°C 🌡️`;
          await sendSlackNotification(message);
      }
  };
  
  ```
  - function.json (Azure Timer Trigger 설정)
  - 5분마다 실행..=> 출근 시각으로 변경 필요
  ```
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
5. 환경 변수 설정 (local.settings.json)
- Azure Functions의 Application Settings에서 환경 변수를 설정하세요.
```
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "OPENWEATHER_API_KEY": "여기에_당신의_API_키",
    "SLACK_WEBHOOK_URL": "여기에_당신의_Slack_Webhook_URL"
  }
}
```
6. 실행 및 배포
- 로컬에서 실행
```
func start
```
- Azure Functions 배포
```
func azure functionapp publish <your-function-app-name>
```
