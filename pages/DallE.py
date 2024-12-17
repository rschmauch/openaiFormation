from openai import OpenAI
from env import OPENAI_API_KEY
import streamlit as st

client = OpenAI(api_key=OPENAI_API_KEY)

value = st.chat_input("Requete")

with st.chat_message("user"):
    if (value):
        txt = st.text("Waiting for API")

        image = client.images.generate(
            prompt=value,
            model="dall-e-2",
            n=1,
            size="500x500")

        txt.image(image.data[0].url)