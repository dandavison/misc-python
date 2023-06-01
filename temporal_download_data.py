"""
Implement a function that, given an array of URLs and a download function, downloads all the data from the urls, merges it into a single dictionary of {url:data} and return a method with parallelism (concurrency)
"""
import asyncio
from typing import Dict, List

import aiohttp

async def download(url, session):
    async with session.get(url) as response:
        return await response.read()


async def download_all(urls: List[str]) -> Dict[str, str]:
    async with aiohttp.ClientSession() as session:
    if False:
            data = await asyncio.gather(*(download(url, session) for url in urls))
        data = [v[:100] for v in data]
        return dict(zip(urls, data))
    else:
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(download(url, session)) for url in urls]

        import pdb; pdb.set_trace()
        return result

def main():
    result = asyncio.run(download_all(['https://www.gov.uk', 'https://www.theguardian.com']))
    print(result)

main()
