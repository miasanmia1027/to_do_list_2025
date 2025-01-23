import streamlit as st
import sqlite3
from functions import Finish_LIST,check_our_db

st.title("MOVE_LIST_DB")
connect = sqlite3.connect('to_do_list_2025.db')
cursor = connect.cursor()

#finish 가 1인것만 출력을 하게 한다.
cursor.execute("SELECT * FROM to_do_list WHERE finish=1;")
DB_LIST = cursor.fetchall()
for i in range(len(DB_LIST)):
    st.write(i+1,DB_LIST[i])

prompt = st.chat_input("몇번을 복구하고 싶은지 알려주세요")
if prompt:
    cursor.execute(f"UPDATE to_do_list SET finish = 0 WHERE numbering = {prompt};")
    connect.commit() 