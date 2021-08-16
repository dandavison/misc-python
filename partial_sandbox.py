from typing import Callable


def my_workflow():
    print("my_workflow")
    import random

    print(random.random())


def my_activity():
    print("my_activity")
    import random

    print(random.random())


def worker():
    get_next_workflow_task(my_workflow)
    execute_activity(my_activity)


def execute_activity(activity: Callable[[], None]):
    activity()


def get_next_workflow_task(workflow: Callable[[], None]):
    execute_in_sandbox(workflow)


def execute_in_sandbox(fn):
    sandbox_globals = construct_global_namespace_with_omissions_and_substitutions()
    exec(fn.__code__, globals=sandbox_globals)


if __name__ == "__main__":
    worker()