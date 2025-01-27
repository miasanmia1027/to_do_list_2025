import streamlit as st
import sqlite3
from program.functions import Finish_LIST,check_our_db

st.title("MOVE_END_DB")
connect = sqlite3.connect('to_do_list_2025.db')
cursor = connect.cursor()

#finish 가 0인것만 출력을 하게 한다.
cursor.execute("SELECT * FROM to_do_list WHERE finish=0;")
DB_LIST = cursor.fetchall()
for i in range(len(DB_LIST)):
    st.write(i+1,DB_LIST[i])

# 날짜 선택
choose_date = st.date_input("작업 완료 날짜를 선택하세요")

# 작업 번호 입력
prompt = st.chat_input("몇 번 작업을 완료했는지 입력하세요")

if prompt:
    cursor.execute(f"""
        UPDATE to_do_list 
        SET finish = 1, date_end = ? 
        WHERE rowid = ?;
        """, (choose_date, prompt))
    connect.commit()
    st.success(f"작업 {prompt}이 완료 처리되었습니다!")
   



