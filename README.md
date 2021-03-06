# Welcome to DEVRY

// 이미지 위치 
## 🏠 [Homepage]()

<br>

## 🚤팀원소개

**Dae Hyun Park**

- 🥪Github: [@daep93](https://github.com/daep93)

**Yoon Vin Kim**

- 🥨Github: [@vreez](https://github.com/vreez)

**Dae Yeong Jeong**

- 🥠Github: [@kingdom](https://github.com/kingdom)

**Hyeon Jun Nam**

- 🧀Github: [@applevalley](https://github.com/applevalley) 

**Si Eun Jeong**

- 🍤Github: [@sieun-iris](https://github.com/sieun-iris)



## 📆 프로젝트 개요

- **진행 기간**: 
	- sub-proj1: 2021.01.11 ~ 2020.01.15
	- sub-proj2: 2021.01.18 ~ 2022.01.22
	- sub-proj3: 2022.01.25 ~2020.02.19

- **목표**
  - 개발자 통합 커뮤니티 
  
## 📒 Tech Log
- Node.js 14.15.3
## 🔧 Tech Stack


## ⚙️ Install and Usage

### Frontend

#### frontend 실행 방법

- step0. frontend 폴더 클릭

- step1. 패키지 설치

```
$ npm i
```

- step2. 프로젝트 실행

```
$ npm run serve
```

### Backend

#### backend 실행 방법

- step0. backend 폴더 클릭
- step1. 가상환경 구동

```bash
$ python -m venv venv       # 첫 venv 뒤의 venv에서는 가상환경 이름을 자유롭게 정의 가능합니다.
```

```bash
# 만들어진 가상환경을 활성화하는 과정입니다. 
$ source venv/Scripts/activate  # windows

$ source venv/bin/activate     # Mac / Linux
```

```bash
$ source venv/Scripts/activate     # 가상환경이 정상적으로 활성화되었습니다.
(venv) 
```

```bash
$ deactivate                # 가상환경 비활성화
```

- step2. pip 업그레이드
  - 현재 가상 환경을 새로 생성한 경우 pip의 버전이 낮아 라이브러리 설치 시 cryptography 라이브러리와 충돌하는 문제가 있습니다. 이를 해결하기 위해 다른 라이브러리들을 설치해주기 전 pip의 업그레이드를 먼저 진행합니다.

```bash
$ python -m pip install --upgrade pip
```

```bash
# 라이브러리들을 requirements.txt에 기록된 라이브러리와 버전을 기준으로 설치합니다.
$ pip install -r requirements.txt     
```

- step3. 마이그레이션 진행

```bash
$ python manage.py makemigrations
```

```bash
$ python manage.py migrate
```

- step4. 서버 구동

```bash
$ python manage.py runserver
```



#### Node Version Manager

- 맥: [NVM](https://github.com/joshua1988/vue-til-server#nvm-%EC%84%A4%EC%B9%98-%EB%B0%8F-%EB%B2%84%EC%A0%84-%EB%B3%80%EA%B2%BD-%EB%B0%A9%EB%B2%95)
- 윈도우: [NVM-window](http://hong.adfeel.info/backend/nodejs/window%EC%97%90%EC%84%9C-nvmnode-version-manager-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0/)
#### vscode 플러그인
- Eslint
- Vetur
- Vue VSCode Snippets
- vue
- Vue 3 Snippets
- Vue Inline Templage
- Vue Peek
- Prettier를 혹시 설치했다면 해제할 것

### Backend

#### vscode 플러그인

- Python
- Django



## 👀 서비스 소개
![devry](img/README/sub2/devry.JPG)

**DEVRY란?**

DEVRY는 **개발자 특화 커뮤니티** 서비스와 **포트폴리오** 서비스를 결합한 개발자 SNS 플랫폼입니다.

`Developer` + `Everyone` 의 합성어로, 모든 개발자를 위한 공간이라는 뜻을 함축하고 있습니다.

</br>

**자세한 기획 배경 및 기능 소개가 궁금하다면?**

[DEVRY 기획/기능 명세서 바로가기](https://www.notion.so/DEVRY-9f3cc7c325694d2287e476160df50fc2)

[API 요청 문서 확인하기](https://www.notion.so/API-763e6ef61f074ccd935f48a199e561a4)

[API 문서 확인하기](https://www.notion.so/Devry-API-Document-057c077d706c4dfb8db173658c39d185)

</br>



## ⭐️ 주요 기능

### 1. 커뮤니티 기능

- DEVRY는 다섯 가지의 카테고리를 중심으로 커뮤니티가 구성되어 있으며, `#해시태그` 기반으로 강력한 세부 검색 기능을 제공합니다.
- 또한 SNS와 같이, 다른 사용자를 구독하는 기능을 제공합니다.



**① Forum**

> 기술 스택을 주제로 글을 작성하고, 공유하는 공간

- 태그 필터링 기능을 통해 원하는 기술 스택의 글만 선택해서 확인 가능
  - 왼쪽 카테고리 구역의 My tags에서 내가 팔로우하는 태그 고정, 페이지 이동 시 자동 필터링
- 작성자의 프로필 및 대표 글을 미리보기 형태로 제공, 관심 있을 경우 바로 팔로우 할 수 있도록 함
- 블로그에서 작성하는 것과 같이 편집 기능 제공

![forum](img/README/sub3/포럼게시판.PNG)
---
![forum_detail](img/README/sub3/포럼게시물.PNG)

</br>

**② QnA**

> 질의응답을 할 수 있는 공간

- 태그 필터링 기능을 통해 원하는 기술 스택의 글만 선택해서 확인 가능
  - 왼쪽 카테고리 구역의 My tags에서 내가 팔로우하는 태그 고정, 페이지 이동 시 자동 필터링
- 답변 완료, 답변 대기 상태를 색깔로 구분 가능
- 질문자와 채택된 답변자의 프로필 및 대표 글을 미리보기 형태로 제공

![qna](img/README/sub3/qna게시판.PNG)
---
![qna](img/README/sub3/qna게시물.PNG)

</br>

**③ Event**

>  컨퍼런스 등 각종 이벤트 정보를 확인할 수 있는 공간

- 단체 또는 개인이 주최하는 모임 등록 가능
- 태그 필터링 기능을 통해 원하는 기술 스택의 이벤트만 선택해서 확인 가능
  - 왼쪽 카테고리 구역의 My tags에서 내가 팔로우하는 태그 고정, 페이지 이동 시 자동 필터링

![event](img/README/sub3/이벤트게시판.PNG)
---
![event](img/README/sub3/이벤트게시물.PNG)


</br>

### 2. 포트폴리오 기능

① 프로필 페이지

> 사용자의 프로필 정보를 보여주는 공간

**주요 내용**

- 유저가 설정한 개인정보
- 글에서 참조한 태그 통계
- 관심있는 기술 태그
- 맘에 드는 글 상단에 고정 (pinned 기능)
- 내가 쓴 글 또는 댓글을 시간 순으로 확인 가능

자신의 개발 이력 및 커뮤니티 활동 내역 요약을 통해, 마치 작은 블로그를 제공하는 것처럼 또 하나의 포트폴리오를 제공

![profile](img/README/sub3/프로필1.PNG)
---
![profile](img/README/sub3/프로필2.PNG)
---

---




</br>

①-1. 프로필 설정 페이지

>  프로필 페이지에 들어갈 정보를 추가 및 수정할 수 있는 공간

- 개발자에게 특화된 이력 입력폼 제공

![profile](img/README/sub3/프로필설정1.PNG)
---
![profile](img/README/sub3/프로필설정2.PNG)

</br>

①-2. 팔로우/팔로잉 모달

>  사용자의 팔로워/팔로잉 목록을 모달 형태로 열어서 확인할 수 있도록 구현

- 해당 화면에서 바로 팔로우 및 팔로우 취소 가능

![modal1](img/README/sub3/팔로우1.PNG)
---
![modal1](img/README/sub3/팔로우2.PNG)


</br>

</br>

### 3. 편집 기능 


- Forum, QnA 게시판 글 작성 시, 마크다운 에디터 지원
- Ctrl + S 입력을 통해 md 파일 미리보기 지원
- 사진 업로드 가능
- Liquid 태그를 통해 아래의 항목 임베드 가능
  - Youtube
  - CodeSandBox
  - Repl.it
  - Instagram


![liquid](img/README/Liquid_태그_가이드.PNG)
---
![liquid1](img/README/Liquid_1.PNG)
---
![liquid2](img/README/Liquid_2.PNG)






















