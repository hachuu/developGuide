1. LLM 이란?
- 대량의 텍스트를 학습해 다음에 올 말을 확률적으로 예측하는 언어 모델
- 질문에 대한 그럴듯한 응답 생성에는 강하지만, 스스로 행동하지는 못함
- 기본적으로 상태,기억,목표가 없는 단발성 응답 구조

2. AI Agent 배경
- LLM의 한계
  - 대화 맥락과 정보를 지속적으로 기억하지 못함
  - 외부 시스템(DB, API, 알림 등)을 직접 제어할 수 없음
  - 목표 달성이나 결과 검증에 대한 책임과 판단 구조가 없음
- AI Agent가 등장한 배경
  - 답변 생성을 넘어 실제 업무를 처리할 AI가 필요해짐
  - LLM에 상태, 도구 사용, 실행 로직을 결합해 행동 가능하게 만듦
  - 반복 작업, 워크플로우, 자동화를 위해 제어 가능한 구조가 요구됨

3. AI Agent란?
- 한줄 요약 : 생각만 하는 AI가 아닌 상황을 이해하고 필요한 일을 나눠서 실제 행동까지 시키는 프로그램 구조
- 목표를 달성하기 위해 "계획(Plan) -> 실행(Act) -> 관찰(Observe) -> 수정(Iterate)"을 반복하는 소프트 웨어
- 단순 챗봇이 "답변 생성"에만 집중한다면, 에이전트는 보통 아래를 포함
  - 도구 사용(Tool calling) : DB 조회, API 호출, 파일 읽기/쓰기, Slack 전송 등
  - 상태(State) : 대화/작업 컨텍스트(세션 메모리), 장기 메모리(지식/기록)
  - 워크플로우(Orchestration) : 어떤 순서로 어떤 작업을 시킬지, 실패 시 재시도/대체 경로
  - 가드레일 : 정책/보안/PII 마스킹, 입력 검증, 비용/시간 제한

4. AI Agent 구조
  1. **Single** : 단순구조
    - 구조
      1. 사용자 입력
      2. LLM이 "생각 + 툴 호출" 결정
      3. 툴 결과 반영해서 최종 답변
    - 한계
      1. 검색, 요약, 분류, 검증, 액션
      2. 실패/지연/비용이 늘음
      3. 테스트/디버깅 어려움
  2. **Multie** : Single 보완, 역할 분리, LLM을 여러번 쓰는 것이 아니라, 책임과 실패 영역을 분리해서 운영이 쉬워짐
    - 구조
      1. Router(분기/의도문류)
      2. Retriever(검색/근거수집)
      3. Planner(계획수립)
      4. Executor(툴 실행)
      5. Verifier(검증/안전/품질)
      6. Summarizer(결과 정리)
      7. Memory Manager(STM/LTM 저장/삭제/회수)

  3. Single에서 멀티로 발전한 이유
    - 하나의 Agent가 모든 역할을 맡으면 복잡도와 실패 리스크가 증가
    - 역할별 Agent 분리 책임, 품질, 디버깅이 쉬워짐
    - 대규모 처리와 확장을 위해 비동기, 분산 구조가 필요해짐
    
  4. Single -> Multie 구조화 단계
     - 단계 A. 역할 분리 + 계약 (Contract)
       - 각 서브 에이전트는 입력/출력 스키마(JSON)를 고정
       - 예 : Retriever는 "근거 목록 + 출처 + 신뢰도"만 반환
       - 장점 : 테스트 가능, 교체 가능
     - 단계 B. 오케스트레이터 도입
       - 중앙 Orchestrator(Manager/Coordinator)를 둡니다.
       - 역할 :
         - 어떤 에이전트를 언제 호출할지 결정
         - 타임아웃/재시도/폴백
         - 상태(세션) 관리
     - 단계 C. 비동기화 + Pub/Sub / Queue로 확장
       요청이 많아지면 동기 체인이 길어져서 느려지고 불안정해짐
       이때 Pub/Sub + Queue 가 들어가짐
       - Pub/Sub(이벤트 브로드캐스트) : "무슨 일이 발생했다"를 여러 소비자에게 알림
       - Queue(작업 대기열) : "일을 처리해라"를 안정적으로 순서/부하조절하며 처리
       * Pub/Sub = 알림(이벤트), Queue = 작업(잡 처리)
     - 단계 D. 상태/메모리 분리
       멀티 에이전트에서 제일 많이 터지는 문제가 "상태 공유"
       - 추천 원칙 : 
         - 세션 상태(STM) : Redis 같은 빠른 저장소
         - 장기 메모리(LTM) : DB/Vector DB(추후 Cosmos DB  확장 계획인 경우)
         - 에이전트들은 각자 메모리 갖고 있지 말고 Memory Service를 통해 읽고 씀

