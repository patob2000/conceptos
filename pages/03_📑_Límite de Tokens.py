import streamlit as st

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


# Crear dos columnas para los campos de entrada

container = st.container(border=True)
container.page_link("pages/02_📑_Ventana de Contexto.py", label="Click aquí para Continuar ...", icon="👉")
