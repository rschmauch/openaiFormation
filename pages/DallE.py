from openai import OpenAI
try:
    OPENAI_API_KEY
except:
    from env import OPENAI_API_KEY
import streamlit as st

client = OpenAI(api_key=OPENAI_API_KEY)

generation, alteration = st.tabs(["Génération d'image","Altération d'image"])

with generation:
    value = st.chat_input("Requete")

    with st.chat_message("user"):
        if (value):
            txt = st.text("Waiting for API")

            image = client.images.generate(
                prompt=value,
                model="dall-e-2",
                n=1,
                size="512x512")

            txt.image(image.data[0].url)

with alteration:
    value = st.file_uploader("Image")

    with st.chat_message("user"):
        if (value):
            txt = st.text("Waiting for API")

            image = client.images.create_variation(
                image=value,
                model="dall-e-2",
                n=1,
                size="512x512")

            txt.image(image.data[0].url)