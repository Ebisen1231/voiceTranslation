import os
from openai import OpenAI
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

file = open("sample.wav","rb")

transcript = client.audio.translations.create(
    model="whisper-1",
    file=file,
)

print(transcript.text)
