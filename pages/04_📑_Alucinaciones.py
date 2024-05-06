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


st.title("👁️‍🗨️ Alucinaciones")

# Cargar un archivo de audio
audio_file = open('alucinaciones.mp3', 'rb')
audio_bytes = audio_file.read()

# Mostrar el reproductor de audio
st.audio(audio_bytes, format='audio/mp3', start_time=0)


st.markdown("""

### Comprendiendo las Alucinaciones en ChatGPT

Usar ChatGPT para escribir o informarse puede llevar a un fenómeno llamado "alucinaciones".  
Este término evoca visiones no basadas en la realidad.  
De hecho, eso es lo que sucede.  
ChatGPT intenta llenar huecos de conocimiento con detalles inventados,  
como un novelista añadiendo elementos a una historia.

Este fenómeno se debe a su entrenamiento.  
A partir de vastos textos, aprende a predecir palabras o frases,  
basándose en patrones y correlaciones.  
No tiene acceso a una base de datos de hechos reales en tiempo real.  
A veces "improvisa" basándose en las probabilidades.

Imagina que dibujas un mapa de un lugar visitado hace tiempo;  
algunos detalles pueden ser incorrectos o imaginados.

Las alucinaciones son un desafío cuando se requiere precisión factual,  
como en libros de historia o guías técnicas.  
Es crucial ser consciente de que la información de ChatGPT no siempre es 100% precisa.  
Verificar los hechos es necesario.

Al usar ChatGPT para escribir un libro, adopta un enfoque crítico.  
Analizar y corroborar la información es esencial.  
Asegura la calidad y exactitud del contenido.  
Es similar a revisar un borrador inicial de un libro,  
donde autores y editores pulen y mejoran el texto.
            """)




st.markdown("""  
---      
### FAQ Interactivas
            """)

choice = st.selectbox(
    '¿Quieres sabe más ...?',
    ('Selecciona alguna pregunta frecuente...',
     'Explícame las Alucinaciones en los modelos llm, cómo si yo fuera un niño', 
     '¿Qué es las Alucinaciones en los modelos llm y cómo afecta la generación de texto?', 
     "Cuéntame algo al estilo \"Ripley's Believe It or Not ...\" relacioando con las Alucinaciones en los modelos llm",
     "Una tabla con otros temas relacionados y su definición",
    ))

#st.markdown(f"Currrent value: {choice}")
if choice != "Selecciona alguna pregunta frecuente...":
    system = """
    Eres un asistente que responde solo preguntas y realiza aportes relacionadas estrechamente con *Inteligencia Artificial* y *Alucinaciones en los modelos llm* en el ambito de la escritura de libros digitales.  
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
container.page_link("pages/05_📑_Markdown.py", label="Click aquí para Continuar ...", icon="👉")


st.write("---")
st.caption("Creado con [www.aulasimple.ia](https://aulasimple.ai/plataforma)")