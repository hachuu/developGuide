# keyword

## 자연어 처리 고도화
- encoder : 문장 이해
- decoder : 답변 생성 -> llm 모델에 주로 사용

- 딥러닝 -> 트랜스포머 -> Mamba(아직 상용화되진 않음)
- transformer : 모든 llm 모델에 사용
  - 단점 : attention 망각, 환각 현상
- 파인튜닝했을 때.. 도메인 지식을 넣어봤자, 학습데이터가 적고, 확률 분포가 안좋을 수 있음 모델 정확도가 안좋을 수 있음

- BERT : encoder 모델
- DeepSeek: Knowledge Distillation 문제
- 지식 증류
  - Hard Target(하드 타겟): "이 문제의 정답은 A입니다"(0 또는 1)
  - Soft Target(소프트 타겟): "A가 60% 확률로 맞고, B는 20%, C는 15%..."(확률 분포) ex) 인생은 무엇인가... 정답이 없는 것들..

- fine tuning : 미세 조정 -> ex ) 오은영박사 저서 학습으로 육아 전문 모델
- Emergent Abilities(창발적 능력): 임계점을 넘으면 나타나는 능력 -> 쉬운 비유: 물이 끓는 현상
- 벡터 검색 : 의미 기반
- 임베딩 : 사람의 언어 -> 컴퓨터의 언어로 번역(숫자)
- 청킹 : 데이터 조각

## python 3.11 실습
git clone https://github.com/parkseohuinim/lecture.git
py -m venv venv
.\venv\Scripts\activate
cd .\lab03~~
Readme.md 참조


python.exe -m pip install --upgrade pip (py -3.11 -m pip install --upgrade pip)
py -3.11 -m pip install -r req
pip install -r req(tab)

```
py -0p

# 3.11로 파이썬 실행
py -3.11

# 3.11 인터프리터로 스크립트 실행 : lab 해당 경로로 가서
py -3.11 basic_embedding.py
```
# 3.11 인터프리터에 패키지 설치 (중요!)
py -3.11 -m pip install openai tiktoken python-dotenv
``
