import streamlit as st


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