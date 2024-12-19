from openai import OpenAI
from env import OPENAI_API_KEY
import streamlit as st
from pathlib import Path
import os

client = OpenAI(api_key=OPENAI_API_KEY)

dir = Path(__file__).parent / "files"

try:
    os.mkdir(dir)
except:
     if not os.path.isdir(dir):
          print("Erreur de système")

if 'history' not in st.session_state:
    st.session_state.history = ["start"]

if 'history' in st.session_state:
    prompt = st.session_state.history[-1]

txt = st.text("Waiting for API")
image = st.text("loading")
audio = st.text("loading")
opt1 = st.button('1')
opt2 = st.button('2')
opt3 = st.button('3')
opt4 = st.button('retour')
display = [txt,audio,image]

def create_chapter(client : OpenAI,display,prompt,new=True):

    index = len(st.session_state.history)

    if new: 
        data = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role":"user","content":prompt}]
            )

        answer = data.choices[0].message.content
    else :
        answer = st.session_state.history[-1]

    audio = client.audio.speech.create(
        model="tts-1",
        voice="shimmer",
        input=answer
    )

    file_path = Path(__file__).parent / ("files/audio"+str(index)+".mp3")

    audio.stream_to_file(file_path)

    display[1].audio(file_path, autoplay=False)

    illustrate = "Illustrate the text :"+answer[slice(500)]

    img = client.images.generate(
    prompt=illustrate,
    model="dall-e-2",
    n=1,
    size="512x512")

    display[2].image(img.data[0].url)

    display[0].text(answer)

    if new:
        st.session_state.history.append(answer)





if (opt1):
    create_chapter(client,display,"Ecrit la suite de l'histoire :"+prompt+"en moins de 600 caractères, où le choix 1 a été choisi, tu proposeras entre deux et trois choix d'options pour la suite. Si la situation te semble sans issue tu mettras un seul choix de fin a la place. Ne renvoie que la suite et les options.")
if (opt2):
   create_chapter(client,display,"Ecrit la suite de l'histoire :"+prompt+"en moins de 600 caractères, où le choix 2 a été choisi, tu proposeras entre deux et trois choix d'options pour la suite. Si la situation te semble sans issue tu mettras un seul choix de fin a la place. Ne renvoie que la suite et les options.")
if (opt3):
    create_chapter(client,display,"Ecrit la suite de l'histoire :"+prompt+"en moins de 600 caractères, où le choix 3 a été choisi, tu proposeras entre deux et trois choix d'options pour la suite. Si la situation te semble sans issue tu mettras un seul choix de fin a la place. Ne renvoie que la suite et les options.")
if (opt4):
    st.session_state.history.pop()
    create_chapter(client,display,"eh",False)
else:
    create_chapter(client,display,"Ecrit-moi l'introduction d'un livre dont vous etes le héros. Tu devras faire un texte de maximum 800 caractères. Tu proposeras ensuite trois choix en une phrase chacun pour poursuivre l'aventure.")
