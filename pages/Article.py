from openai import OpenAI
if (not(OPENAI_API_KEY)):
    from env import OPENAI_API_KEY
import streamlit as st

client = OpenAI(api_key=OPENAI_API_KEY)

value = st.chat_input("Thème de l'article")

with st.chat_message("user"):
    if (value):
        txt = st.text("Waiting for API")

        valuetxt = "Create an article about the topic: '"+value+"'. The article must be 200 words long at most."
        #valueimg = "Create an illustration for an article about the topic: '"+value+"'."

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role":"user","content":valuetxt}]
        )

        txt.text(completion.choices[0].message.content)

        valueimg = "illustrate this article:"+completion.choices[0].message.content

        image = client.images.generate(
                prompt=value,
                model="dall-e-2",
                n=2,
                size="512x512")

        st.image(image.data[0].url)
        st.image(image.data[1].url)