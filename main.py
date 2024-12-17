import streamlit as st

path = "root/pages/"
pg = st.navigation([
        st.Page(path + "Base.py", title="Bases"),
        st.Page(path + "DallE.py", title="Dall-E"),
    ]) 
pg.run()