import os
import time
from dataclasses import dataclass
from queue import Queue
from threading import Thread, Lock

latest_prices = {}  # hash map: ticker_symbol => (price, time)
mutex = Lock()


def make_thread_A():
    """
    Read messages from streaming API and update in-memory dictionary of latest prices.
    """

    def closure():
        cnxn = FinanceApiConnection(
            os.environ.get("FINANCE_API_USER"), os.environ.get("FINANCE_API_PASSWORD")
        )
        for msg in cnxn.stream():
            with mutex:
                print(f"{msg.ticker_symbol}: {msg.price}")
                latest_prices[msg.ticker_symbol] = (msg.price, msg.time)

    return Thread(target=closure)


def make_thread_B(ticker: "Ticker"):
    """
    Periodically write in-memory data to durable storage.

    Period is determined by `ticker`.
    """
    time_series_length = 1000
    one_day = 24 * 60 * 60
    time_series_intervals = {
        "last_day": one_day / time_series_length,
        "last_month": 30 * one_day / time_series_length,
        "last_year": 365 * one_day / time_series_length,
    }

    def closure():
        while True:
            ticker.wait()
            with mutex:
                write_to_data_store(latest_prices)

    return Thread(target=closure)


class Ticker:
    def __init__(self, period: float):
        self.channel = Queue()
        self.period = period
        self.thread = Thread(target=self.tick)
        self.thread.start()

    def tick(self):
        while True:
            self.channel.put(None)
            time.sleep(self.period)

    def wait(self):
        self.channel.get()  # receive from timer channel blocks if empty

    def join(self):
        self.thread.join()


TICKER_SYMBOLS = ["AMZN", "UBER", "TMPRL"]


@dataclass
class Message:
    ticker_symbol: str
    price: int
    time: int


class FinanceApiConnection:
    def __init__(self, user, password):
        # authenticate and establish SSE connection
        pass

    def stream(self):
        import random

        timestamp = 1629914352
        while True:
            yield Message(
                random.choice(TICKER_SYMBOLS), random.randint(100, 200), timestamp
            )
            next_time = random.randint(0, 2)
            time.sleep(next_time)
            timestamp += next_time


def write_to_data_store(latest_prices):
    print("*** Write to data store")


if __name__ == "__main__":
    timer_channel = Queue()

    ticker = Ticker(0.5)

    thread_A = make_thread_A()
    thread_B = make_thread_B(ticker)

    for t in [thread_A, thread_B]:
        t.start()

    ticker.join()
    for t in threads:
        t.join()
