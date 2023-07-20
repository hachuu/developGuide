# Python3에서 Selenium으로 크롬 자동화 작업 하는 방법

## 순서
1. python 3 다운로드
   - 다운이 되어 있는 경우 py --version / python --version 명령어로 버전 확인함
2. 셀레니움 다운로드 pip install selenium
   - pip를 인지 못하는 경우 pip 환경 변수, 시스템 변수 등록
   - 경로 : C:\Users\KTDS\AppData\Local\Programs\Python\Python311\Scripts
   - 다시 시작 후 pip 명령어 실행 => 정상 동작
3. chromedriver 다운로드
  - https://sites.google.com/a/chromium.org/chromedriver/downloads : 9x version 이하
  - https://sites.google.com/chromium.org/driver/downloads?authuser=0 : 현재 114 version 
4. 소스 구현
5. venv\Scripts\activate
6. debug start
```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome 웹 드라이버 경로 설정
driver_path = "드라이버_경로_설정"

# 웹 드라이버 초기화
driver = webdriver.Chrome(driver_path)

# 웹 페이지로 이동
driver.get("로그인_페이지_URL")

# 로그인 정보 입력
username = driver.find_element_by_name("username")  # 사용자명 입력 필드 선택
password = driver.find_element_by_name("password")  # 비밀번호 입력 필드 선택

username.send_keys("사용자명")  # 사용자명 입력
password.send_keys("비밀번호")  # 비밀번호 입력

# 로그인 버튼 클릭
login_button = driver.find_element_by_xpath("//button[contains(text(), '로그인')]")
login_button.click()

# 로그인 후 처리 대기
wait = WebDriverWait(driver, 10)  # 최대 10초까지 대기
wait.until(EC.title_contains("로그인 성공 페이지 제목"))

# 라디오 체크박스 선택
radio_button = driver.find_element_by_id("라디오_체크박스_ID")
radio_button.click()

# 버튼 클릭
button = driver.find_element_by_id("버튼_ID")
button.click()

# 웹 드라이버 종료
driver.quit()

```
