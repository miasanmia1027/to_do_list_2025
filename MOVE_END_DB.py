import streamlit as st
import sqlite3
from functions import Finish_LIST,check_our_db

st.title("MOVE_END_DB")
connect = sqlite3.connect('D:/DataBase/to_do_list_2025.db')
cursor = connect.cursor()

#finish 가 0인것만 출력을 하게 한다.
cursor.execute("SELECT * FROM to_do_list WHERE finish=0;")
DB_LIST = cursor.fetchall()
for i in range(len(DB_LIST)):
    st.write(i+1,DB_LIST[i])

prompt = st.chat_input("몇번을 끝냈는지 알려주세요")
if prompt:
    cursor.execute(f"UPDATE to_do_list SET finish = 1 WHERE numbering = {prompt};")
    connect.commit() 

