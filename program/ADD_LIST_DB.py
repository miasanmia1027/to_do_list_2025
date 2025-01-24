import streamlit as st
import sqlite3
from program.functions import add_list_DB,group_list


st.title("ADD_LIST_DB")

connect = sqlite3.connect('to_do_list_2025.db')
cursor = connect.cursor()

cursor.execute("SELECT COUNT(*) FROM to_do_list;")
DB_count = cursor.fetchone()[0] 
# key 중복을 피하기 위해서 기존에 몇개의 열을 가지고 있는지 확인 하는 코드

# Prompt 입력값 상태 관리
if "prompt" not in st.session_state:
    st.session_state.prompt = ""

# 날짜 상태 관리
if "choose_date" not in st.session_state:
    st.session_state.choose_date = None

# 그룹 상태 관리
if "group" not in st.session_state:
    st.session_state.group = []

# 사용자 입력
prompt = st.chat_input("어떤 것을 해야 하는지 쓰세요")
if prompt:
    st.session_state.prompt = prompt  # 상태에 저장
    st.write(f"너가 추가한 내용: {prompt}")

# 날짜 선택
st.session_state.choose_date = st.date_input(
    label="날짜를 선택하시오",
    value=st.session_state.choose_date,  # 이전 상태 유지
)

# 그룹 선택
st.session_state.group = st.multiselect(
    "현재 저장된 그룹에서 선택하세요:",
    group_list(),
    default=st.session_state.group  # 이전 선택 유지
)

# 추가 버튼
if st.button("추가하기"):
    if st.session_state.prompt and st.session_state.choose_date:
        add_list_DB(
            st.session_state.prompt,
            st.session_state.choose_date,
            DB_count + 1,
            st.session_state.group
        )
        st.success("작업이 성공적으로 추가되었습니다!")
        # 상태 초기화
        st.session_state.prompt = ""
        st.session_state.choose_date = None
        st.session_state.group = []
    else:
        st.error("모든 항목을 입력해야 합니다!")
    



