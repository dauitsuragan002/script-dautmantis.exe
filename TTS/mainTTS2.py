import asyncio

import edge_tts

TEXT = "Мында өз сөзіңізді жазыңыз"

VOICE = "ru-RU-SvetlanaNeural" #ru-RU-SvetlanaNeural/kk-KZ-AigulNeural/ru-Ru-DmitryNeural kk-KZ-DauletNeural en-US-GuyNeural
OUTPUT_FILE = "TESTa_ru.mp3"
WEBVTT_FILE = "TESTa_ru.vtt"


async def _main() -> None:
    communicate = edge_tts.Communicate(TEXT, VOICE)
    submaker = edge_tts.SubMaker()
    with open(OUTPUT_FILE, "wb") as file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                file.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                submaker.create_sub((chunk["offset"], chunk["duration"]), chunk["text"])

    with open(WEBVTT_FILE, "w", encoding="utf-8") as file:
        file.write(submaker.generate_subs())
        
if __name__ == "__main__":
    asyncio.run(_main())
