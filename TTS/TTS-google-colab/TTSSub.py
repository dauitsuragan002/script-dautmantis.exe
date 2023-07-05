# Скрипт - Текстті осы алаңда көрсету арқылы және таңдалынған атауы бар файлға  дыбыстап,авто субтитр жасап сақтау TTSSub.py

import asyncio
import edge_tts
import os

VOICE = "kk-KZ-DauletNeural" #ru-RU-SvetlanaNeural/kk-KZ-AigulNeural/ru-Ru-DmitryNeural kk-KZ-DauletNeural en-US-GuyNeural
OUTPUT_FILE = "test.mp3"
WEBVTT_FILE = "test.vtt"
SRT_FILE = "test.srt"

async def generate_audio(text):
    communicate = edge_tts.Communicate(text, VOICE)
    submaker = edge_tts.SubMaker()
    with open(OUTPUT_FILE, "wb") as file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                file.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                submaker.create_sub((chunk["offset"], chunk["duration"]), chunk["text"])

    with open(WEBVTT_FILE, "w", encoding="utf-8") as file:
        file.write(submaker.generate_subs())

    vtt_to_srt(WEBVTT_FILE, SRT_FILE)
    os.remove(WEBVTT_FILE)

def vtt_to_srt(vtt_file, srt_file):
    with open(vtt_file, "r", encoding="utf-8") as vtt:
        vtt_content = vtt.read()

    srt_content = vtt_content.replace("WEBVTT\n\n", "")
    vtt_subtitles = srt_content.split("\n\n")

    srt_content = ""
    for i, vtt_subtitle in enumerate(vtt_subtitles, start=1):
        if vtt_subtitle.strip(): 
            srt_content += f"{i}\n{vtt_subtitle}\n\n"

    with open(srt_file, "w", encoding="utf-8") as srt:
        srt.write(srt_content)

async def main():
    text = "Осында өзіңіздің  текстіңізді жазыңыз" #Осында өзіңіздің  текстіңізді жазыңыз  
    await generate_audio(text)

asyncio.create_task(main())
