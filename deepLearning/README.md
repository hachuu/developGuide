# [딥러닝 교육](https://www.notion.so/c28d54a55bc34c6da9db3f3965706ac1?pvs=4)


- 머신러닝
    - 지도 학습 : 문제와 정답을 모두 알려주고 공부시킴
        - 비용이 많이 들음
    - 비지도 학습 : 답을 가르쳐주지 않고 공부시킴
        - chatGpt같은 생산형 AI에서 많이 쓰임
    - 강화 학습 : 게임같이 보상해주는 것 (어려운 개념..)
- 머신러닝 아키텍쳐에는 서비스형태와 데이터 학습하는 형태가 구분되어있음

- Perceptron 1957 : 다수의 입력으로부터 가중합을 계산하고, 이를 이용해 하나의 출력을 만드는 구조
    - f(x1,x2)  = w1x1 + w2x2 + b
    - chatGpt에서 w와 b는 1700억개
    - Output(예측값) = Activation(dot(W,x))
    - error(손실값) = loss(Output,y)
    - 입력 데이터x와 타깃 y는 고정되어있다면, 이 함수는 W를  error에 매핑하는 함수로 볼 수 있음
        - error = f(W)
        - 오차함수 미분

- 스테이블 디퓨전 : 게이밍 컴퓨터가 있다면

- ✨딥러닝
    - 딥러닝 학습 : 손실함수가 최소가 되도록 하는 매개변수를 찾는 것 / 신경망 학습을 컴퓨터나 gpu에게 시키는 것
    - 신경망 학습 : w, b (학습매개변수)를 구하는 것
    - gpu의 강점 : 반복된 계산을 잘함
    - 학습 데이터를 통한 최적화로 얼마나 학습되지 않은 데이터(새로운 데이터)에 대해 일반화가 잘되었나가 중요함 ⇒ 실제로 Optimal하게 하는 것이 중요함
    
    - 일반적인 학습 순서
        1. 주어진 문제와 훈련할 데이터를 정의
        2. 이 데이터를 수집하고 필요하면 데이터 정규화, 레이블 태깅등을 한다.
        3. 손실함수를 정하고, 성공을 어떻게 측정할지 선택 
            1.  검증 데이터에서 모니터링할 지표는 무엇인지 정의
        4. 평가 방법을 결정
            1. 검증에 사용할 데이터의 양은 얼마나 되나?
            2. 홀드아웃 검증, K-겹 교차 검증 등 방법 정의
        5. 단순한 랜덤 선택 모델보다 나은 통계적 검정력이 있는 첫번째 모델을 생성
        6. 과대적합된 모델을 생성 (Overfit)
        7. 검증 데이터의 성능에 기초하여 모델에 규제를 적용, 하이퍼파라미터를 튜닝해 최적의 모델을 찾음
    - keras
    
