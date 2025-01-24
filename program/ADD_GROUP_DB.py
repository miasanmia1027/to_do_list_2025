import streamlit as st
from program.functions import add_group_DB

st.title("ADD_GROUP_DB")

prompt = st.chat_input("group를 생성하세요")
if prompt:
    st.write(f"너가 추가한 구룹: {prompt}")
    # 지금까지 일단 사용자 입력을 받았다.
    add_group_DB(prompt)