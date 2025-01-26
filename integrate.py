import streamlit as st

pg = st.navigation([
    st.Page("program/ADD_LIST_DB.py", title="ADD_LIST_DB", icon="🔥"),
    st.Page("program/ADD_GROUP_DB.py", title="ADD_GROUP_DB", icon="🔥"),
    st.Page("program/MOVE_END_DB.py", title="MOVE_END_DB", icon="✅"),
    st.Page("program/MOVE_LIST_DB.py", title="MOVE_LIST_DB", icon="✅"),
    st.Page("program/DELETE_DB.py", title="DELETE_DB", icon="🗑"),
    st.Page("program/find_group.py", title="find_group", icon="📈"),
])
pg.run()

# ✅.🔥.📦.📈.🗑.

#find_group