5. 멀티 에이전트의 아키텍처 패턴 3가지
  1. Manager-Worker
    - Manager(오케스트레이터)가 계획 수립
    - Worker 서브 에이전트들이 실행/검색/검증 수행
    - 장점 : 통제가 쉽고 운영/디버깅 용이
    - ex) 대부분의 사내 업무 자동화, 고객응대, 워크플로우
  2. Event-Driven
    - 이벤트 발생 -> 여러 에이전트가 구독해서 각자 처리
    - 장점 : 확장성/느슨한 결합, 기능 추가가 쉬움
    - 단점 : 추적/디버깅(관측성) 없으면 지옥
    - ex) 비동기 파이프라인, 로그/레코드 기반 자동화
  3. Pipeline / DAG
    - 정해진 단계대로 흘러감 (A->B->C)
    - 장점 : 결과 재현/테스트 쉬움
    - 단점 : 예외 케이스 분기 많아지면 복잡
    - ex) 문서 처리(분류->추출->요약->검증), 정형 워크 플로우

6. Pub/Sub VS Queue
```
사용자 메시지 들어옴 -> 콘텐츠인지 판단 -> 웹검색/사내검색 -> 요약 -> 검증 -> Slack 전송/저장
```

- Pub/Sub 이벤트 :
  - MesssageReceived
  - ContentDetected
  - EvidenceCollected
  - DraftReady
  - Verified
- Queue 작업
  - RunDetectionJob
  - RunRetrievalJob
  - RunSummarizeJob
  - RunVerificationJob
  - RunPublishJob
 
