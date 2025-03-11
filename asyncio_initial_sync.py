import asyncio
from dataclasses import dataclass
from typing import Any


@dataclass
class WorkflowHandle:
    response: Any


class RequestBatch:
    def __init__(self):
        self._handle = asyncio.Future[WorkflowHandle]()
        self._started = False

    async def get_handle(self) -> WorkflowHandle:
        return await self._handle

    async def execute_update(self):
        if self._started:
            raise Exception("Cannot issue update more than once")
        self._started = True
        resp = await self._send_request()
        self._handle.set_result(WorkflowHandle(resp))

    async def _send_request(self) -> Any:
        await asyncio.sleep(0.1)
        return "response"


b = RequestBatch()
asyncio.gather(b.execute_update(), b.execute_update())
