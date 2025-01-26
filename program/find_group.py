import streamlit as st
import sqlite3
from program.functions import group_list

st.title("Find Group")
connect = sqlite3.connect('to_do_list_2025.db')
cursor = connect.cursor()

# 그룹 상태 관리
if "group" not in st.session_state:
    st.session_state.group = []

# 그룹 선택
st.session_state.group = st.multiselect(
    "현재 저장된 그룹에서 선택하세요:",
    group_list(),
    default=st.session_state.group  
)
st.write(f"선택된 그룹: {st.session_state.group}")

# 선택된 그룹 데이터를 문자열로 변환
if st.session_state.group:
    group_query = ",".join(st.session_state.group)  # 리스트를 쉼표로 구분된 문자열로 변환
    cursor.execute(f"SELECT * FROM to_do_list WHERE grouplist LIKE '%{group_query}%';")
    DB_group = cursor.fetchall()
    
    if DB_group:
        for i, row in enumerate(DB_group, start=1):
            st.write(f"{i}. {row}")
    else:
        st.write("선택한 그룹과 일치하는 데이터가 없습니다.")
else:
    st.write("그룹을 선택해주세요.")

st.session_state.group = []
