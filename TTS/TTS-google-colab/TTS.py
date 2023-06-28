# Скрипт - Текстті осы алаңда көрсету арқылы және таңдалынған атауы бар файлға  дыбыстап сақтау TTS.py

import asyncio
import edge_tts

TEXT = "Мында өз сөзіңізді жазыңыз"

VOICE = "kk-KZ-AigulNeural" #ru-RU-SvetlanaNeural/kk-KZ-AigulNeural/ru-Ru-DmitryNeural kk-KZ-DauletNeural en-US-GuyNeural
OUTPUT_FILE = "Tkz.mp3"

async def generate_audio(text):
    communicate = edge_tts.Communicate(text, VOICE)
    with open(OUTPUT_FILE, "wb") as file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                file.write(chunk["data"])

async def main():
    await generate_audio(TEXT)

asyncio.create_task(main())
