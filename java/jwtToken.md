### jwt token spring java


- jwt token 생성
```
public static String generateToken() {
    // 토큰 유효 시간을 10분으로 설정
    long nowMillis = System.currentTimeMillis();
    long expMillis = nowMillis + 600000; // 10분 후 (10 * 60 * 1000)
    Date exp = new Date(expMillis);

    return Jwts.builder()
            .setHeaderParam("typ", "JWT")
            .claim("userId", UUID.randomUUID().toString())
            .claim("data", "")
            .claim("scope", "")
            .setExpiration(exp)
            .signWith(SECRET_KEY)
            .compact();
}
```

- interceptor에서 token 유효성 검사
```
// JWT 토큰 검사
String token = request.getHeader("Authorization");

if (token == null || token.isEmpty()) {
    response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "Invalid JWT token");
    return false;
}

// 토큰 재발급
try {
    if(!validateJwtToken(token)) {
        // Extract devServiceId
        String devServiceId = request.getParameter("devServiceId");

        // Extract userKey
        String userKey = request.getParameter("userKey");
        try {
            String newToken = SecurityUtil.generateToken(devServiceId, userKey);
            response.setHeader("Authorization", "Bearer " + newToken);
        } catch (Exception e) {
            response.sendError(HttpServletResponse.SC_INTERNAL_SERVER_ERROR, "Error generating new JWT token");
            return false;
        }
    }
} catch (Exception e) {
    response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "Invalid JWT token");
    return false;
}

// 원래 경로로 리다이렉트
String newUri = uri.replace("/bypass", "");
request.getRequestDispatcher(newUri).forward(request, response);
return false; // 여기서 false를 반환하여 현재 핸들러로의 처리를 중단

private boolean validateJwtToken(String token) throws Exception {
    try {
        String bearerToken = null;
        if (token != null && token.startsWith("Bearer ")) {
            bearerToken = token.substring(7); // "Bearer " 접두사 제거
        }
        return SecurityUtil.isValidateToken(bearerToken);
    } catch (Exception e) {
        System.out.println("에러 : " + e);
        throw new Exception("Invalid JWT Token", e);
    }
}

```
- 유효한 jwt token인지 확인
  1. 유효케이스
  2. 만료된 케이스
  3. jwt signature 불일치
  4. jwt token 유효하지 않음
  5. jwt string empty
```

@Component
public class SecurityUtil implements EnvironmentAware {
	public static boolean isValidateToken(String token) throws Exception {
			try {
	
				Jwts.parser()
						.setSigningKey(jwtSecurityLiveKey.getBytes())
						.parseClaimsJws(token)
						.getBody();
				return true;
			} catch (ExpiredJwtException e) {
				return false;
			} catch (SignatureException e) {
				throw new Exception("Invalid JWT signature", e);
			} catch (MalformedJwtException e) {
				throw new Exception("Invalid JWT Token", e);
			} catch (IllegalArgumentException e) {
				throw new Exception("JWT claims string is empty.", e);
			}
		}
	}
}
```
