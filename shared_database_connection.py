def fetch_1(id, cnxn):
    with cnxn:
        fut = cnxn.query(id)
        yield
    # can't use cnxn
    result = fut.result
    [result]


def queries_2(id):
    fut = cnxn.query(id)
    yield
    result = fut.result
    fut2 = cnxn.query(id)
    yield fut2


def fetch_2(id, cnxn):
    fut = yield from queries_2()
    result2 = fut.result
    [result, result2]


def fetch_all(id, cnxn):
    fetch_fns = [fetch_1, fetch_2]
    gens = []
    for fn in fetch_fns:
        gen = fn(id, cnxn)
        next(gen)
        gens.append(gen)

    cnxn.execute()

    results = []
    finished = set()
    while True:
        if finished == set(gens):
            break
        for gen in gens:
            try:
                results.extend(next(gen))
            except StopIteration:
                finished.add(gen)

    return results


def subgen():
    yield 2
    yield 3


def mygen():
    yield 1
    yield from subgen()
    yield 4


print(list(mygen()))