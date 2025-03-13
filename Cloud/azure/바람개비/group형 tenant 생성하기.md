# 여러 개발자들이 하나의 구독에서 Function App을 개발하고 배포하는 방법

## 1. Azure Tenant 생성
- Azure AD Tenant(조직)를 새로 생성하려면:
- **Microsoft Entra 관리 센터**에 접속
- "Tenant 만들기" → "Azure AD" 선택
- 조직 정보를 입력하고 테넌트 생성
## 2. Azure 구독 및 결제 설정
- 테넌트만으로는 리소스를 만들 수 없으므로 **Azure 구독(Subscription)**을 추가해야 함
- Azure Portal 접속 → **"구독"**으로 이동
- "새 구독 추가"
- 결제 계정 1개로 관리하려면 Microsoft 고객 계약(MCA) 또는 Enterprise Agreement(EA) 추천
- 개인용이면 Pay-As-You-Go(종량제) 선택
- 결제 수단(신용카드 또는 청구 계정) 등록
## 3. 개발자 계정 및 권한 설정
- 개발자가 Function App을 관리할 수 있도록 권한을 부여해야 함
- Azure AD에서 사용자 추가
- Microsoft Entra ID → "사용자" → "새 사용자"
- 이메일로 개발자 7명 추가
- RBAC(Role-Based Access Control) 설정
- 구독 또는 리소스 그룹에서
- 개발자들에게 "기여자(Contributor)" 역할 부여
- 필요 시 Function App에 대해 "Function App 기여자" 역할만 부여
## 4. 리소스 그룹 및 Function App 생성
- 각 개발자가 작업할 수 있도록 공통 리소스 그룹을 만들거나 개별 리소스 그룹을 할당-
- 리소스 그룹 생성
- RG-FunctionApps 같은 그룹을 생성
- Function App 배포
- Azure Functions → "새로 만들기"
- 런타임 선택(.NET, Python, Node.js 등)
- 호스팅 계획(Consumption Plan 추천)
## 5. 개발 및 배포 환경 구성
- 개발자들이 원활하게 작업할 수 있도록 Azure DevOps 또는 GitHub Actions를 연동
- Azure DevOps: CI/CD Pipeline 구축
- GitHub Actions: azure/functions-action으로 배포 자동화
- Application Insights: Function App 모니터링

# 결론
- ✅ Azure Tenant 생성
- ✅ 결제 계정 하나로 구독 추가
- ✅ 개발자 계정 추가 및 권한 설정
- ✅ Function App 개발 환경 구성
