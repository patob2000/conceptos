import streamlit as st



st.title("✍️ Markdown")

# Cargar un archivo de audio
audio_file = open('markdown.mp3', 'rb')
audio_bytes = audio_file.read()

# Mostrar el reproductor de audio
st.audio(audio_bytes, format='audio/mp3', start_time=0)


st.markdown("""
          
### Aprovechando Markdown para Formatear Textos

Escribir un libro con ChatGPT no solo implica qué escribir, sino cómo presentarlo.  
Markdown es un lenguaje de marcado ligero para formatear texto fácilmente.  
Piensa en Markdown como atajos rápidos para estilizar texto,  
similar a gestos en una escultura de arcilla: cada uno transforma la pieza.

Markdown te permite añadir encabezados, listas, cursivas, negritas y enlaces.  
Usa caracteres simples como asteriscos, guiones y corchetes.

Por ejemplo, **texto** aplica negrita, y # Título crea un encabezado de nivel uno.  
Esto es útil en la escritura de libros digitales con ChatGPT,  
ya que permite estructurar visualmente el contenido sin software complejo.

Imagina que esbozas la estructura de tu libro en un cuaderno.  
Con Markdown, cada anotación destacada es como usar un marcador de diferente color.  
Esto hace tu manuscrito más legible y organizado,  
y facilita la navegación y comprensión del lector.

Usar Markdown con ChatGPT es vital porque ChatGPT no crea formatos de documento complejos.  
Incorporar Markdown permite mantener control sobre el formato del texto final,  
asegurando que el libro sea rico en contenido, atractivo y fácil de leer.

En la preparación de un manuscrito para publicación, especialmente en formatos digitales,  
Markdown es invaluable.  
Plataformas de autoedición convierten archivos de Markdown a formatos de libro electrónico,  
simplificando la publicación y reduciendo la necesidad de diseño de formato manual.



            """)



st.markdown("""

### Códigos Markdown
            """)

st.code("""
# H1 - Encabezado nivel 1
## H2 - Encabezado nivel 2
### H3 - Encabezado nivel 3
#### H4 - Encabezado nivel 4
##### H5 - Encabezado nivel 5
###### H6 - Encabezado nivel 6

- Lista no ordenada
* Lista no ordenada
+ Lista no ordenada

1. Lista ordenada
2. Lista ordenada

> Bloque de cita

`Código en línea`



**Texto en negrita**
__Texto en negrita__

*Texto en cursiva*
_Texto en cursiva_

~~Texto tachado~~

[Texto del enlace](URL)

![Texto alternativo de la imagen](URL de la imagen)

| Tabla | Ejemplo | 
| --- | --- |
| Contenido de celda | Contenido de celda |


        """)