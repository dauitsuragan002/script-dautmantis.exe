import asyncio
import edge_tts

VOICE = "kk-KZ-DauletNeural"
OUTPUT_FILE = "test.mp3"
WEBVTT_FILE = "test.vtt"

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

async def main():
    text = "Осында өзіңіздің текстіңізді жазсаңыз болады"
    await generate_audio(text)

asyncio.create_task(main())
