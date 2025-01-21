1. AOP 설정
먼저, Spring AOP를 설정하기 위해 필요한 의존성을 pom.xml에 추가합니다.
```
implementation 'org.springframework.boot:spring-boot-starter-aop'
```

2. 암호화 및 복호화 로직
파라미터를 암호화 및 복호화하는 유틸리티 클래스를 작성합니다.

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

3. JWT 토큰 검사 로직
JWT 토큰을 검사하는 유틸리티 클래스를 작성합니다.

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

4. AOP 적용
이제 AOP를 통해 원하는 경로로 들어오는 요청을 가로채고, 파라미터를 암호화/복호화 및 JWT 토큰을 검사한 후 원래의 메서드를 호출하는 로직을 구현합니다.

```java
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;

import javax.servlet.http.HttpServletRequest;
import java.util.Map;

@Aspect
@Component
public class RequestInterceptor {

    @Around("execution(* com.example.SampleController.*(..)) && @annotation(org.springframework.web.bind.annotation.RequestMapping)")
    public Object interceptRequests(ProceedingJoinPoint joinPoint) throws Throwable {
        HttpServletRequest request = null;

        for (Object arg : joinPoint.getArgs()) {
            if (arg instanceof HttpServletRequest) {
                request = (HttpServletRequest) arg;
                break;
            }
        }

        if (request != null) {
            String uri = request.getRequestURI();
            if (uri.startsWith("/api/sample/")) {
                // JWT 토큰 검사
                String token = request.getHeader("Authorization");
                if (token == null || token.isEmpty() || !validateJwtToken(token)) {
                    throw new SecurityException("Invalid JWT token");
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


5. 기존 controller에 interceptor와 다르게 catch할 RequestMapping에 해당하는 function을 기존 로직 function과 동일한 형태로 중복 생성해야 함
```java
@RestController
@RequestMapping("/api/sample")
public class SampleController {

    @RequestMapping(value = "/catch/getSomething", method = RequestMethod.GET)
    public String getSomething(@RequestParam String param) {
        // 여기서 param은 복호화된 상태로 전달됩니다.
        return "Publisher List: " + param;
    }

    @RequestMapping(value = "/getSomething", method = RequestMethod.GET)
    public String getSomethingWithoutCatch(@RequestParam String param) {
        // 이 경로로 직접 요청하는 경우, 별도의 처리 없이 호출됩니다.
        return "Publisher List: " + param;
    }
}
```
