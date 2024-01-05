import asyncio

import aiohttp


async def request():
    session = aiohttp.ClientSession()

    resp = await session.get("http://localhost:7777/valid-json")
    print(await resp.json())
    await session.close()


asyncio.run(request())
