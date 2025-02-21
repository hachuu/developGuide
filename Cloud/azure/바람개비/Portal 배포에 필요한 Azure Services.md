# Azure Service Portal 배포 시 명령어
## 1. Storage Account 생성 (이름은 고유해야 함)
```
az storage account create --name hachustorage --location eastasia \
    --resource-group hachu-static-web-app --sku Standard_LRS
```
## 2. Azure Function App 생성 (소비 요금제 사용, Node.js 18 버전)
```
az functionapp create --resource-group hachu-static-web-app \
    --consumption-plan-location eastasia \
    --runtime node --runtime-version 18 \
    --name HachuFunctionApp --storage-account hachustorage
```

## ✅3. Azure Function App 생성 (기존 storage account, resource group 사용)
```
az functionapp create --resource-group hachu-static-web-app \
    --consumption-plan-location eastasia \
    --runtime node --runtime-version 18 \
    --name HachuFunctionApp --storage-account hachustaticwebapp83ce
```
---

# 🔹 Azure Functions에서 Storage Account가 필요한 이유
- Azure Functions는 서버리스 컴퓨팅을 제공하는 플랫폼으로, 함수의 실행을 관리하기 위해 Storage Account가 반드시 필요

## 1️⃣ 트리거 및 상태 저장 (Triggers & State Storage)
- Timer, Event Grid, Queue Storage 등의 트리거 사용 시 필요
- 예를 들어, Timer Trigger의 실행 일정이나 Event Grid Trigger의 이벤트 로그를 저장하는 역할
- Azure Queue Storage를 사용하는 경우, 대기 중인 메시지를 저장
## 2️⃣ Function App의 실행 상태 관리
- Azure Functions는 기본적으로 Azure Files를 사용하여 실행 환경을 유지
- Storage Account는 함수 실행 중 상태 데이터를 저장하며, 여러 인스턴스 간 공유 가능
## 3️⃣ 배포 및 스케일링 관리
- Azure Functions의 코드 및 설정 파일을 저장
- 특히 Consumption Plan(소비 요금제) 사용 시, 동적으로 확장될 때 여러 인스턴스가 동일한 코드를 참조해야 함
- Storage Account가 없으면 동적 스케일링이 불가능
## 4️⃣ 로그 및 모니터링 (Logs & Monitoring)
- Azure Application Insights, Kudu logs 등을 활용해 함수의 로그 데이터를 저장하고 분석 가능
- func start 등 로컬에서 실행할 때도 일부 로그 데이터를 저장하는 역할
- 📌 결론: Storage Account는 Azure Functions 실행에 필수적인 저장 공간

- Azure Functions의 실행 및 상태 관리, 로그 저장 등을 위해 Storage Account가 필수적으로 사용됩니다.
- 특히 Consumption Plan(소비 요금제)에서 자동 확장을 위해 반드시 필요합니다.

## 결론 
- 💡 Storage Account가 없으면 Function App을 생성할 수 없으며, 트리거 및 실행 상태도 유지할 수 없습니다. 🚀


# 🔹 Azure에서 Resource Group(리소스 그룹)이 필요한 이유
- Azure에서 **Resource Group(리소스 그룹)** 은 Azure 리소스를 논리적으로 그룹화하는 컨테이너 역할을 합니다.
- 즉, 관련된 리소스를 하나의 그룹으로 묶어서 효율적으로 관리할 수 있도록 도와줍니다.

## 1️⃣ 리소스 관리의 용이성
- 같은 프로젝트나 애플리케이션의 리소스를 한 곳에서 관리 가능
- 예를 들어, Function App, Storage Account, Event Grid, Cosmos DB 등이 하나의 리소스 그룹에 속할 수 있음
## 2️⃣ 배포 및 삭제가 간편
- 리소스 그룹에 속한 모든 리소스를 한 번에 배포하거나 삭제 가능
- 예를 들어, 개발 환경에서 테스트 후 리소스 그룹을 삭제하면, 내부의 모든 리소스도 함께 삭제됨
- 실수로 불필요한 리소스를 남겨두어 비용이 발생하는 것을 방지
## 3️⃣ 액세스 및 권한 관리 (IAM)
- 리소스 그룹 단위로 사용자 및 서비스의 권한(Role-Based Access Control, RBAC) 설정 가능
- 예를 들어, 특정 팀원에게 이 리소스 그룹 안의 리소스만 수정 가능하도록 제한 가능
## 4️⃣ 청구(Billing) 및 비용 관리
- 같은 리소스 그룹 내에서 사용된 모든 리소스의 비용을 한 번에 확인 가능
- 팀별, 프로젝트별로 리소스 그룹을 분리하여 비용을 추적하고 최적화 가능
## 5️⃣ 리전(Region) 관리
- 리소스 그룹 자체는 특정 리전에 종속되지 않지만, 그 안의 리소스는 특정 리전에 배포 가능
- 동일한 리전에서 배포된 리소스를 하나의 그룹으로 관리 가능하여 성능 및 네트워크 비용 최적화
## 📌 결론
- Resource Group은 Azure 리소스를 효율적으로 관리하는 핵심 단위
```
✅ 리소스를 논리적으로 그룹화하여 관리 및 삭제가 쉬움
✅ 권한(RBAC) 설정을 통해 보안 강화 가능
✅ 비용 추적 및 최적화 가능
✅ 배포 및 유지보수 편리
```
- 💡 Azure에서는 모든 리소스가 반드시 하나의 Resource Group에 속해야 하며, 이를 활용하면 인프라 관리를 훨씬 효율적으로 할 수 있습니다. 🚀
