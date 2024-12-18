import streamlit as st

path = "root/pages/"
pg = st.navigation([
        st.Page(path + "Base.py", title="Bases"),
        st.Page(path + "DallE.py", title="Dall-E"),
        st.Page(path + "Article.py", title="Article"),
        st.Page(path + "Whisper.py", title="Whisper"),
    ]) 
pg.run()