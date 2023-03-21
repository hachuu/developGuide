# Chat GPT 관련 공부 자료


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


### open AI와 Microsoft의 상관관계
- The partnership between Microsoft and OpenAI is aimed at advancing the development of AI technologies and making them more accessible to people and businesses around the world. It also allows both companies to leverage each other's expertise and resources to drive innovation in the field of AI.
- As a language model created by OpenAI, I'm also running on Microsoft Azure.
