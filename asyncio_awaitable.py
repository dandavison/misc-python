import asyncio


class Hello:
    def __init__(self):
        print("init")

    def __await__(self):
        async def closure():
            print("await")
            return self

        return closure().__await__()


async def main():
    h = Hello()
    await h
    await h


if __name__ == "__main__":
    asyncio.run(main())
