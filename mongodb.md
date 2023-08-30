# MongoDB 교육

https://www.notion.so/MongoDB-e0b4626dbc1f4909b858556c38eff514

### 데이터베이스 트랜드

- DB-Ranking
    - 1위 오라클
    - 3위 Microsoft SQL Server
    - 5위 몽고db

| DBMS | 오라클 | SQL Server |
| --- | --- | --- |
| Database Model | Relational DBMS, Multi-model | Relational DBMS, Multi-model |
| Multi-model | Document store, Graph DBMS, RDF store, Spatial DBMS |  Document store, Graph DBMS, Spatial DBMS |

> 관계형 데이터베이스는 인덱스로 키나, 레인지로 검색하는데
요새 db트랜드는 ai의 영향으로 유사도 검색이 트랜딩함 ex) Snowflake
> 

AWS와 PostgreSQL 연관에 의해 오픈소스 연계형 DBMS를 많이 씀

RDBMS - 오픈 DBMS에는 PostgreSQL과 MariaDB가 있고 / 상용에는 ORACLE, SQL Server, Tibero, MySQL…

|  | RDBMS  | NoSQL |
| --- | --- | --- |
|  | 상용 ORACLE, SQL Server, Tibero, MySQL 오픈 PostgreSQL, MariaDB | Redis MongoDB Cassandra influxDB Ne |
| 특징 | 복잡한 트랜잭션 및 조인 데이터 품질 | 유연한 스키마 Scale-Out 확장 데이터 성능 |

## MongoDB

- 활용
    - 로그
    - Big Data
    - Content Management and Delivery
    - Mobile and Social Infrastructure
    - Data Hub
    - 기가지니에도 MongoDB를 쓴다고?!

### RDBMS ⇒ MongoDB

- 테이블 Table ⇒ 컬렉션 Collection
- 튜플/로우 Tuple/Row ⇒ 다큐먼트 Document
- 칼럼 Column ⇒ 필드 Field
- 테이블 조인 Table Join ⇒ Embedded Documents
    - Embedded Documents : 필드 안에 또 다른  document를 내포할 수 있음
- Primary Key ⇒ ‘_id’ default 제공 (중복이 생기지 않도록 기본적으로 제공되는 값)
- Array 필드 가져올때는 <array>.<index>로 가져옴 ex) contrib.2
- embedded documents를 가져올 때는 <embedded document>.<field> ex) name.last, contact.phone.number

### Document 제약사항

- 사이즈 16MB
- _id field 는 항상 document의 첫번째 순서
- _id field를 생략하고 document 입력시 자동으로 ObjectId로 추가됨

- 실습 (설치)
    1. 데이터베이스와 컬렉션 생성
        - use myNewDB
        - show dbs (collection 생성하지 않으면 리스트에 보이지 않음)
        - db.myNewCollection1.insertOne( {x:1} )
    2. 몽고 db 설치  https://www.mongodb.com/try/download/community
    3. 몽고 쉘 설치 Tool > Shell 설치 https://www.mongodb.com/try/download/shell
    4. (몽고 Compass (GUI) 2번 몽고 db 설치 시 자동 설치 됨)

- mongsosh
    - 환경변수 등록 사용자변수 > D:\mongosh\bin
    - cmd에 mongosh라고 치면 자동 연결됨
    - use myNewDB하면 데이터베이스 myNewDB로 변경됨
    

### 관계형 데이터베이스 CRUD 오퍼레이션 지원

### CRUD

- CREATE Insert

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6d8c8ebc-027f-4942-ba6e-c503ca30a22a/Untitled.png)

- insertMany

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8f5cdd36-8617-4d06-9f4b-60e7cc9abc62/Untitled.png)

- insertOne (한개의 document)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/723b1ddb-87e2-4bd0-9b53-f224e390d7bd/Untitled.png)

- Read select
    - where 1번째 조건 ex) {age:{$gt:18}} age가 18 초과
    - projection 2번째 조건 ex) {name:1, age:1, _id:0, status:1} 1은 보여줌 0은 안보여줌
    - and는 ,로 표현하고 or는 $or로 표현

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c1a79754-6c24-42ae-b617-24c6dd8da7b1/Untitled.png)

- sort

