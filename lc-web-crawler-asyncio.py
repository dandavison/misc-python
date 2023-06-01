import asyncio
from urllib.parse import urlparse
from collections import deque
from typing import List


class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        return asyncio.run(self._crawl(startUrl, htmlParser))

    async def _crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = self.parse_hostname(startUrl)
        seen = {startUrl}
        coros = {self.fetch(startUrl, htmlParser)}
        while coros:
            done, coros = await asyncio.wait(coros, return_when=asyncio.FIRST_COMPLETED)
            for fut in done:
                urls = fut.result()
                urls = [url for url in urls
                        if url not in seen and self.parse_hostname(url) == hostname]
                seen.update(urls)
                coros.update(self.fetch(url, htmlParser) for url in urls)
        return list(seen)

    @staticmethod
    def parse_hostname(url: str) -> str:
        return urlparse(url).hostname


    async def fetch(self, url, htmlParser):
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, htmlParser.getUrls, url)

class Solution2:
    # Incorrect: not sure why
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        return asyncio.run(self._crawl(startUrl, htmlParser))

    async def _crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = lambda url: url.split('/')[2]
        seen = {startUrl}
        coros = [self.fetch(startUrl, htmlParser)]
        while coros:
            new_coros = []
            for coro in asyncio.as_completed(coros):
                urls = await coro
                urls = [url for url in urls
                        if url not in seen and self.parse_hostname(url) == hostname]
                seen.update(urls)
                new_coros.extend(self.fetch(url, htmlParser) for url in urls)
            coros = new_coros
        return list(seen)

    @staticmethod
    def parse_hostname(url: str) -> str:
        return urlparse(url).hostname

    async def fetch(self, url, htmlParser):
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, htmlParser.getUrls, url)
