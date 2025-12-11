import httpx

text = "こんにちは、テスト音声です。"

async def test_voicevox():
    async with httpx.AsyncClient() as client:
        query = await client.post(
            "http://localhost:50021/audio_query",
            params={"text": text, "speaker": 1}
        )
        wav = await client.post(
            "http://localhost:50021/synthesis",
            params={"speaker": 1},
            content=query.content
        )
        with open("voice/out.wav", "wb") as f:
            f.write(wav.content)

import asyncio
asyncio.run(test_voicevox())