```jsx
test> db.inventory.find().sort({qty: 1}) //정순
test> db.inventory.find().sort({qty: -1}) //역순
test> db.inventory.find().sort({qty: 1}).limit(3) // 정순에 top 3개만 출력
```

- Update update
    - db.collection.updateOne
    
    ```jsx
    test> db.inventory.updateOne(
    ...    { item: "paper" },
    ...    {
    ...      $set: { "size.uom": "cm", status: "P" },
    ...      $currentDate: { lastModified: true }
    ...    }
    ... )
    {
      acknowledged: true,
      insertedId: null,
      matchedCount: 1,
      modifiedCount: 1,
      upsertedCount: 0
    }
    ```
    
    - db.collection.updateMany
    
    ```jsx
    test> db.inventory.updateMany(
    ... { status:'P'}, {$set: {status :'A'}})
    {
      acknowledged: true,
      insertedId: null,
      matchedCount: 3,
      modifiedCount: 3,
      upsertedCount: 0
    }
    ```
    
    - db.collection.replaceOne 하나의 document를 다른 document로 replace하겠다는 의미
    
    ```jsx
    test> db.inventory.find({item:'paper'})
    [
      {
        _id: ObjectId("64eecf33387e1233b74fa564"),
        item: 'paper',
        qty: 100,
        size: { h: 8.5, w: 11, uom: 'cm' },
        status: 'A',
        lastModified: ISODate("2023-08-30T05:10:49.086Z")
      }
    ]
    test> db.inventory.replaceOne(
    ... {item: 'paper'},
    ... {item: 'paper', instock: [{warehouse :'A', qty: 60}, {warehouse: 'B', qty:40}]}
    ... )
    {
      acknowledged: true,
      insertedId: null,
      matchedCount: 1,
      modifiedCount: 1,
      upsertedCount: 0
    }
    test> db.inventory.find({item:'paper'})
    [
      {
        _id: ObjectId("64eecf33387e1233b74fa564"),
        item: 'paper',
        instock: [ { warehouse: 'A', qty: 60 }, { warehouse: 'B', qty: 40 } ]
      }
    ]
    ```
    
    - 필드값을 수정하기 위해 $set과 같은 update 연산자를 제공함
    - $set과 같은 update 연산자는 필드가 존재하지 않으면 필드를 생성함
- Delete delete
    - deleteMany는 모든 documents 삭제
    
    ```jsx
    test> db.inventory.find({status:'A'}).count()
    4
    test> db.inventory.deleteMany({status:'A'})
    { acknowledged: true, deletedCount: 4 }
    test> db.inventory.find({status:'A'}).count()
    0
    ```
    
    - deleteOne 첫 번째 document 삭제
    
    ```jsx
    test> db.inventory.deleteOne({status:'A'})
    { acknowledged: true, deletedCount: 1 }
    ```
    
- drop
    
    ```jsx
    db.inventory.drop()
    ```
    

### SQL 과 MongoDB의 차이

https://www.mongodb.com/docs/manual/reference/sql-comparison/

### MongoDb Data Modeling

- 핵심 고려 사항
    - Embedded
    - References (관계형 데이터베이스에서의 참조 방식을 mongodb에서도 사용 가능하다)

- config
- replication
    - d드라이브에 mongdo\data01, data02, data03 경로를 만들고 hosts파일에서 추가한다.
    
    ```jsx
    # Copyright (c) 1993-2009 Microsoft Corp.
    #
    # This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
    #
    # This file contains the mappings of IP addresses to host names. Each
    # entry should be kept on an individual line. The IP address should
    # be placed in the first column followed by the corresponding host name.
    # The IP address and the host name should be separated by at least one
    # space.
    #
    # Additionally, comments (such as these) may be inserted on individual
    # lines or following the machine name denoted by a '#' symbol.
    #
    # For example:
    #
    #      102.54.94.97     rhino.acme.com          # source server
    #       38.25.63.10     x.acme.com              # x client host
    
    # localhost name resolution is handled within DNS itself.
    #	127.0.0.1       localhost
    #	::1             localhost
    127.0.0.1 mongodb0.example.net
    127.0.0.1 mongodb1.example.net
    127.0.0.1 mongodb2.example.net
    ```
    
    - 서비스에서 mongodb 속성에서 config 파일 확인하고, MongoDB Server (MongoDB) 중지, 속성에서 시작유형을 수동으로 바꿔줌
    
    [mongod.cfg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6d5199bc-2c46-424c-a16b-75295716734d/mongod.cfg)
    
    - 환경 변수에 C:\Program Files\MongoDB\Server\7.0\bin 추가
    - cmd에서 아래 명령어 입력
    
    ```jsx
    mongod --replSet "rs0" --bind_ip localhost --dbpath d:\mongodb\data01 --port 27017
    mongod --replSet "rs0" --bind_ip localhost --dbpath d:\mongodb\data02 --port 27018
    mongod --replSet "rs0" --bind_ip localhost --dbpath d:\mongodb\data03 --port 27019
    
    ```
    
    - 복제셋 초기화
    
    ```jsx
    test> rs.initiate( { _id : "rs0", members : [ {_id:0, host :"mongodb0.example.net:27017"}, {_id:1, host :"mongodb1.example.net:27018"}, {_id:2, host :"mongodb2.example.net:27019"} ] })
    { ok: 1 }
    rs0 [direct: other] test> rs.conf()
    ```
    