7. Sample Architecture
  1. 멀티 에이전트 아키텍처 다이어그램
     a. 동기(초기) 버전 : Orchestrator 중심
     <img width="1089" height="767" alt="image" src="https://github.com/user-attachments/assets/2b2fbf9f-c050-41b4-80ec-d7fd7fe9aeae" />
     
      ```
      flowchart LR
        U[User/App] --> API[Fastify API]
        API --> ORCH[Orchestrator/Manager]
      
        ORCH --> R[Router Agent]
        ORCH --> P[Planner Agent]
        ORCH --> RET[Retriever Agent]
        ORCH --> EXE[Executor Agent]
        ORCH --> V[Verifier Agent]
        ORCH --> S[Summarizer Agent]
      
        ORCH <--> MEM[Memory Service]
        MEM <--> STM[(Redis: STM)]
        MEM <--> LTM[(DB/Vector: LTM)]
      
        EXE --> TOOLS[Tools: DB/API/Slack]
        ORCH --> API --> U
      ```
      
     b. 비동기(확장) 버전 : Pub/Sub + Queue
     <img width="1674" height="924" alt="image" src="https://github.com/user-attachments/assets/7542b4b3-1a5d-4632-b9c7-2aeb48d6719c" />
     
      ```
      flowchart TB
        U[User/App] --> API[Fastify API]
        API --> EV[Event: MessageReceived]
        EV --> EG[(Pub/Sub: Event Bus)]
      
        EG --> ORCH[Orchestrator]
        ORCH --> Q1[(Queue: Detect/Route Jobs)]
        ORCH --> Q2[(Queue: Retrieval Jobs)]
        ORCH --> Q3[(Queue: Summarize/Verify Jobs)]
        ORCH --> Q4[(Queue: Publish/Store Jobs)]
      
        Q1 --> R[Router Agent]
        Q2 --> RET[Retriever Agent]
        Q3 --> S[Summarizer Agent]
        Q3 --> V[Verifier Agent]
        Q4 --> PUB[Publisher Agent]
      
        ORCH <--> MEM[Memory Service]
        MEM <--> STM[(Redis STM)]
        MEM <--> LTM[(Cosmos/PG + Vector LTM)]
      
        PUB --> Slack[Slack Webhook]
        PUB --> DB[(DB/Blob)]
        PUB --> EG2[Event: Done/Failed] --> EG
      ```
      
      **(참고) Azure 리소스 위치(포털에서 찾는 경로)**
        1. Event Grid: Azure Portal → Event Grid → Topics / Subscriptions
        2. Service Bus(Queue/Topic): Azure Portal → Service Bus → Queues / Topics
        3. Azure Functions: Azure Portal → Function App
        4. Redis: Azure Portal → Azure Cache for Redis
        5. Cosmos DB: Azure Portal → Azure Cosmos DB
        6. Monitor/Logs: Azure Portal → Monitor → Log Analytics / Application Insights
        
  2. 서브 에이전트 "입력/출력 JSON 계약(Contract)" 템플릿
  
    a. 공통 Envelope (모든 Agent 공통)
    
    ```
    {
      "traceId": "uuid",
      "sessionId": "string",
      "timestamp": "ISO-8601",
      "input": {},
      "context": {
        "userLocale": "ko-KR",
        "tenant": "dev|stg|prd",
        "budget": { "maxTokens": 2000, "maxToolCalls": 5 },
        "security": { "piiAllowed": false }
      }
    }
    ```
    
    b. Router Agent (의도/분기)
    - input
    
    ```
    {
      "message": "사용자 원문",
      "hints": { "channel": "web|slack|app", "knownIntents": ["news", "weather", "content"] }
    }
    ```
    
    - output
    
    ```
    {
      "route": "content_search|qa|action|handoff",
      "confidence": 0.0,
      "signals": ["hasContentTitleLikePhrase", "needsWebSearch"],
      "normalizedQuery": "검색 키워드(정규화된 형태)",
      "language": "ko"
    }
    ```
    
    c. Planner Agent (계획 수립)
    - input
    
    ```
    {
      "goal": "무엇을 달성할지",
      "routeResult": { "route": "content_search", "normalizedQuery": "..." },
      "constraints": { "timeLimitMs": 8000, "noWeb": false }
    }
    ```
    
    - output
    
    ```
    {
      "plan": [
        { "step": 1, "agent": "Retriever", "task": "관련 근거 수집", "inputs": { "query": "..." } },
        { "step": 2, "agent": "Summarizer", "task": "요약 초안", "inputs": { "style": "short" } },
        { "step": 3, "agent": "Verifier", "task": "팩트/정책 검증", "inputs": {} }
      ],
      "stopConditions": { "maxSteps": 6, "failFast": true }
    }
    ```
    
    d. Retriever Agent (근거 수집)
    - input
    
    ```
    {
      "query": "검색어",
      "sources": ["web", "internal_docs"],
      "topK": 5
    }
    ```
    
    - output
    
    ```
    {
      "evidence": [
        {
          "title": "문서/기사 제목",
          "snippet": "핵심 발췌(짧게)",
          "source": "web|internal",
          "url": "가능하면",
          "publishedAt": "ISO-8601",
          "confidence": 0.0
        }
      ],
      "coverage": { "isEnough": true, "missingAngles": ["공식 발표", "가격"] }
    }
    ```
    
    e. Executor Agent (툴 실행)
    - input
    
    ```
    {
      "actions": [
        { "tool": "db.query", "args": { "sql": "..." } },
        { "tool": "slack.send", "args": { "text": "..." } }
      ]
    }
    ```
    
    - output
    
    ```
    {
      "results": [
        { "tool": "db.query", "ok": true, "data": [{ "id": 1 }] },
        { "tool": "slack.send", "ok": true, "data": { "ts": "..." } }
      ],
      "errors": []
    }
    ```
    
    f. Summarizer Agent (요약/서술)
    - input
    
    ```
    {
      "evidence": [/* retriever evidence */],
      "style": "short|bullet|blog",
      "tone": "neutral|friendly",
      "maxChars": 600
    }
    ```
    
    - output
    
    ```
    {
      "draft": "요약 결과 텍스트",
      "keyPoints": ["포인트1", "포인트2"],
      "citations": ["evidence[0]", "evidence[2]"]
    }
    ```
    
    g. Verifier Agent (검증/가드레일)
    - input
    
    ```
    {
      "draft": "초안",
      "evidence": [/* evidence */],
      "rules": { "noPII": true, "mustCite": true, "noHallucination": true }
    }
    ```
    
    - output
    
    ```
    {
      "verdict": "pass|revise|fail",
      "issues": [
        { "type": "missing_citation", "detail": "2번째 문장 출처 필요" },
        { "type": "overclaim", "detail": "단정 표현 완화 필요" }
      ],
      "revisedDraft": "수정본(필요 시)"
    }
    ```
    
    h. Memory Manager (STM/LTM 저장)
    - input
    
    ```
    {
      "op": "read|write|summarize|delete",
      "scope": "stm|ltm",
      "key": "session:xxx",
      "payload": { "notes": "..." }
    }
    ```
    
    - output
    
    ```
    {
      "ok": true,
      "data": { "value": "..." }
    }
    ```
     
  3. 샘플 워크플로우 : "콘텐츠명 추정 -> 검색 -> 요약 -> 검증 -> 공유/저장"
    a. 이벤트/큐 기준 흐름(실제 운영 형태)
      1. API: 사용자 발화 수신 → MessageReceived 이벤트 발행
      2. Router Job(Queue): Router Agent가 콘텐츠명/뉴스/일반QA 분기
      3. content_search면
        - Retrieval Job: Retriever Agent가 웹/내부 검색 근거 수집
        - Summarize Job: Summarizer Agent가 “짧은 요약 + 핵심 포인트” 생성
        - Verify Job: Verifier Agent가 출처/과장/정책 체크 후 pass/revise
      4. Publish Job: Slack/DB/블로그(추후)로 전송 및 저장
      5. 실패 시: DLQ로 보내고 Failed 이벤트 발행(알람)


    b. Router 분기 예시(콘텐츠명 추정 로직)
      - 입력 : "냉부해 보고 싶어"
      - Router Output 예시 : 
      
      ```
      {
        "route": "content_search",
        "confidence": 0.82,
        "signals": ["hasContentTitleLikePhrase", "needsWebSearch"],
        "normalizedQuery": "냉부해 프로그램"
      }
      ```
    
  4. 구현 팁 (Node/Azure에서 "멀티로 갈때" 제일 중요한 것)\
    a. TraceId 필수: 모든 이벤트/큐 메시지에 traceId 넣기
    b. Idempotency Key: 같은 job이 2번 실행돼도 결과가 깨지지 않게(특히 publish)
    c. Timeout/Retry 정책 분리: Retrieval은 재시도 2~3회, Publish는 멱등+짧게
    d. LLM 비용 상한: step별 maxTokens / maxToolCalls 하드 제한
    e. Memory Service 중앙화: 에이전트가 Redis/DB 직접 만지지 말고 서비스로만
    f. Observability: 단계별 latency/에러율/토큰/툴콜 수를 App Insights에 로깅

  **Sample : "오늘 날씨 무드에 맞는 노래랑 영화 추천"**
  1. 처리 흐름도 (동기 Orchestrator 중심)
  <img width="771" height="1326" alt="image" src="https://github.com/user-attachments/assets/13d030f9-b878-487d-85f4-bed533ed62cb" />
  
  ```
  flowchart TD
    U[User: 오늘 날씨 무드에 맞는 노래랑 영화추천] --> API[API Gateway / Fastify]
    API --> ORCH[Orchestrator]
  
    ORCH --> R[Router Agent\n의도/요청 분해]
    R -->|intent=weather_mood_reco| P[Planner Agent\n작업 계획 수립]
  
    P --> W[Weather Agent\n날씨 조회]
    W --> EXE[Executor\nTool Call: Weather API]
    EXE --> W
  
    W --> MOOD[Mood Mapper Agent\n날씨→무드/키워드 변환]
    MOOD --> RET[Retriever Agent\n추천 후보 수집]
    RET --> EXE2[Executor\nTool Call: 음악/영화 DB or 추천 API]
    EXE2 --> RET
  
    RET --> RANK[Ranker Agent\n사용자 제약 반영/정렬]
    RANK --> V[Verifier Agent\n안전/품질 체크]
    V --> S[Composer Agent\n최종 답변 구성]
  
    S --> API --> U
  ```
  
    - 각 Agent가 하는 일
      - Router : 날씨 기반 감성 추천으로 분기 + 입력을 "날씨 조회/ 무드 추출 / 음악 / 영화"로 쪼갬
      - Planner : "날씨->무드->후보 수집->정렬->검증->응답" 플랜 생성
      - Weather Agent : 오늘(사용자 위치 기준) 날씨를 가져옴
      - Mood Mapper : 예) 비/흐림 ->차분/멜랑콜리, 맑음 -> 산뜻/활기
      - Retriever : 노래/영화 후보 리스트를 가져옴(내부 DB, 추천 API, 캐시 등)
      - Ranker : "무드 일치도 + 대중성 + 다양성 + 사용자 선호(장르/공포X 등)"로 정렬
      - Verifier : 과장/금칙/부적절 콘텐츠 필터(사용자 공포 싫어함 같은 정책 반영)
      - Composer : 보기 좋은 포맷으로 추천 + 한 줄 코멘트 +  대체안까지 구성
  
  2. 처리 흐름도 (비동기 Pub/Sub + Queue 버전)
  <img width="276" height="2322" alt="image" src="https://github.com/user-attachments/assets/43b0a994-669c-4dbd-9761-7babbedbe327" />
  
  ```
  flowchart TB
    U[User] --> API[Fastify]
    API --> EV1((Event: MessageReceived))
  
    EV1 --> Q1[(Queue: RouteJob)]
    Q1 --> R[Router]
  
    R --> Q2[(Queue: WeatherJob)]
    Q2 --> W[Weather Agent]
    W --> Q3[(Queue: MoodJob)]
    Q3 --> MOOD[Mood Mapper]
  
    MOOD --> Q4[(Queue: RetrievalJob)]
    Q4 --> RET[Retriever]
  
    RET --> Q5[(Queue: RankVerifyComposeJob)]
    Q5 --> RANK[Ranker]
    RANK --> V[Verifier]
    V --> S[Composer]
  
    S --> Q6[(Queue: PublishJob)]
    Q6 --> OUT[Send Response + Store Logs/Memory]
    OUT --> EV2((Event: Completed/Failed))
  ```
  
  - 특정 단계(예: 추천 후보 수집)가 느려도 큐에 쌓아 처리 가능
  - 실패하면 재시도 / DLQ로 보내고 운영 알람 가능
  
  3. 실제 "응답 포맷" 예시 (멀티 에이전트 결과물 느낌)
    - 오늘 날씨: 흐리고 약한 비 → 무드: 차분/잔잔/집콕
    - 노래 3곡
      1. (잔잔한 피아노/로파이)
      2. (보컬 중심/감성)
      3. (비 오는 날 드라이브)
    - 영화 3편 (공포 제외)
      1. (잔잔/위로)
      2. (감성/로맨스)
      3. (따뜻/힐링)
    - 대체 무드: “우울 말고 리셋 느낌”이면? → 밝은 인디/코미디로 2개 추가


