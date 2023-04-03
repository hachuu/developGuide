# Chat GPT 프로젝트 관련 공부 자료

## openAi에서 지원하는 자연어 처리 기술
- Embedding
- Fine tuning
- Completion
    - Text-Completion
    - Chat-Completion

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

### 임베딩을 통한 텍스트 유사성 조회
- 임베딩된 벡터값으로부터 특정 키워드를 추출하는 방법은 다양한 방법이 존재
- 이 중에서 가장 간단하면서도 효과적인 방법 중 하나는 벡터값 간의 코사인 유사도(Cosine Similarity)를 계산하여 특정 키워드와 유사한 단어들을 추출하는 것
- 코사인 유사도는 두 벡터 간의 유사도를 계산하는 데 사용되는 지표로, 벡터값이 공간에서 이루는 각도를 이용하여 유사도를 측정합니다. 즉, 코사인 유사도가 1에 가까울수록 두 벡터가 비슷하다는 것을 의미
- 과정
    1. 임베딩된 벡터값을 얻습니다. 예를 들어, OpenAI API의 createEmbedding 함수를 사용하여 벡터값을 얻을 수 있습니다.
    2. 추출하려는 키워드를 벡터값으로 변환합니다. 예를 들어, OpenAI API의 encode 함수를 사용하여 키워드를 벡터값으로 변환할 수 있습니다.
    3. 코사인 유사도를 계산하여 가장 유사한 단어들을 추출합니다. 벡터값 간의 코사인 유사도를 계산하는 데에는 여러 가지 방법이 있습니다. 예를 들어, numpy 패키지에서 제공하는 cosine_similarity 함수를 사용할 수 있습니다.
```
const openai = require('openai');
const { cosine } = require('calculate-cosine-similarity');

// OpenAI API 인증
openai.api_key = "YOUR_API_KEY";

// 키워드와 비교할 텍스트
const keyword = "apple";
const text = "I like to eat apples and bananas.";

// 키워드와 텍스트를 임베딩된 벡터값으로 변환
openai.Embedding.create({
  engine: "text-davinci-002",
  documents: [text],
  query: [keyword]
}).then(result => {
  const keywordVector = result.data[0].vector;
  const textVector = result.data[1].vector;

  // 키워드와 텍스트 간의 코사인 유사도 계산
  const similarity = cosine(keywordVector, textVector);
  console.log("Similarity:", similarity);

  // 텍스트에서 유사한 단어 추출
  const wordList = text.split(" ");
  const similarityList = cosine(keywordVector, textVector);
  const topN = 3;  // 상위 n개의 단어
  const topNSimilarWords = wordList
    .map((word, index) => ({ word, similarity: similarityList[index] }))
    .filter(({ word }) => word !== keyword)
    .sort((a, b) => b.similarity - a.similarity)
    .slice(0, topN)
    .map(({ word }) => word);
  console.log("Top N similar words:", topNSimilarWords);
}).catch(error => console.error(error));

```
```
const tf = require('@tensorflow/tfjs-node');
const cosineSimilarity = require('cosine-similarity');

// TensorFlow.js 모델 로드
const model = await tf.loadLayersModel('path/to/embedding/model.json');

// 입력 문장의 embedding 벡터 추출
const sentence = "Hello, how are you?";
const sentenceTokens = sentence.toLowerCase().split(" ");
const sentenceEmbedding = model.predict(tf.tensor([sentenceTokens])).arraySync()[0];

// OpenAI API로 completion 생성
const openai = require('openai');
const api_key = 'your_api_key';
const api_endpoint = 'https://api.openai.com/v1';
const prompt = `Your prompt goes here`;
const max_tokens = 32;
const n = 5;
const engine = 'davinci';
const completions = await openai.complete({ engine, prompt, max_tokens, n, api_key, api_endpoint });

// 각 completion의 embedding 벡터 추출 및 유사도 계산
const completionEmbeddings = completions.choices.map(c => c.embedding);
const similarities = completionEmbeddings.map(c => cosineSimilarity(sentenceEmbedding, c));

// 가장 유사한 completion 출력
const mostSimilarIndex = similarities.indexOf(Math.max(...similarities));
console.log(`Most similar completion: ${completions.choices[mostSimilarIndex].text}`);

```

