from concurrent.futures import ThreadPoolExecutor


def raise_exception():
    raise Exception("Deliberate error")


def do_work():
    return 1 + 1


def reporter(fut):
    print(fut)


executor = ThreadPoolExecutor()
fut = executor.submit(do_work)
fut.add_done_callback(reporter)
print(fut.result())