- 딥러닝 실습
    - [https://colab.research.google.com/drive/1eqGoWHeGI9jI2KziPGP6J0B1NAqu2yv3#scrollTo=8Q-sO8Ir2qq9](https://colab.research.google.com/drive/1eqGoWHeGI9jI2KziPGP6J0B1NAqu2yv3#scrollTo=8Q-sO8Ir2qq9)
    - Data 전처리
        - 딥러닝 모델 : 입력 데이터의 형상(shape)을 정확하게 파악하여 모델의 구조를 결정
        - 입력 데이터의 형상은 데이터셋에 따라 다양하게 변화할 수 있음, 이 때문에 모델이 예측할 수 있는 입력 데이터의 형상도 다양하게 변화하게 됨
        - 입력 데이터의 형상이 모델에 맞지 않을 때 reshape을 사용하여 형상을 바꿔주어야 함
            - reshape : 데이터 전처리(preprocessing) 과정에서 필수적인 작업 중 하나 (TensorFlow나 PyTorch 같은 딥러닝 프레임워크에서는 reshape을 간단하게 수행할 수 있는 함수를 제공)

---
## Embedding vs Fine tuning
- 임베딩은 텍스트를 벡터로 변환하는 과정
- 파인튜닝은 이미 학습된 모델을 새로운 데이터에 맞게 추가 학습하여 성능을 향상시키는 과정

### Fine Tuning
- [참조](https://platform.openai.com/docs/guides/fine-tuning)
- JSONL document 포맷
- CLI data preparation tool을 통해 데이터 변환 가능

### Fine Tuning 방법
1. Dataset : 내가 가지고 있는 데이터를 jsonl 파일로 변환해야함
    - ex ) pdf => jsonl / pdf 텍스트를 추출, python으로 텍스트 => jsonl 로 변환
    - Fine-tuning에 사용되는 데이터셋이 모델이 사용될 구조와 작업 유형과 매우 유사하도록 작업
    - 클래스가 하나의 토큰에 매핑되도록 클래스를 선택
    - 프롬프트 + 완성이 분리자를 포함하여 2048개의 토큰을 초과하지 않도록
    - 클래스 당 최소 100개의 예제를 목표
2. Data type
    - prompt : 모델에 학습시키기 위한 입력
    - completion : 모델이 생성하는 출력
3. 변환된 텍스트를 자연어 처리를 하기 위해 python과 같은 언어에서 작업을 함
```
{"prompt":"Company: BHFF insurance\nProduct: allround insurance\nAd:One stop shop for all your insurance needs!\nSupported:", "completion":" yes"}
{"prompt":"Company: Loft conversion specialists\nProduct: -\nAd:Straight teeth in weeks!\nSupported:", "completion":" no"}
```

### 임베딩 : 텍스트를 다루기 쉽도록 변환하는 과정 (자연어 처리)
- ex) Amazon Fine Food Reviews
- [Introduction to Text and Code Embeddings in the OpenAI API | TransformX 2022](https://www.youtube.com/watch?v=mnTV_TIkf9M)

## 자연어 처리
- temperature : 0~2사이값 0.8 이상 : random / 0.2 : 좀 더 집중되고, 결정론적인 출력


## Best practices
- The model is better at inserting longer completions
- Prefer finish_reason == "stop"
- resampling 3 or 5 times

---

tensorflow는 어디꺼야?

TensorFlow는 Google에서 개발하고 유지 관리하는 오픈소스 머신 러닝 프레임워크입니다. TensorFlow는 Python, C++, Java 등 다양한 언어로 사용할 수 있으며, GPU를 이용한 가속화를 지원하여 대규모 딥러닝 모델을 효율적으로 학습시킬 수 있습니다. TensorFlow는 TensorFlow.org에서 다운로드 및 사용할 수 있습니다.


Pytorch는?

PyTorch는 Facebook에서 개발하고 유지 관리하는 오픈소스 머신 러닝 프레임워크입니다. PyTorch는 Python에서 제공되며, 딥러닝 모델의 구성과 학습을 위한 다양한 편리한 도구와 인터페이스를 제공합니다. PyTorch는 자동 미분 기능을 갖추고 있어, 딥러닝 모델의 학습을 더욱 쉽게 할 수 있습니다. PyTorch는 PyTorch.org에서 다운로드 및 사용할 수 있습니다.


keras는?

Keras는 딥러닝 모델을 쉽고 빠르게 구성할 수 있는 고수준 라이브러리입니다. TensorFlow, Theano, CNTK 등 다양한 백엔드 엔진을 지원하며, 쉽게 모델을 구성하고 학습할 수 있는 API를 제공합니다. Keras는 Python에서 제공되며, 다양한 신경망 레이어, 활성화 함수, 최적화 알고리즘 등을 포함하여 다양한 딥러닝 모델을 구성할 수 있습니다. Keras는 TensorFlow의 공식 API로 통합되어, TensorFlow 2.0 이상 버전에서는 TensorFlow.keras 모듈로 제공됩니다. Keras는 keras.io에서 다운로드 및 사용할 수 있습니다.
