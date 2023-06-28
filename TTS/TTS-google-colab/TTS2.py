# Скрипт - Дайын тексттік файл атауын нұсқау арқылы және таңдалынған атауы бар файлға  дыбыстап сақтау TTS2.py

import asyncio
import edge_tts

VOICE = "kk-KZ-DauletNeural" #ru-RU-SvetlanaNeural/kk-KZ-AigulNeural/ru-Ru-DmitryNeural kk-KZ-DauletNeural en-US-GuyNeural
OUTPUT_FILE = "test.mp3"
INPUT_FILE = "/content/12.txt"  #Дайын тексттік файлдың аты мен орнын нұсқаймыз

async def generate_audio(text):
    communicate = edge_tts.Communicate(text, VOICE)
    with open(OUTPUT_FILE, "wb") as file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                file.write(chunk["data"])

async def main():
    text = ''
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        for line in file:
            text += line
    text = text.strip()
    await generate_audio(text)

asyncio.create_task(main())
