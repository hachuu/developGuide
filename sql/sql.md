# SQL 관련 공부 내용

## sql like 검색
```
  SELECT * FROM table where word like '%끝'
```
- [join 예제들](https://cceeun.tistory.com/189)
- [sqld기출](https://stricky.tistory.com/273)


## SQL
- Structured Query Language의 약자로, 데이터베이스에서 데이터를 관리하고 검색하는 데 사용되는 프로그래밍 언어


### 데이터베이스 생성
CREATE DATABASE database_name;

### 테이블 생성
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
    ...
);

### 레코드 삽입
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);

### 레코드 검색
sql
Copy code
SELECT column1, column2, ...
FROM table_name
WHERE condition;

### 레코드 업데이트
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;

### 레코드 삭제
DELETE FROM table_name
WHERE condition;

## join
- SQL에서 테이블 조인(join)은 두 개 이상의 테이블에서 관련 데이터를 결합하여 데이터를 검색하는 기술입니다. 보통은 하나의 테이블에 모든 정보를 저장하지 않기 때문에 여러 개의 테이블을 조인하여 필요한 정보를 가져오는 것이 필요합니다.

### INNER JOIN
- 두 개의 테이블에서 서로 일치하는 값을 가져옵니다.
SELECT *
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;

### LEFT JOIN
- 왼쪽 테이블의 모든 레코드를 가져온 후, 오른쪽 테이블에서 일치하는 값이 있는 경우 오른쪽 테이블의 값을 함께 가져옵니다.
SELECT *
FROM table1
LEFT JOIN table2
ON table1.column_name = table2.column_name;

### RIGHT JOIN
- 오른쪽 테이블의 모든 레코드를 가져온 후, 왼쪽 테이블에서 일치하는 값이 있는 경우 왼쪽 테이블의 값을 함께 가져옵니다.
SELECT *
FROM table1
RIGHT JOIN table2
ON table1.column_name = table2.column_name;

### FULL OUTER JOIN
- 두 테이블의 모든 레코드를 가져옵니다.
SELECT *
FROM table1
FULL OUTER JOIN table2
ON table1.column_name = table2.column_name;
- 위의 쿼리문에서 *는 모든 열을 선택하는 것을 의미합니다. 원하는 열을 선택하려면 SELECT 절에서 원하는 열 이름을 지정하면 됩니다.
- 또한, ON 절에서는 두 테이블 간에 일치하는 열 이름을 지정해야합니다. 이것은 두 테이블 간의 조인 기준이 되는 열입니다. 일치하는 값을 찾아 연결할 수 있도록 해당 열의 값이 동일해야합니다.
