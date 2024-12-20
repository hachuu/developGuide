### Interceptor

- Controller 클래스에서 메서드가 두 경로를 모두 처리하도록 설정할 수 있습니다.
- 이렇게 하면 /api/sample/getSomething /api/sample/catch/getSomething 경로로 들어오는 요청을 동일한 메서드에서 처리할 수 있습니다.
```java
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/sample")
public class SampleController {

    @RequestMapping(value = {"/getSomething", "/catch/getSomething"}, method = RequestMethod.GET)
    public String getSomething(@RequestParam String param) {
        // 여기서 param은 복호화된 상태로 전달됩니다.
        return "Publisher List: " + param;
    }
}
```

- Interceptor를 이용한 암호화 및 JWT 토큰 검증
- 위의 설정을 기반으로 인터셉터를 사용하여 파라미터 복호화 및 JWT 토큰 검증을 수행할 수 있습니다. 이렇게 하면 두 경로 모두 동일한 검증 로직을 적용할 수 있습니다.

- RequestInterceptor.java

```java
import org.springframework.stereotype.Component;
import org.springframework.web.servlet.HandlerInterceptor;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.Map;

@Component
public class RequestInterceptor implements HandlerInterceptor {

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        String uri = request.getRequestURI();
        if (uri.contains("/catch/")) {
            // JWT 토큰 검사
            String token = request.getHeader("Authorization");
            if (token == null || token.isEmpty() || !validateJwtToken(token)) {
                response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "Invalid JWT token");
                return false;
            }

            // 파라미터 복호화
            Map<String, String[]> params = request.getParameterMap();
            for (Map.Entry<String, String[]> entry : params.entrySet()) {
                String[] values = entry.getValue();
                for (int i = 0; i < values.length; i++) {
                    values[i] = EncryptionUtil.decrypt(values[i]);
                }
            }
        }
        return true;
    }

    private boolean validateJwtToken(String token) {
        try {
            JwtUtil.validateToken(token);
            return true;
        } catch (Exception e) {
            return false;
        }
    }
}
```
- WebConfig.java
- 인터셉터를 등록하여 /api/audioBook/gapp/* 경로로 들어오는 요청을 가로챕니다.

```java

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfig implements WebMvcConfigurer {

    @Autowired
    private RequestInterceptor requestInterceptor;

    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(requestInterceptor)
                .addPathPatterns("/api/audioBook/gapp/*");
    }
}
```
- 이 설정을 통해 /api/sample/getSomething /api/sample/catch/getSomething 경로로 들어오는 요청은 동일한 컨트롤러 메서드에서 처리되며, /api/sample/catch/* 경로로 들어오는 요청은 인터셉터를 통해 JWT 토큰 검사와 파라미터 복호화 작업을 거치게 됩니다.


- SampleController.java
```java

import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/audioBook")
public class AudioBookController {

    @RequestMapping(value = {"/getSomething", "/catch/getSomething"}, method = RequestMethod.GET)
    public String getSomething(@RequestParam String param) {
        // 여기서 param은 복호화된 상태로 전달됩니다.
        return "Publisher List: " + param;
    }
}
```
- RequestInterceptor.java
```java

import org.springframework.stereotype.Component;
import org.springframework.web.servlet.HandlerInterceptor;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.Map;

@Component
public class RequestInterceptor implements HandlerInterceptor {

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        String uri = request.getRequestURI();
        if (uri.contains("/catch/")) {
            // JWT 토큰 검사
            String token = request.getHeader("Authorization");
            if (token == null || token.isEmpty() || !validateJwtToken(token)) {
                response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "Invalid JWT token");
                return false;
            }

            // 파라미터 복호화
            Map<String, String[]> params = request.getParameterMap();
            for (Map.Entry<String, String[]> entry : params.entrySet()) {
                String[] values = entry.getValue();
                for (int i = 0; i < values.length; i++) {
                    values[i] = EncryptionUtil.decrypt(values[i]);
                }
            }
        }
        return true;
    }

    private boolean validateJwtToken(String token) {
        try {
            JwtUtil.validateToken(token);
            return true;
        } catch (Exception e) {
            return false;
        }
    }
}
```
- WebConfig.java
```java

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfig implements WebMvcConfigurer {

    @Autowired
    private RequestInterceptor requestInterceptor;

    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(requestInterceptor)
                .addPathPatterns("/api/sample/catch/*");
    }
}
```
- 이 구성을 통해 두 경로를 동일한 메서드에서 처리하고, /gapp/* 경로로 들어오는 요청에 대해 인터셉터를 통해 추가 검증 및 복호화 작업을 수행할 수 있습니다.

### AOP

- AOP를 사용하여 특정 경로로 들어오는 요청에 대해 파라미터 복호화와 JWT 토큰 검증을 수행한 후 원래의 컨트롤러 메서드로 전달하는 방법을 구현해 보겠습니다. AOP를 사용하면 메서드 호출을 가로채서 필요한 작업을 수행할 수 있지만, 경로를 변경하지 않고 동일한 경로로 요청을 처리하게 됩니다.

- 다음은 AOP를 사용하여 /api/sample/catch/* 경로로 들어오는 요청을 처리하는 예시입니다.

1. AOP 설정
- RequestInterceptorAspect.java
- AOP를 사용하여 요청을 가로채고, 필요한 검증과 파라미터 복호화를 수행합니다.

```java

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.ServletRequestAttributes;
import java.util.Map;

@Aspect
@Component
public class RequestInterceptorAspect {

    @Around("execution(* com.example.SampleController.*(..)) && @annotation(org.springframework.web.bind.annotation.RequestMapping)")
    public Object interceptRequests(ProceedingJoinPoint joinPoint) throws Throwable {
        ServletRequestAttributes attributes = (ServletRequestAttributes) RequestContextHolder.getRequestAttributes();
        HttpServletRequest request = attributes.getRequest();
        HttpServletResponse response = attributes.getResponse();

        String uri = request.getRequestURI();
        if (uri.startsWith("/api/sample/catch/")) {
            // JWT 토큰 검사
            String token = request.getHeader("Authorization");
            if (token == null || token.isEmpty() || !validateJwtToken(token)) {
                response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "Invalid JWT token");
                return null;
            }

            // 파라미터 복호화
            Map<String, String[]> params = request.getParameterMap();
            for (Map.Entry<String, String[]> entry : params.entrySet()) {
                String[] values = entry.getValue();
                for (int i = 0; i < values.length; i++) {
                    values[i] = EncryptionUtil.decrypt(values[i]);
                }
            }
        }

        return joinPoint.proceed();
    }

    private boolean validateJwtToken(String token) {
        try {
            JwtUtil.validateToken(token);
            return true;
        } catch (Exception e) {
            return false;
        }
    }
}
```
2. 컨트롤러
- 컨트롤러 메서드에서 두 경로를 모두 처리하도록 설정합니다.

```java

import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/sample")
public class SampleController {

    @RequestMapping(value = {"/getSomething", "/catch/getSomething"}, method = RequestMethod.GET)
    public String getSomething(@RequestParam String param) {
        // 여기서 param은 복호화된 상태로 전달됩니다.
        return "Publisher List: " + param;
    }
}
```

3. 유틸리티 클래스
- 파라미터 암호화/복호화와 JWT 토큰 검증을 위한 유틸리티 클래스도 정의합니다.

- EncryptionUtil.java
```java
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;

public class EncryptionUtil {
    private static final String KEY = "1234567890123456"; // 16-byte key

    public static String encrypt(String strToEncrypt) {
        try {
            Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
            final SecretKeySpec secretKey = new SecretKeySpec(KEY.getBytes(), "AES");
            cipher.init(Cipher.ENCRYPT_MODE, secretKey);
            return Base64.getEncoder().encodeToString(cipher.doFinal(strToEncrypt.getBytes("UTF-8")));
        } catch (Exception e) {
            throw new RuntimeException("Error while encrypting: " + e.toString());
        }
    }

    public static String decrypt(String strToDecrypt) {
        try {
            Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5PADDING");
            final SecretKeySpec secretKey = new SecretKeySpec(KEY.getBytes(), "AES");
            cipher.init(Cipher.DECRYPT_MODE, secretKey);
            return new String(cipher.doFinal(Base64.getDecoder().decode(strToDecrypt)));
        } catch (Exception e) {
            throw new RuntimeException("Error while decrypting: " + e.toString());
        }
    }
}
```
- JwtUtil.java
```java
import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;

public class JwtUtil {
    private static final String SECRET_KEY = "mySecretKey";

    public static Claims validateToken(String token) {
        return Jwts.parser()
                .setSigningKey(SECRET_KEY)
                .parseClaimsJws(token)
                .getBody();
    }
}
```

- 이 구성을 통해 /api/sample/getSomething /api/sample/catch/getSomething 경로로 들어오는 요청은 동일한 컨트롤러 메서드에서 처리됩니다. /api/sample/catch/* 경로로 들어오는 요청에 대해서는 AOP를 사용하여 JWT 토큰 검사와 파라미터 복호화 작업을 수행합니다. 이렇게 하면 동일한 로직을 여러 경로에서 재사용할 수 있습니다.


## 결론
- AOP와 인터셉터는 모두 특정 로직을 재사용 가능하게 하고, 공통된 기능을 여러 경로에서 적용할 수 있도록 해줍니다. 그러나 두 접근 방식에는 약간의 차이가 있습니다.

- AOP vs. Interceptor
### AOP
장점:
강력한 기능: 특정 메서드 호출을 전후로 또는 예외 발생 시점 등에 대해 다양한 시점에서 코드를 실행할 수 있습니다.
모듈성: 공통 관심사를 모듈화하여 핵심 비즈니스 로직과 분리할 수 있습니다.
단점:
복잡성: 설정 및 디버깅이 상대적으로 복잡할 수 있습니다.
HTTP 요청/응답에 대한 세부 제어가 어려움: HTTP 레벨에서의 세밀한 제어가 필요한 경우에는 제한적일 수 있습니다.
### Interceptor
- 장점:
HTTP 요청/응답 처리: HTTP 요청 및 응답을 직접적으로 다룰 수 있어 웹 레이어에서의 제어가 용이합니다.
단순성: 설정과 사용이 비교적 간단합니다.
- 단점:
범용성: 메서드 호출 전후의 로직 적용 등, HTTP 요청/응답 이외의 범위에 대해서는 제한적입니다.
범용적 확장 가능성
인터셉터는 HTTP 요청/응답을 처리하는 데 매우 적합하지만, 메서드 호출 전후의 공통 로직을 처리하는 데는 AOP가 더 적합합니다. 따라서 확장 가능성과 유지 보수성을 고려할 때, 각각의 장점을 활용하는 방향으로 접근하는 것이 좋습니다.

### 결론 및 권장 사항
- 인터셉터:

HTTP 요청/응답과 관련된 로직이 필요할 때 (예: 인증, 권한 부여, 로깅, 파라미터 조작 등).
URL 패턴에 따라 다르게 동작해야 할 때.
특정 경로에 대한 공통 처리 로직이 필요한 경우.
- AOP:

메서드 호출 전후의 로직이 필요할 때 (예: 트랜잭션 관리, 메서드 실행 시간 측정, 로깅 등).
서비스 계층에서 공통된 로직을 분리하고 재사용하고자 할 때.
이 상황에서는 요청의 URL 패턴에 따라 특정 처리가 필요하고, HTTP 요청 및 응답을 다루는 것이므로 인터셉터가 더 적합합니다. 인터셉터를 사용하면 요청을 가로채어 파라미터 복호화와 JWT 토큰 검증을 수행한 후, 필요에 따라 다른 경로로 리다이렉트할 수도 있기 때문입니다.
