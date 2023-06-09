# Challenge 11:

# In this challenge, you are to demonstrate asyncio's ability to execute I/O-bound tasks more efficiently through concurrency.

# Write a program that fetches several URLs, using aiohttp to make the requests concurrently. However, you should limit the number of requests that are made at the same time, so you don't exhaust resources or get blocked by the server. You can use the asyncio.Semaphore for this purpose.

# Your main coroutine should create an aiohttp.ClientSession, and use it to fetch the URLs. Each URL fetch will be a coroutine that waits for a semaphore before making the request.

# You can use any URLs you like for this challenge, but make sure they're suitable for large-scale testing (i.e., not small sites that could be disrupted, or sites that may block you for making too many requests).

# Use the provided fetch_url coroutine to implement your solution.
import asyncio

import aiohttp


URLS = [
    "https://chat.openai.com/",
    "https://app.coderpad.io/",
    "https://drive.google.com/",
    "https://music.youtube.com/",
    "https://mail.google.com/",
]


async def fetch_url(url: str, semaphore: asyncio.Semaphore):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                text = await response.text()
                print(f"Got {url}: {text[:20]}")
                await asyncio.sleep(3)
                return text

async def main(max_in_flight):
    semaphore = asyncio.Semaphore(max_in_flight)
    await asyncio.gather(*(fetch_url(url, semaphore) for url in URLS))

asyncio.run(main(max_in_flight=3))
