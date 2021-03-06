# 0228 개발 일지
- 회원가입 API 구현
    - 회원가입시 토큰 자동생성
- 로그인 API 구현
    - username(이메일), password 항목을 받도록 설정
- super 계정 생성
    - admin 페이지에서 회원을 생성하면 비밀번호가 암호화가 되지 않는 문제가 있음

# 0301 개발 일지
- 유저 프로필 API 구현
    - Link와 Project 모델 추가하고 외래키로 연결
    - 토큰을 통해 인증 이후 프로필 수정 가능
    - tech(tech_stack) 저장할 땐 '|'로 기술 구분을 하여 문자열로 저장하고, 불러올 땐 '|'를 기준으로 나눠서 배열로 반환
    - signal을 통해서 User 생성 이후, Link와 Project 객체 생성과 Profile 생성을 유도

# 0305 개발 일지
- 유저 프로필 모델에 my_tags 추가
    - 이전과는 다르게 MultiSelectField를 사용하지 않고 문자열로 저장하고 tech처럼 '|'로 구분한다.
- QnA 생성, 목록, 디테일 API 구현
    - 생성 API
        - token으로 사용자 인증을 받고, profile을 찾아 writer에 저장한다.
        - title, content, ref_tags 정보를 받아서 저장한다. 
        - written_time은 갱신되는 시간으로 지정해뒀다.
    - 목록 API
        - 생성된 QnA 포스트 목록들을 불러온다.
        - like_num와 liked 여부를 serializer 선에서 처리를 한다.
        - writer 정보를 상세하게 표시해뒀다.
    - 디테일 API
        - 어떤 qna인지 정보를 받기 때문에 해당 API에 조회, 수정, 삭제 기능을 구현해뒀다. 
        - 수정, 삭제에는 작성자 인증이 안될 경우 에러를 발생하도록 해두었다.
- 좋아요 기능 구현
