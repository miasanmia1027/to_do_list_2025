# to_do_list_2025
# 데이터구축 방식
- SQLite
SQL은 Structured Query Language의 약자로, 데이터베이스를 조작하고 관리하는 데 사용되는 표준화된 언어입니다. 
데이터베이스는 구조화된 데이터를 저장하고 관리하는 시스템으로, 기업이나 조직에서 중요한 정보를 보관하고 활용하는 데 사용됩니다.
- 공식 문서
https://sqlite-database.readthedocs.io/en/latest/

https://wikidocs.net/book/1530



https://www.w3schools.com/sql/

# 프론트 모듈
- Flask + Jinja2
- flask 공식문서
https://flask.palletsprojects.com/en/stable/
###  포기
- streamlit 시작
- 공식문서
https://docs.streamlit.io/
- DB 연결
https://docs.streamlit.io/get-started/fundamentals/advanced-concepts



# 서버에 올리는 법
- Streamlit Community Cloud
- https://todolist2025-olms5my9e7g248qzbufxan.streamlit.app/




# 코드 설명 
- ADD_DB == 사용자가 자기가 해야 하는 작업을 올리는 페이지
- MOVE_END_DB == 사용자가 추가한 목록을 finish를 1로 바꾸는 작업
- MOVE_LIST_DB == 사용자가 잘못 옮긴 코드를 다시 불러오는 작업
- DELETE_DB == 잘못 추가한 열을 삭제하는 코드


### 내가 해야 하는거 
1. 이제 해야하는거는 delte를 사용하면 프로그램이 먹통이 되는거 -> delete를 할때 음수로 바꾸는 거 생각하기 -> 이거 오늘 해야지
2. ADD_GROUP_DB할때 numbring만 쓰지말고 group도 쓰고
3. end 시킬때 날짜를 넣는거 넣기
4. st.session_state를 다른 코드에도 넣기
5. 구룹별로 보이기 하는걸로 바꾸기  -> 구룹을 선택하라고 하면서 하게 하는건가?