8. Next AI Agent
   - Agent의 한계
     1. 이해가 아니라 패턴 추정 : 의미를 아는 게 아니라 그럴 듯한 다음 행동을 고를 뿐
       - 진짜 원인 이해/ 인과 추론 / 상식적 판단에는 한계
     2. 장기 목표에 약함
       - 단기 목표 O, 단계적 작업 O, 장기 전략 일관성 X
     3. 자기 자신을 제대로 평가 못함 : 반성 흉내는 내나 메타 학습은 못함
     4. 현실 세계와의 간극 : 센서 없음, 몸 없음, 직접 경험 없음
     
   - 다음 Agent
     - **[Model-based Agent] - 세계 모델을 가진 Agent**
       - 내부에 '세상 시뮬레이터'를 가짐
       - 행동 전에 가상으로 여러 미래를 돌려봄
     - **[Collective Intelligence] - 집단 지능 시스템**
       - Agent + 사람 + 규칙 + 피드백 루프
       - 핵심 변화
         - Agent는 사람 판단을 증폭시키는 존재
         - 예시) 패턴 제시, 선택지 비교, 판단을 돕는 구조
     - **[Learning System] - 스스로 변하는 시스템**
       - 실패/성공을 구조적으로 학습
       - 프롬프트/룰/워크플로우를 스스로 조정
       - Agent를 포함한 '시스템'이 학습
     - **[Human-in-the-loop + Value-aligned System]** - 인간 참여형 AI (HITL)
       - Agent가 결정하지 않고, 근거를 만들어 사람이 최종 선택
       - AI를 인간의 가치에 부합하게 유지
       - https://www.holisticai.com/blog/human-in-the-loop-ai

   - 현실적 결론
     - Agent가 인간의 사고 능력을 확장
