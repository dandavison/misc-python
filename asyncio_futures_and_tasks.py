import asyncio


class WorkflowHandle:
    def execute_update(self): ...
    def query(self): ...


class Client:
    def start(self) -> WorkflowHandle:
        return WorkflowHandle()


class LazyWorkflowHandle:
    def __await__(self):
        async def g():
            return WorkflowHandle()

        return g().__await__()


async def c():
    lh = LazyWorkflowHandle()
    h = await lh
    print(h)


if __name__ == "__main__":
    asyncio.run(c())
