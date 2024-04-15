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



st.title("🚧 Tokens de Salida")

# Cargar un archivo de audio
audio_file = open('tokens.mp3', 'rb')
audio_bytes = audio_file.read()

# Mostrar el reproductor de audio
st.audio(audio_bytes, format='audio/mp3', start_time=0)



st.markdown("""

            
### Entendiendo el Límite de Tokens de Salida

Trabajar con ChatGPT en la creación de contenidos implica entender los tokens.  
Piensa en cada token como un ladrillo en una construcción.  
No todos los ladrillos son iguales.  
Algunos son una palabra completa, otros solo una parte, y otros signos de puntuación.

Esta variabilidad es crucial.  
ChatGPT tiene un límite de cuántos tokens puede usar para construir una respuesta.

Este límite significa que hay un máximo de texto que ChatGPT puede generar por interacción.  
Es como escribir un capítulo con un número limitado de palabras.  
Si solo tienes 1000 palabras, debes elegir cuidadosamente qué incluir.

ChatGPT debe optimizar el uso de sus tokens dentro de este espacio limitado.

Además, debido a este límite, es imposible escribir un libro entero de una vez con ChatGPT.  
Así como una persona no puede narrar una historia completa sin pausas,  
ChatGPT necesita múltiples entradas y ajustes para abarcar algo tan extenso como un libro.

Por lo tanto, al planificar escribir un libro con ChatGPT,  
es esencial entender y adaptarse a estas limitaciones de tokens.  
Debes estructurar el contenido en segmentos manejables.  
Esto permite que ChatGPT desarrolle cada parte efectivamente en cada interacción.




            """)



st.markdown("""  
---      
### FAQ Interactivas
            """)

choice = st.selectbox(
    '¿Quieres sabe más ...?',
    ('Selecciona alguna pregunta frecuente...',
     'Explícame los Tokens, cómo si yo fuera un niño', 
     '¿Qué son Tokens y cómo afecta la generación de texto?', 
     "Cuéntame algo al estilo \"Ripley's Believe It or Not ...\" relacioando con los Tokens",
     "Una tabla con otros temas relacionados y su definición",
    ))

#st.markdown(f"Currrent value: {choice}")
if choice != "Selecciona alguna pregunta frecuente...":
    system = """
    Eres un asistente que responde solo preguntas y realiza aportes relacionadas estrechamente con *Inteligencia Artificial* y *Límite de Tokens de Salida* en el ambito de la escritura de libros digitales.  
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





st.markdown("---")
container = st.container(border=True)
container.page_link("pages/04_📑_Alucinaciones.py", label="Click aquí para Continuar ...", icon="👉")
