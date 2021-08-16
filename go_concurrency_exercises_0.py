# https://github.com/loong/go-concurrency-exercises/tree/master/0-limit-crawler
import time
from threading import Thread
from queue import Queue


class Ticker:
    def __init__(self, seconds: float):
        self.queue = Queue()
        self.seconds = seconds
        self.thread = Thread(target=self.tick)
        self.thread.start()

    def tick(self):
        while True:
            self.queue.put(None)
            time.sleep(self.seconds)

    def wait(self):
        self.queue.get()

    def join(self):
        self.thread.join()


def make_crawler(url, depth):
    def closure():
        return crawl(url, depth)

    return Thread(target=closure)


def crawl(url: str, depth: int):
    if depth <= 0:
        return

    ticker.wait()
    body, urls, err = fetch(url)
    for url in urls:
        thread = make_crawler(url, depth - 1)
        thread.start()


def fetch(url: str):
    print(f"fetch: {url}")
    data = {
        "http://golang.org/": {
            "body": "The Go Programming Language",
            "urls": {
                "http://golang.org/pkg/",
                "http://golang.org/cmd/",
            },
        },
        "http://golang.org/pkg/": {
            "body": "Packages",
            "urls": {
                "http://golang.org/",
                "http://golang.org/cmd/",
                "http://golang.org/pkg/fmt/",
                "http://golang.org/pkg/os/",
            },
        },
        "http://golang.org/pkg/fmt/": {
            "body": "Package fmt",
            "urls": {
                "http://golang.org/",
                "http://golang.org/pkg/",
            },
        },
        "http://golang.org/pkg/os/": {
            "body": "Package os",
            "urls": {
                "http://golang.org/",
                "http://golang.org/pkg/",
            },
        },
    }
    res = data.get(url)
    if res:
        return res["body"], res["urls"], None
    else:
        return None, [], "ERROR: not found"


def test_ticker():
    ticker = Ticker(0.87)
    prev = time.time()
    while True:
        ticker.wait()
        cur = time.time()
        print(cur - prev)
        prev = cur


if __name__ == "__main__":
    ticker = Ticker(1.0)
    make_crawler("http://golang.org/", 4).start()
    time.sleep(60)
