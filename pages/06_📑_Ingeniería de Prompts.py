import streamlit as st


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

