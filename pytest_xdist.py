import os

import pytest

os.system("rm -f /tmp/log")


def pprint(x):
    with open("/tmp/log", "a") as f:
        print(x, file=f)


@pytest.fixture(scope="session")
def session_data(worker_id):
    pprint(f"worker_id: {worker_id}")


def test_1(session_data):
    pprint("in test 1")


def test_2(session_data):
    pprint("in test 2")


def test_3(session_data):
    pprint("in test 3")


def test_4(session_data):
    pprint("in test 4")


def test_5(session_data):
    pprint("in test 5")


def test_6(session_data):
    pprint("in test 6")


def test_7(session_data):
    pprint("in test 7")


def test_8(session_data):
    pprint("in test 8")


def test_9(session_data):
    pprint("in test 9")


def test_10(session_data):
    pprint("in test 10")
