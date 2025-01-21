# psql
- 정의 : psql은 PostgreSQL 데이터베이스에 접속하고 쿼리를 실행하는 명령 줄 도구

## psql 명령어
```
psql -U [사용자 이름]: PostgreSQL 데이터베이스에 접속합니다. -U 옵션을 사용하여 사용자 이름을 지정할 수 있습니다.

\l: 현재 서버에 있는 데이터베이스 목록을 표시합니다.

\c [데이터베이스 이름]: 지정된 데이터베이스에 연결합니다.

\dt: 현재 데이터베이스의 모든 테이블 목록을 표시합니다.

\d [테이블 이름]: 지정된 테이블의 정보를 표시합니다.

\q: psql을 종료합니다.

SELECT: 데이터를 검색합니다. 
예를 들어, SELECT * FROM mytable;은 mytable 테이블에서 모든 데이터를 선택합니다.

INSERT INTO: 데이터를 삽입합니다. 
예를 들어, INSERT INTO mytable (column1, column2) VALUES ('value1', 'value2');은 mytable 테이블에 column1과 column2에 각각 'value1'과 'value2' 값을 가진 새로운 행을 삽입합니다.

UPDATE: 데이터를 업데이트합니다. 
예를 들어, UPDATE mytable SET column1 = 'newvalue' WHERE column2 = 'somevalue';는 mytable 테이블에서 column2가 'somevalue'인 모든 행의 column1 값을 'newvalue'로 업데이트합니다.

DELETE FROM: 데이터를 삭제합니다. 
예를 들어, DELETE FROM mytable WHERE column1 = 'somevalue';는 mytable 테이블에서 column1이 'somevalue'인 모든 행을 삭제합니다.
```
