import asyncio
import edge_tts

TEXT = "Мында өз сөзіңізді жазыңыз"

VOICE = "kk-KZ-AigulNeural" #ru-RU-SvetlanaNeural/kk-KZ-AigulNeural/ru-Ru-DmitryNeural kk-KZ-DauletNeural en-US-GuyNeural
OUTPUT_FILE = "example.mp3"

async def _main() -> None:
    communicate = edge_tts.Communicate(TEXT, VOICE)
    with open(OUTPUT_FILE, "wb") as file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                file.write(chunk["data"])
        
if __name__ == "__main__":
    asyncio.run(_main())
