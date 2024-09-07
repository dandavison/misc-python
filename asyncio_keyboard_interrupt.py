import asyncio

try:
    asyncio.run(asyncio.sleep(float("inf")))
except KeyboardInterrupt as e:
    import pdb

    pdb.set_trace()
    print("hello", e)
