import streamlit as st
import sqlite3
from program.functions import add_group_DB

st.title("ADD_GROUP_DB")


# 데이터베이스 연결
connect = sqlite3.connect('group_table.db')
cursor = connect.cursor()

# 현재 저장된 그룹 가져오기
st.write("현재 저장된 그룹:")
cursor.execute("SELECT groupvalue FROM group_table;")
groups = cursor.fetchall()  # 그룹 데이터를 가져옴

if groups:
    for i, group in enumerate(groups, start=1):
        st.write(f"{i}. {group[0]}")  # 그룹 이름 출력
else:
    st.write("저장된 그룹이 없습니다.")



prompt = st.chat_input("group를 생성하세요")
if prompt:
    st.write(f"너가 추가한 구룹: {prompt}")
    # 지금까지 일단 사용자 입력을 받았다.
    add_group_DB(prompt)