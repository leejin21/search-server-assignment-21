# Search-Server-Assignment-21

## What is this project for

서버 개발자 채용과정의 코딩 과제입니다.
도커를 사용해 개발했습니다.

### 기능들

1. 새로운 회사 추가하기 - /companies/ POST
2. 회사 이름으로 회사 검색하기 - /companies/ GET
3. 자동완성 - /companies/candidates/ GET

## How this project works

### docker 명령어

```bash
# 이미지 빌드 및 컨테이너 실행
docker-compose -f docker-compose.dev.yml up -d --build

# docker 관련 파일 변경 없이(이미지 상태 그대로) 컨테이너 실행
docker-compose -f docker-compose.dev.yml up -d

# 컨테이너 중지 및 삭제(이때 volume은 삭제되지 않음에 유의)
docker-compose -f docker-compose.dev.yml down

```

-   flask는 debug mode == ON 으로 설정함
-   따라서, 이미지 변경 없이 서버만 코드 변경했을 때는 컨테이너 런 다시 안해도 됨.

### 접속 주소

-   서버: http://localhost:5000/
-   pgadmin: http://localhost:8088/browser/

## 기능 구동 모습

### 기능 1. 새로운 회사 추가하기

#### /companies/ POST 200 SUCCESS

![companies post 200 구동](./imgs/comp_post_200.gif)

#### /companies/ POST 400 ERROR

![companies post 400 구동](./imgs/comp_post_400.gif)

### 기능 2. 회사 이름으로 회사 검색하기

#### /companies/ GET

![companies get all 구동](./imgs/comp_get_all.gif)

### 기능 3. 자동완성

#### /companies/candidates/ GET

![candidates get all 구동](./imgs/cand_get_all.gif)

## How I made this project

### Business Logic

![비즈니스 로직](./imgs/business_logic.png)

### DOCS

#### API 문서

![API문서](./imgs/rest_api_docs.png)

#### DB 문서

![DB문서](./imgs/DB_img.png)

### Architecture

Uncle Bob의 클린 아키텍처 구조를 토대로 우선 구성해 보았습니다.

![architecture](./imgs/architecture.png)

#### 참고: Uncle Bob의 클린 아키텍처 구조

![uncle bob architecture](./imgs/CleanArchitecture.jpg)

## Github Commit Convention

-   feat: 새로운 기능 추가
-   fix: 버그 픽스
-   docs: 문서 수정
-   style: 포맷, 세미콜론 수정, Optimize import, Code clean up 등 코드가 아닌 스타일에 관련된 수정
-   refactor: 코드 리펙토링
-   test: 테스트 코드 추가
-   chore: 빌드 관련 업무 수정(안드로이드의 경우 builde.gradle, manifest)
