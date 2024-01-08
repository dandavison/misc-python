import asyncio

import aiohttp


async def request():
    session = aiohttp.ClientSession()

    resp = await session.get("http://localhost:7777/invalid-json")

    try:
        await resp.json()
    except Exception as exc:
        print(f"caught {exc}")

    print(await resp.read())
    await session.close()


asyncio.run(request())
