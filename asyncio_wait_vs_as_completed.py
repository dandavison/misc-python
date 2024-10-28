import asyncio


async def using_wait():
    f1 = asyncio.Future()
    f2 = asyncio.Future()

    f1.set_result("f1-result")
    f2.set_result("f2-result")
    done, _ = await asyncio.wait([f1, f2], return_when=asyncio.FIRST_COMPLETED)
    assert len(done) == 2
    print("using wait:")
    for d in done:
        print("    ", await d)


async def using_as_completed():
    f1 = asyncio.Future()
    f2 = asyncio.Future()

    f1.set_result("f1-result")
    f2.set_result("f2-result")
    print("using as completed:")
    for d in asyncio.as_completed([f1, f2]):
        print("    ", await d)


asyncio.run(using_wait())
asyncio.run(using_as_completed())
