# // point struct {x, y}
# //
# // shoot(point) -> bool -> True if ship was hit. Blocking. Reentrable. RPC under the hood. Takes from 1 to 10 sec.
# //
# // Implement:
# // volleyShot(point[]) -> bool -> true if at least one ship was hit. Return as soon as possible.

import asyncio
from typing import List, Tuple


async def shoot(point: Tuple[int, int]) -> bool: ...


async def volleyShot(points: List[Tuple[int, int]], max_concurrent: int) -> bool:
    errors = []

    tasks = set()

    points_iter = iter(points)
    while len(tasks) < max_concurrent:
        if p := next(points_iter, None):
            tasks.add(asyncio.create_task(shoot(p)))
        else:
            break

    while tasks:
        done, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        for task in done:
            try:
                result = task.result()
            except Exception as exc:
                errors.append(exc)
                result = False
            if result:
                for task in tasks:
                    task.cancel()
                return True
            else:
                if p := next(points_iter, None):
                    tasks.add(asyncio.create_task(shoot(p)))

    if any(errors):
        raise Exception(f"First error: {errors[0]}")
    return False
