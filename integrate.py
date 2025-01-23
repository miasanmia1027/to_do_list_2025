import streamlit as st
pg = st.navigation([
    st.Page("ADD_DB.py", title="ADD_DB", icon="🔥"),
    st.Page("MOVE_END_DB.py", title="MOVE_END_DB", icon="🔥"),
    st.Page("MOVE_LIST_DB.py", title="MOVE_LIST_DB", icon="🔥"),
    st.Page("DELETE_DB.py", title="DELETE_DB", icon="🔥"),
])
pg.run()

