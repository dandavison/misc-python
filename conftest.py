import xdist


def pprint(x):
    with open("/tmp/log", "a") as f:
        print(x, file=f)


def pytest_sessionfinish(session, exitstatus):
    pprint(
        f"in pytest_sessionfinish: {session} {exitstatus} worker: {xdist.is_xdist_worker(session)} master: {xdist.is_xdist_master(session)}"
    )