![캡처.PNG](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4a21f149-a47f-4cf6-b712-e2782482a516/%EC%BA%A1%EC%B2%98.png)

![캡처3.PNG](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9ede6aa0-0053-4517-aac5-450927a1d1b7/%EC%BA%A1%EC%B2%983.png)

- primary인 mongodb0 27017 서버를 죽여도 조회하면 잘 나옴
    - 복제셋 과반수 이상 서버가 살아 있어야 문제 없이 작동됨, 2개 서버를 죽이면 동작 안함

### 실습 내용

- 실습 query
```
  test> db.inventory.insertMany( [
...    { item: "canvas", qty: 100, size: { h: 28, w: 35.5, uom: "cm" }, status: "A" },
...    { item: "journal", qty: 25, size: { h: 14, w: 21, uom: "cm" }, status: "A" },
...    { item: "mat", qty: 85, size: { h: 27.9, w: 35.5, uom: "cm" }, status: "A" },
...    { item: "mousepad", qty: 25, size: { h: 19, w: 22.85, uom: "cm" }, status: "P" },
...    { item: "notebook", qty: 50, size: { h: 8.5, w: 11, uom: "in" }, status: "P" },
...    { item: "paper", qty: 100, size: { h: 8.5, w: 11, uom: "in" }, status: "D" },
...    { item: "planner", qty: 75, size: { h: 22.85, w: 30, uom: "cm" }, status: "D" },
...    { item: "postcard", qty: 45, size: { h: 10, w: 15.25, uom: "cm" }, status: "A" },
...    { item: "sketchbook", qty: 80, size: { h: 14, w: 21, uom: "cm" }, status: "A" },
...    { item: "sketch pad", qty: 95, size: { h: 22.85, w: 30.5, uom: "cm" }, status: "A" }
... ] )
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId("64eecf33387e1233b74fa55f"),
    '1': ObjectId("64eecf33387e1233b74fa560"),
    '2': ObjectId("64eecf33387e1233b74fa561"),
    '3': ObjectId("64eecf33387e1233b74fa562"),
    '4': ObjectId("64eecf33387e1233b74fa563"),
    '5': ObjectId("64eecf33387e1233b74fa564"),
    '6': ObjectId("64eecf33387e1233b74fa565"),
    '7': ObjectId("64eecf33387e1233b74fa566"),
    '8': ObjectId("64eecf33387e1233b74fa567"),
    '9': ObjectId("64eecf33387e1233b74fa568")
  }
}
test> db.inventory.updateOne(
...    { item: "paper" },
...    {
...      $set: { "size.uom": "cm", status: "P" },
...      $currentDate: { lastModified: true }
...    }
... )
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
test> db.collection.find()

test> db.inventory.find()
[
  {
    _id: ObjectId("64eecf33387e1233b74fa55f"),
    item: 'canvas',
    qty: 100,
    size: { h: 28, w: 35.5, uom: 'cm' },
    status: 'A'
  },
  {
    _id: ObjectId("64eecf33387e1233b74fa560"),
    item: 'journal',
    qty: 25,
    size: { h: 14, w: 21, uom: 'cm' },
    status: 'A'
  },
  {
    _id: ObjectId("64eecf33387e1233b74fa561"),
    item: 'mat',
    qty: 85,
    size: { h: 27.9, w: 35.5, uom: 'cm' },
    status: 'A'
  },
  {
    _id: ObjectId("64eecf33387e1233b74fa562"),
    item: 'mousepad',
    qty: 25,
    size: { h: 19, w: 22.85, uom: 'cm' },
    status: 'P'
  },
  {
    _id: ObjectId("64eecf33387e1233b74fa563"),
    item: 'notebook',
    qty: 50,
    size: { h: 8.5, w: 11, uom: 'in' },
    status: 'P'
  },
  {
    _id: ObjectId("64eecf33387e1233b74fa564"),
    item: 'paper',
    qty: 100,
    size: { h: 8.5, w: 11, uom: 'cm' },
    status: 'P',
    lastModified: ISODate("2023-08-30T05:10:49.086Z")
  },
  {
    _id: ObjectId("64eecf33387e1233b74fa565"),
    item: 'planner',
    qty: 75,
    size: { h: 22.85, w: 30, uom: 'cm' },
    status: 'D'
  },
  {
    _id: ObjectId("64eecf33387e1233b74fa566"),
    item: 'postcard',
    qty: 45,
    size: { h: 10, w: 15.25, uom: 'cm' },
    status: 'A'
  },
  {
    _id: ObjectId("64eecf33387e1233b74fa567"),
    item: 'sketchbook',
    qty: 80,
    size: { h: 14, w: 21, uom: 'cm' },
    status: 'A'
  },
  {
    _id: ObjectId("64eecf33387e1233b74fa568"),
    item: 'sketch pad',
    qty: 95,
    size: { h: 22.85, w: 30.5, uom: 'cm' },
    status: 'A'
  }
]
test> db.inventory.updateMany(
... { status:'P'}, {$set: {status :'A'}})
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 3,
  modifiedCount: 3,
  upsertedCount: 0
}
test> db.inventory.updateMany( { status: 'P' }, { $set: { status: 'A' } })
test>
(To exit, press Ctrl+C again or Ctrl+D or type .exit)
test>

C:\Users\User>

C:\Users\User>

C:\Users\User>mongosh
Current Mongosh Log ID: 64eed100709fec8a9e1612e7
Connecting to:          mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.10.6
Using MongoDB:          7.0.0
Using Mongosh:          1.10.6

For mongosh info see: https://docs.mongodb.com/mongodb-shell/

------
   The server generated these startup warnings when booting
   2023-08-30T11:04:54.935+09:00: Access control is not enabled for the database. Read and write access to data and configuration is unrestricted
------

test> db.inventory.updateMany( {'qty': {$lt: 50}}, { $set: {"size.uom": "in", status : "p"}, $currentDate: {lastModified:true}})
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 3,
  modifiedCount: 3,
  upsertedCount: 0
}
test> show databases
admin     40.00 KiB
config   108.00 KiB
local     72.00 KiB
myNewDB  112.00 KiB
test      56.00 KiB
test> db.inventory.find()
[
  {
    _id: ObjectId("64eecf33387e1233b74fa55f"),
    item: 'canvas',
    qty: 100,
    size: { h: 28, w: 35.5, uom: 'cm' },
    status: 'A'
  },
  {
    _id: ObjectId("64eecf33387e1233b74fa560"),
    item: 'journal',
    qty: 25,
    size: { h: 14, w: 21, uom: 'in' },
    status: 'p',
    lastModified: ISODate("2023-08-30T05:19:57.286Z")
  },
  {
    _id: ObjectId("64eecf33387e1233b74fa561"),
    item: 'mat',
    qty: 85,
    size: { h: 27.9, w: 35.5, uom: 'cm' },
    status: 'A'
  },
  {
    _id: ObjectId("64eecf33387e1233b74fa562"),
    item: 'mousepad',
    qty: 25,
    size: { h: 19, w: 22.85, uom: 'in' },
    status: 'p',
    lastModified: ISODate("2023-08-30T05:19:57.286Z")
  },
  {
    _id: ObjectId("64eecf33387e1233b74fa563"),
    item: 'notebook',
    qty: 50,
    size: { h: 8.5, w: 11, uom: 'in' },
    status: 'A'
  },
  {
    _id: ObjectId("64eecf33387e1233b74fa564"),
    item: 'paper',
    qty: 100,
    size: { h: 8.5, w: 11, uom: 'cm' },
    status: 'A',
    lastModified: ISODate("2023-08-30T05:10:49.086Z")
  },
  {
    _id: ObjectId("64eecf33387e1233b74fa565"),
    item: 'planner',
    qty: 75,
    size: { h: 22.85, w: 30, uom: 'cm' },
    status: 'D'
  },
  {
    _id: ObjectId("64eecf33387e1233b74fa566"),
    item: 'postcard',
    qty: 45,
    size: { h: 10, w: 15.25, uom: 'in' },
    status: 'p',
    lastModified: ISODate("2023-08-30T05:19:57.286Z")
  },
  {
    _id: ObjectId("64eecf33387e1233b74fa567"),
    item: 'sketchbook',
    qty: 80,
    size: { h: 14, w: 21, uom: 'cm' },
    status: 'A'
  },
  {
    _id: ObjectId("64eecf33387e1233b74fa568"),
    item: 'sketch pad',
    qty: 95,
    size: { h: 22.85, w: 30.5, uom: 'cm' },
    status: 'A'
  }
]
test> db.inventory.find({ 'size.uom': 'in'})
[
  {
    _id: ObjectId("64eecf33387e1233b74fa560"),
    item: 'journal',
    qty: 25,
    size: { h: 14, w: 21, uom: 'in' },
    status: 'p',
    lastModified: ISODate("2023-08-30T05:19:57.286Z")
  },
  {
    _id: ObjectId("64eecf33387e1233b74fa562"),
    item: 'mousepad',
    qty: 25,
    size: { h: 19, w: 22.85, uom: 'in' },
    status: 'p',
    lastModified: ISODate("2023-08-30T05:19:57.286Z")
  },
  {
    _id: ObjectId("64eecf33387e1233b74fa563"),
    item: 'notebook',
    qty: 50,
    size: { h: 8.5, w: 11, uom: 'in' },
    status: 'A'
  },
  {
    _id: ObjectId("64eecf33387e1233b74fa566"),
    item: 'postcard',
    qty: 45,
    size: { h: 10, w: 15.25, uom: 'in' },
    status: 'p',
    lastModified: ISODate("2023-08-30T05:19:57.286Z")
  }
]
test> db.inventory.find({item:'paper'})
[
  {
    _id: ObjectId("64eecf33387e1233b74fa564"),
    item: 'paper',
    qty: 100,
    size: { h: 8.5, w: 11, uom: 'cm' },
    status: 'A',
    lastModified: ISODate("2023-08-30T05:10:49.086Z")
  }
]
test> db.inventory.replaceOne(
... {item: 'paper'},
... {item: 'paper', instock: [{warehouse :'A', qty: 60}, {warehouse: 'B', qty:40}]}
... )
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
test> db.inventory.find({item:'paper'})
[
  {
    _id: ObjectId("64eecf33387e1233b74fa564"),
    item: 'paper',
    instock: [ { warehouse: 'A', qty: 60 }, { warehouse: 'B', qty: 40 } ]
  }
]
test> db.inventory.deleteOne({status:'A'})
{ acknowledged: true, deletedCount: 1 }
test> db.inventory.find({status:'A'})
[
  {
    _id: ObjectId("64eecf33387e1233b74fa561"),
    item: 'mat',
    qty: 85,
    size: { h: 27.9, w: 35.5, uom: 'cm' },
    status: 'A'
  },
  {
    _id: ObjectId("64eecf33387e1233b74fa563"),
    item: 'notebook',
    qty: 50,
    size: { h: 8.5, w: 11, uom: 'in' },
    status: 'A'
  },
  {
    _id: ObjectId("64eecf33387e1233b74fa567"),
    item: 'sketchbook',
    qty: 80,
    size: { h: 14, w: 21, uom: 'cm' },
    status: 'A'
  },
  {
    _id: ObjectId("64eecf33387e1233b74fa568"),
    item: 'sketch pad',
    qty: 95,
    size: { h: 22.85, w: 30.5, uom: 'cm' },
    status: 'A'
  }
]
test> db.inventory.find({status:'A'}).count()
4
test> db.inventory.deleteMany({status:'A'})
{ acknowledged: true, deletedCount: 4 }
test> db.inventory.find({status:'A'}).count()
0
```
