import asyncio
import edge_tts
import fileinput

VOICE = "kk-KZ-DauletNeural" 
OUTPUT_FILE = "test.mp3"

async def _main() -> None:
    text = ''
    with fileinput.input(files=('Файл атауын расширениесімен көрсетіңіз.txt'), openhook=fileinput.hook_encoded("utf-8")) as file:
        for line in file:
            text += line
    text = text.strip()
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(OUTPUT_FILE)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(_main())
    finally:
        loop.close()
