import streamlit as st
import sqlite3
from functions import Finish_LIST,check_our_db

st.title("Finish_LIST")
connect = sqlite3.connect('D:/DataBase/to_do_list_2025.db')
cursor = connect.cursor()

cursor.execute("SELECT * FROM to_do_list;")
DB_LIST = cursor.fetchall()
for i in range(len(DB_LIST)):
    st.write(i+1,DB_LIST[i])

prompt = st.chat_input("몇번을 삭제하고 싶은지 알려주세요")
if prompt:
    cursor.execute(f"UPDATE to_do_list SET finish = 1 WHERE numbering = {prompt};")
    connect.commit() 

# 이제는 "1" 인것만 혹은  "0"인 것만 이렇게 출력을 하는 프로그램을 만들어 보자

