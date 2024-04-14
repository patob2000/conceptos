import streamlit as st





st.title("🚀 Introducción")

# Cargar un archivo de audio
audio_file = open('introduccion.mp3', 'rb')
audio_bytes = audio_file.read()

# Mostrar el reproductor de audio
st.audio(audio_bytes, format='audio/mp3', start_time=0)



st.markdown("""


¿Sabías que el 90% de los e-books creados con IA son un poco... meh? 😕

La mayoría no destaca por falta de un ingrediente crucial:  
el entendimiento profundo de la interacción con la inteligencia artificial.

No basta con pedir a ChatGPT que genere texto tras texto.  
Hay arte y ciencia en hacerlo bien.

Este libro busca cambiar eso.

Exploraremos conceptos esenciales que muchos ignoran,  
pero que son fundamentales para crear algo genial con IA.

Discutiremos cómo entender la ventana de contexto,  
manejar los tokens efectivamente,  
y cómo enfrentar las "alucinaciones" que complican las cosas.  
Entender esto hace que la relación humano-IA sea más fluida y productiva.

Si estás cansado de resultados mediocres y aspiras a estar en el 10% que realmente hace magia,  
este es tu libro. 

Te mostraremos cómo dominar estos trucos del oficio,  
para que puedas crear no solo un buen e-book, sino una obra que realmente resalte. 


            """)

