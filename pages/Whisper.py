from openai import OpenAI
try:
    OPENAI_API_KEY
except:
    from env import OPENAI_API_KEY
import streamlit as st
from pathlib import Path
import os

client = OpenAI(api_key=OPENAI_API_KEY)

audio = st.audio_input("Requete")

dir = Path(__file__).parent.parent / "files"

try:
    os.mkdir(dir)
except:
     if not os.path.isdir(dir):
          print("Erreur de système")
          

if (audio):
    file_path = Path(__file__).parent.parent / "files/input.mp3"

    with open(file_path, "wb") as file:
        file.write(audio.getbuffer())

    txt = st.text("Waiting for API")

    with open(file_path, "rb") as file:
            audiotranscript = client.audio.transcriptions.create(
            model="whisper-1",
            file=file
            )

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":audiotranscript.text+". Fait moi une réponse en quatres phrases"}]
    )

    answer = completion.choices[0].message.content

    response = client.audio.speech.create(
        model="tts-1",
        voice="onyx",
        input=answer
    )

    file_path = Path(__file__).parent.parent / "files/output.mp3"

    response.stream_to_file(file_path)

    st.audio(file_path, autoplay=True)

