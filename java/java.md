# JAVA 정리

## java 비동기식 처리

```java
public class Main {
	public static void main(String[] args) {
	    Thread thread1 = new Thread(()-> method_1);
	    Thread thread2 = new Thread(()-> method_2);
	    Thread thread3 = new Thread(()-> method_3);
	    Thread thread4 = new Thread(()-> method_4);

	    thread1.start();
	    thread2.start();
	    thread3.start();
	    thread4.start();
  	}

  	public static void method_1() {
	    try {
	        System.out.println("start method_1");
	        Thread.sleep(1000);
	        System.out.println("end method_1");
	    } catch (InterruptedException e) {
	        e.printStackTrace();
	    }
	}

	public static void method_2() {
	    try {
	        System.out.println("start method_2");
	        Thread.sleep(1000);
	        System.out.println("end method_2");
	    } catch (InterruptedException e) {
	        e.printStackTrace();
	    }
	}

	public static void method_3() {
	    try {
	        System.out.println("start method_3");
	        Thread.sleep(1000);
	        System.out.println("end method_3");
	    } catch (InterruptedException e) {
	        e.printStackTrace();
	    }
	}

	public static void method_4() {
	    try {
	        System.out.println("start method_4");
	        Thread.sleep(1000);
	        System.out.println("end method_4");
	    } catch (InterruptedException e) {
	        e.printStackTrace();
	    }
	}
}


```

### java CompletableFuture.runAsync
- Thread로 구현하지 않아도 java 비동기식 호출 가능
- [Java - CompletableFuture 사용 방법](https://codechacha.com/ko/java-completable-future/)
- [CompletableFuture - 안정적 비동기 프로그래밍에 대해 - (1)](https://pjh3749.tistory.com/280)

### Spring boot 라이브러리 java 비동기식 호출 방법
- [Spring Boot @Async 어떻게 동작하는가?](https://brunch.co.kr/@springboot/401)

### 로드밸런서 
[대용량 세션을 위한 로드밸런서](https://d2.naver.com/helloworld/605418)

### HashMap, ArrayList, LinkedList 비교
```
HashMap은 Key, Value 쌍을 가지는 데이터를 관리할 때
ArrayList는 데이터가 입력 되고 삭제가 빈번하지 않은 경우
Linkedlist는 Queue와 같이 Head와 Read와 가까이에서 탐색, 삭제가 이뤄지는 경우
```
[출처: HashMap, ArrayList, LinkedList 속도 비교](https://nnoco.tistory.com/73)

#### java time delay 방법
- [자바에서 몇 초를 지연시키는 방법](https://www.delftstack.com/ko/howto/java/how-to-delay-few-seconds-in-java/)

#### spring 기본 개념
[Spring이란](https://jerryjerryjerry.tistory.com/62)

#### JPA
[[JPA] JPA란](https://gmlwjd9405.github.io/2019/08/04/what-is-jpa.html)
