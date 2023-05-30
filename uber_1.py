# Verify whether a long text is following the order rule defined in order
# string. For example the order string is "abcd", which means "a" can't appear
# at any position after "b", "c" and "d" in the text, "b" can't appear at any
# position after "c" and "d" in the text and "c" can't appear at any position
# after "d" in the text. if the text is "axubbxcxbxd", then the text didn't
# follow the rule, since "b" appears after "c" in substring "cxb". This question
# has two parts: The first part is to just implement the verification function
# in single thread, This is the simple part. The second part is how to separate
# the big data set to small data set and run it in parallel, if the text string
# is super large. This is the complicated part. The character in order and text
# string is 8-bit ASCII. And there won't be repeating characters.
from typing import Tuple

def verify(text, order) -> Tuple[bool, int]:
    # order = abcd
    # text = axxxcxxxb ! invalid
    # text = axxxcxxxxd ok

    order_idx = -1
    order_map = {c: i for i, c in enumerate(order)}
    for c in text:
        c_order_idx = order_map.get(c)
        if c_order_idx is not None:
            if c_order_idx < order_idx:
                return False, -1
            else:
                order_idx = c_order_idx
    return True, order_idx


from enum import Enum
from threading import Lock

class Method(Enum):
    THREADS = 1
    THREAD_POOL = 2

method = Method.THREAD_POOL

def verify_parallel(text, order, n_tasks):

    chunks = make_chunks(text, n_tasks)

    results = []
    mutex = Lock()

    def task(id, text):
        is_valid, order_idx = verify(text, order)
        with mutex:
            results.append((id, is_valid, order_idx))

    if method == Method.THREADS:
        from threading import Thread
        threads = [Thread(target = lambda: task(id, chunk)) for id, chunk in enumerate(chunks)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

    elif method == Method.THREAD_POOL:
        from concurrent.futures import ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=1) as executor:
            _ = list(executor.map(lambda args: task(*args), enumerate(chunks)))

    return verify_results(results)

def make_chunks(items, n_chunks):
    assert n_chunks > 0
    chunk_size, rem = divmod(len(items), n_chunks)
    if rem:
        chunk_size += 1

    chunks = []
    while items:
        chunks.append(items[:chunk_size])
        items = items[chunk_size:]

    return chunks


def verify_results(results):
    curr_idx = -1
    for id, is_valid, order_idx in sorted(results):
        if not is_valid:
            return False
        elif order_idx < curr_idx:
            return False
        else:
            curr_idx = order_idx
    return True



assert make_chunks([], 1) == []
assert make_chunks([], 2) == []
assert make_chunks([0], 1) == [[0]]
assert make_chunks([0], 2) == [[0]]
assert make_chunks([0, 1], 1) == [[0, 1]]
assert make_chunks([0, 1], 2) == [[0], [1]]
assert make_chunks([0, 1], 3) == [[0], [1]]
assert make_chunks([0, 1, 2], 1) == [[0, 1, 2]]
assert make_chunks([0, 1, 2], 2) == [[0, 1], [2]], make_chunks([0, 1, 2], 2)
assert make_chunks([0, 1, 2], 3) == [[0], [1], [2]]


assert not verify("axubbxcxbxd", "abcd")[0]
assert verify("a", "ab")[0]
assert verify("b", "ab")[0]
assert verify("bx", "ab")[0]
assert not verify("ba", "ab")[0]
assert not verify("bxa", "ab")[0]


assert verify_parallel("a", "ab", 3)
assert verify_parallel("b", "ab", 3)
assert verify_parallel("bx", "ab", 3)
# assert not verify_parallel("ba", "ab", 3)
# assert not verify_parallel("bxa", "ab", 3)
assert not verify_parallel("axubbxcxbxd", "abcd", 2)
