from openai import OpenAI
import streamlit as st

client = OpenAI()

value = st.text_input("Requete")

if (value):
    txt = st.text("Waiting for API")

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":value}]
    )

    txt.text(completion.choices[0].message.content)