# commit 규칙



## Git

### commit

- ```bash
  [이슈번호] type/기능단위 : 무엇을 어떻게 했는지 작성
  
  body 
  ```

- ```bash
  [S0234165-1] feat/Login : Create login success page
  
  body
  ```
- type
  - 기능(feat): 새로운 기능을 추가
    - Create, Fetch(Read), Update, Delete
  - 디자인(design): 화면단의 배치 변경 또는 css 변경
  - 버그(fix): 버그 수정
  - 리팩토링(refactor): 코드 리팩토링
  - 형식(style): 코드 형식, 정렬, 주석 등의 변경(동작에 영향을 주는 코드 변경 없음)
  - 테스트(test): 테스트 추가, 테스트 리팩토링(제품 코드 수정 없음, 테스트 코드에 관련된 모든 변경에 해당)
  - 문서(docs): 문서 수정(제품 코드 수정 없음)
  - 기타(chore): 빌드 업무 수정, 패키지 매니저 설정 등 위에 해당되지 않는 모든 변경(제품 코드 수정 없음)

- 제목은 50자를 넘지 않고, 대문자로 작성하고 마침표를 붙이지 않는다.
- 과거시제를 사용하지 않고 명령어를 작성한다.
  - Fixed -> Fix
  - Added -> Add


### branch

​		master

​			|

​	  developement

​			|

​	 feature/{field}/{story}

- master : 배포용 브랜치(production)
- developement : 개발용 브랜치
- feature/{field}/{story}: 개인 작업용 브랜치
  - field에 BE인지 FE인지 명시.
  - story에 본인이 맡은 jira Story를 명시(구현할 기능을 모두 포함하는 포괄적인 내용으로 작성).
  - jira Story에 속한 모든 task가 끝나면 development에 MR할 것.
    - MR을 할 경우 MR 성공시 본인이 작업한 브랜치를 삭제하는 항목 체크할 것. 
    - 승인 지정은 각 파트장으로 하고, 파트장은 각 파트의 모든 팀원이 리뷰를 끝내고 충돌, 이슈가 없으면 merge (파트장은 브랜치 삭제 항목이 체크되어있는지 확인)
      - MR을 한 뒤, 각 파트의 구성원들에게 mm을 통해 알릴 것. 구성원들은 알림을 받으면 최대한 빠르게 리뷰를 해줄 것.
      - 충돌이나 이슈가 있으면 파트장이 반려하고 MR 신청자가 이를 고친 뒤 다시 MR을 한다.
    - merge가 되면 각 파트의 구성원들은 본인의 작업 브랜치에 development 브랜치를 merge할 것.


## Jira

- Epic : 기능 단위
- Story
  - Frontend
  - 기능을 CRUD로 작성, 페이지 단위
  - Backend
  - 기능을 CRUD로 작성
- Task
  - Frontend
    - 페이지 안에 세부적으로 들어가야 할 내용들
  - Backend
    - 미정 