# Chat GPT 프로젝트 관련 공부 자료

## Embedding vs Fine tuning 개념
- 임베딩은 텍스트를 벡터로 변환하는 과정 ( 벡터 : 문장에서 단어 간의 유사도를 계산하거나, 문서 간의 유사도를 계산하는 등의 작업에 사용 )
- 파인튜닝은 이미 학습된 모델을 새로운 데이터에 맞게 추가 학습하여 성능을 향상시키는 과정

## Fine tuning
### 방법
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

### 실제 Fine Tuning 개발할 때 풀어나가야 할 사항
- [참조: OpenAI guides] (https://platform.openai.com/docs/guides/fine-tuning)
- dataset할 시 JSONL document 포매팅
- CLI data preparation tool을 통해 데이터 변환 가능

## 임베딩
### 정의
- 텍스트를 다루기 쉽도록 변환하는 과정 (자연어 처리)
- ex) Amazon Fine Food Reviews
- 임베딩의 벡터는 각 단어를 수치화한 값으로, 벡터는 크기와 방향을 가지는 양(quantity)을 나타내며, 일반적으로 숫자들의 배열(array)로 표현
- "vector"는 단어를 수치화하여 숫자들의 배열로 표현한 것을 의미합니다. 이 벡터는 각 단어의 의미와 관련된 정보를 담고 있으며, 자연어 처리(NLP) 분야에서 많이 활용
- 문장에서 단어 간의 유사도를 계산하거나, 문서 간의 유사도를 계산하는 등의 작업에 사용
- [참조: youtube | Introduction to Text and Code Embeddings in the OpenAI API](https://www.youtube.com/watch?v=mnTV_TIkf9M)

## Best practices 와 정교한 모델을 위한 방안
- The model is better at inserting longer completions => 정교한 모델일수록 token이 많이 필요 함
- Prefer finish_reason == "stop"
    => 모델이 가능한한 "stop" 이유로 대화를 종료하도록 하는 조건을 의미합니다. 이는 모델이 대화를 지속할 수 있는 상황에서도 적절한 시점에서 대화를 종료하여 자연스러운 대화 흐름을         유지하고, 사용자의 경험을 향상시키기 위한 전략
- resampling 3 or 5 times => 데이터에 대한 리샘플링이 많을 수록 정교해짐

### open AI와 Microsoft의 상관관계
- The partnership between Microsoft and OpenAI is aimed at advancing the development of AI technologies and making them more accessible to people and businesses around the world. It also allows both companies to leverage each other's expertise and resources to drive innovation in the field of AI.
- As a language model created by OpenAI, I'm also running on Microsoft Azure.
