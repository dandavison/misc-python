from urllib.parse import urlparse
from collections import deque
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
from typing import List


class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = self.parse_hostname(startUrl)
        seen = {startUrl}
        mutex = Lock()

        with ThreadPoolExecutor(max_workers=16) as executor:
            futures = [executor.submit(htmlParser.getUrls, startUrl)]
            while futures:
                for fut in as_completed(futures):
                    futures.remove(fut)
                    urls = [url for url in fut.result()
                            if url not in seen and self.parse_hostname(url) == hostname]
                    with mutex:
                        seen.update(urls)
                    futures.extend(executor.submit(htmlParser.getUrls, url) for url in urls)


        return list(seen)

    @staticmethod
    def parse_hostname(url: str) -> str:
        return urlparse(url).hostname
