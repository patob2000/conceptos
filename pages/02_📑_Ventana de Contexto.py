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






st.title("📄 Ventana de Contexto")

# Cargar un archivo de audio
audio_file = open('ventana.mp3', 'rb')
audio_bytes = audio_file.read()

# Mostrar el reproductor de audio
st.audio(audio_bytes, format='audio/mp3', start_time=0)



st.markdown("""
          
### ¿Qué es la Ventana de Contexto?

Imagina que estás en una cafetería conversando con un amigo.  
A medida que hablan, tu amigo solo recuerda los últimos minutos.  
Si la conversación se alarga, los detalles iniciales se desvanecen de su memoria.

Esta limitación es similar a la "ventana de contexto" en ChatGPT.

ChatGPT, como tu amigo, tiene una memoria limitada.  
Solo "recuerda" el texto reciente en una conversación.  
Llamamos a esto ventana de contexto.  
ChatGPT solo considera cierto número de palabras o caracteres recientes al responder.  
Es excelente para seguir temas con la información más reciente.  
Pero puede "olvidar" detalles de conversaciones extensas.

La ventana de contexto es crucial en cómo ChatGPT maneja las conversaciones.  
Al escribir un libro o dialogar largo con ChatGPT,  
es vital estructurar tus entradas.  
Los puntos clave deben repetirse o resumirse.  
Así aseguras que la información importante se mantenga accesible para ChatGPT.

            """)



st.markdown("""  
---      
### FAQ Interactivas
            """)

choice = st.selectbox(
    '¿Quieres sabe más ...?',
    ('Selecciona alguna pregunta frecuente...',
     'Explícame la ventana de contexto, cómo si yo fuera un niño', 
     '¿Qué es la ventana de contexto y cómo afecta la generación de texto?', 
     '¿Cuáles son las limitaciones impuestas por la ventana de contexto y cómo se pueden mitigar?',
     "Cuéntame algo al estilo \"Ripley's Believe It or Not ...\" relacioando con la Ventana de Contexto...",
     "Una tabla con otros temas relacionados y su definición",
    ))

#st.markdown(f"Currrent value: {choice}")
if choice != "Selecciona alguna pregunta frecuente...":
    system = """
    Eres un asistente que responde solo preguntas y realiza aportes relacionadas estrechamente con *Inteligencia Artificial* y *Ventana de Contexto* en el ambito de la escritura de libros digitales.  
    Tus respuestas debe ser muy fáciles de comprender para personas que no tienen conocimiento técnico. 
    Utiliza negritas, listas y/o tablas, lo que necesites para hacer el texto mas legible y atractivo.
    Si la pregunta del usuario comienza con "Qué" ó "Cuales" utiliza analogías para responder.
    No ofrescas ayuda adicional, solo responde lo solicitado.
    """
    with st.spinner("espera ..."):
        # respuesta = procesar_solicitud_openai(system, choice)
        respuesta = procesar_solicitud_anthropic(system, choice)
        with st.chat_message("assistant"):
            #st.write(respuesta)
            _LOREM_IPSUM = respuesta
            st.write_stream(stream_data)




container = st.container(border=True)
container.page_link("pages/03_📑_Límite de Tokens.py", label="Click aquí para Continuar ...", icon="👉")

#prompt = st.chat_input("Say something")
##if prompt:
###    system=""
#    _LOREM_IPSUM = ""
#    respuesta = procesar_solicitud_anthropic(system, prompt)
#    with st.chat_message("assistant"):
#        #st.write(respuesta)
#        _LOREM_IPSUM = respuesta
#        st.write_stream(stream_data)

