import streamlit as st
import streamlit_shadcn_ui as ui
from funciones import procesar_solicitud_openai, procesar_solicitud_anthropic
import time
import numpy as np


_LOREM_IPSUM = ""


def stream_data():
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)


st.title("⚙️ Ingeniería en prompt")

# Cargar un archivo de audio
audio_file = open('prompt.mp3', 'rb')
audio_bytes = audio_file.read()

# Mostrar el reproductor de audio
st.audio(audio_bytes, format='audio/mp3', start_time=0)





st.markdown("""

Dominar los prompts en ChatGPT es como dirigir una orquesta 🎼.  
No solo pides música.  
Especificas qué instrumentos destacan y cuándo.  
Esta habilidad cambia cómo interactúas con la **inteligencia artificial**.  
Asegura que tu contenido sea original y auténticamente tuyo.

Cuando dominas un prompt, tu contenido deja de ser un eco.  
Ya no te sientes falso usando IA en tu creatividad.

Un buen prompt es clave para respuestas detalladas de ChatGPT.  
No solo lanzas preguntas.  
Construyes solicitudes que guían a la IA hacia lo que quieres.  
Por ejemplo, en vez de "dame información sobre Shakespeare",  
podrías decir "explícame cómo 'Macbeth' refleja las preocupaciones políticas de su época".  
Esto evita errores de la IA y enriquece la conversación.

Formular bien las preguntas maximiza el provecho de ChatGPT.  
Es una extensión de tu creatividad.  
Te permite explorar temas en profundidad y con matices.  
Conocer los límites de la ventana de contexto y manejo de tokens,  
te ayuda a mantener la conversación enfocada y efectiva.

Aprender a diseñar prompts es **esencial** para usar bien la IA.  
Te da el control para que tu contenido refleje tu intención y voz.

Afinar esta habilidad te aleja de ser un simple usuario.  
Te convierte en un verdadero innovador literario 🌟.

            """)




st.markdown("""  
---      
### FAQ Interactivas
            """)

choice = st.selectbox(
    '¿Quieres sabe más ...?',
    ('Selecciona alguna pregunta frecuente...',
     'Explícame la Ingeniería en Prompt en los modelos llm, cómo si yo fuera un niño', 
     '¿Qué es la Ingeniería en Prompt y cómo afecta la generación de texto?', 
     "Cuéntame algo al estilo \"Ripley's Believe It or Not ...\" relacioando con la Ingeniería en Prompt",
     "Una tabla con otros temas con Notación Markdown relacionados y su definición",
    ))

#st.markdown(f"Currrent value: {choice}")
if choice != "Selecciona alguna pregunta frecuente...":
    system = """
    Eres un asistente que responde solo preguntas y realiza aportes relacionadas estrechamente con *Inteligencia Artificial* y *Ingeniería en Prompt en los modelos llm* en el ambito de la escritura de libros digitales.  
    Tus respuestas debe ser muy fáciles de comprender para personas que no tienen conocimiento técnico. 
    Utiliza negritas, listas y/o tablas, lo que necesites para hacer el texto mas legible y atractivo.
    Si la pregunta del usuario comienza con "Qué" ó "Cuales" utiliza analogías para responder.
    *No ofrescas ayuda adicional, solo responde lo solicitado*.
    """
    with st.spinner("espera ..."):
        # respuesta = procesar_solicitud_openai(system, choice)
        respuesta = procesar_solicitud_anthropic(system, choice)
        with st.chat_message("assistant"):
            #st.write(respuesta)
            _LOREM_IPSUM = respuesta
            st.write_stream(stream_data)





st.markdown("---")
container = st.container(border=True)
container.page_link("pages/07_📑_Autor.py", label="Click aquí para Continuar ...", icon="👉")


st.write("---")
st.caption("Creado con [www.aulasimple.ia](https://aulasimple.ai/plataforma)")