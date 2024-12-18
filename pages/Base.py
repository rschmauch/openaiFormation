from openai import OpenAI
import streamlit as st

try:
    OPENAI_API_KEY
except:
    from env import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

value = st.chat_input("Requete")

with st.chat_message("user"):
    if (value):
        txt = st.text("Waiting for API")

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role":"user","content":value}]
        )

        txt.text(completion.choices[0].message.content)