### embedding을 통해 구현하는 것을 간략히 이해되도록 설명하자면...
- 학습시킬 데이터들의 Vector값을 db에 모두 저장한다. => createEmbedding api로 모두 vector 값 추출 가능
- 신규 input으로 createCompletion을 하면서 입력된 input 언어의 vector값을 구해 db에서 가장 유사한 데이터를 찾아 가장 유사성이 높은 solution으로 completion으로 돌려주는 작업

## Best practices 와 정교한 모델을 위한 방안
- The model is better at inserting longer completions => 정교한 모델일수록 token이 많이 필요 함
- Prefer finish_reason == "stop"
    => 모델이 가능한한 "stop" 이유로 대화를 종료하도록 하는 조건을 의미합니다. 이는 모델이 대화를 지속할 수 있는 상황에서도 적절한 시점에서 대화를 종료하여 자연스러운 대화 흐름을         유지하고, 사용자의 경험을 향상시키기 위한 전략
- resampling 3 or 5 times => 데이터에 대한 리샘플링이 많을 수록 정교해짐

## Chat Completion vs Text Completion
```
"Create chat completion"과 "Create completion"은 모두 GPT 모델에서 사용되는 용어입니다.

"Create chat completion"은 사용자와의 대화를 유지하면서 모델이 다음에 올 말을 자동으로 생성하는 기능을 말합니다. 즉, 모델이 이전 대화 내용을 이해하고 그에 맞는 응답을 생성하는 것입니다. 이것은 챗봇과 같은 인터랙티브한 응용 프로그램에서 매우 유용합니다.

반면에 "Create completion"은 모델에게 특정 문장이나 단락을 주면, 그것을 이어지는 문맥과 일치하도록 자동으로 끝을 작성하도록 하는 기능입니다. 이것은 글쓰기, 번역, 요약 등의 응용 프로그램에서 유용합니다.

따라서, "Create chat completion"은 인터랙티브 대화 형식에서 자동 응답 생성을 위해 사용되는 반면에, "Create completion"은 문장 또는 문단을 자동으로 완성하고 이어지는 문맥에 맞추기 위해 사용됩니다.
```

### Completion Request Param 정의
- presence_penalty : -2.0에서 2.0 사이의 숫자, 지금까지 텍스트에 나타나는지 여부에 따라 새로운 토큰에 페널티를 주어 모델이 새로운 주제에 대해 이야기할 가능성을 높임.
- frequency_penalty : -2.0에서 2.0 사이의 숫자, 양수 값은 지금까지 텍스트의 기존 빈도를 기반으로 새 토큰에 페널티를 주어 모델이 동일한 줄을 그대로 반복할 가능성을 줄임
- temperature : 값이 높을수록 모델이 더 많은 위험을 감수하게 됨 => 더 창의적인 응용 프로그램에는 0.9를, 잘 정의된 답이 있는 응용 프로그램에는 0을 사용, top_p와 같이 사용하는 것을 비추천
- top_p : 0.1은 상위 10% 확률 질량을 구성하는 토큰만 고려됨을 의미, 일반적으로 온도와 같이 조절하는 것을 추천하지 않음


### open AI와 Microsoft의 상관관계
- The partnership between Microsoft and OpenAI is aimed at advancing the development of AI technologies and making them more accessible to people and businesses around the world. It also allows both companies to leverage each other's expertise and resources to drive innovation in the field of AI.
- As a language model created by OpenAI, I'm also running on Microsoft Azure.

### 읽을거리들..
[AI가 우리 삶에 끼치는 영향들](https://news.hada.io/weekly/202314?utm_source=slack&utm_medium=bot&utm_campaign=T0138F4V7L0)
