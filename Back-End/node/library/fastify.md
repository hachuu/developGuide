# 기능 설명

## Request/Reply 훅

- 순서
  1. onRequest
  2. preParsing
  3. preValidation
  4. preHandler
  5. handler

- 사용 방법
  1. fastify.addHook('preValidation')
    - 검증 단계 전에 실행
    - 요청 객체에 데이터 부가
  
