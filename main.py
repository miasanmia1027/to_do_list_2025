import streamlit as st
import sqlite3
from functions import add_list_DB

connect = sqlite3.connect('D:/DataBase/to_do_list_2025.db')
cursor = connect.cursor()

cursor.execute("SELECT COUNT(*) FROM to_do_list;")
DB_count = cursor.fetchone()[0] 


st.title("AHN_Page")


prompt = st.chat_input("어떤 것을 해야 하는지 쓰세요")
if prompt:
    st.write(f"너가 추가한 내용: {prompt}")
    choose_date=st.date_input(label="날짜를 선택하시오")
    # 지금까지 일단 사용자 입력을 받았다.
    add_list_DB(prompt,choose_date,DB_count+1)


