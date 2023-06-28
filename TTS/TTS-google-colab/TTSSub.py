import asyncio
import edge_tts
import fileinput

VOICE = "kk-KZ-DauletNeural" #ru-RU-SvetlanaNeural/kk-KZ-AigulNeural/ru-Ru-DmitryNeural
OUTPUT_FILE = "test.mp3"
WEBVTT_FILE = "test.vtt"

async def _main() -> None:
    # Укажите текст напрямую
    text = "Ваш текст здесь"
    
    # Генерируем аудио файл
    communicate = edge_tts.Communicate(text, VOICE)
    submaker = edge_tts.SubMaker()
    with open(OUTPUT_FILE, "wb") as file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                file.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                submaker.create_sub((chunk["offset"], chunk["duration"]), chunk["text"])

    # Генерируем файл с субтитрами в формате WebVTT
    with open(WEBVTT_FILE, "w", encoding="utf-8") as file:
        file.write(submaker.generate_subs())

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(_main())
    finally:
        loop.close()
