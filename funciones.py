from openai import OpenAI
def procesar_solicitud_openai(system,user):
    # Accede a la clave API de OpenAI desde secrets.toml
    client = OpenAI()
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": user}
    ]
    )
    return response.choices[0].message.content


#claude-3-opus-20240229
from anthropic import Anthropic
def procesar_solicitud_anthropic(system,user):
    client = Anthropic()
    response = client.messages.create(
        system=system,
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": user,
            }
        ],
        model="claude-3-haiku-20240307",
    )
    return response.content[0].text