class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        return self._front(remove=True)

    def peek(self) -> int:
        return self._front(remove=False)

    def _front(self, remove: bool) -> Optional[int]:
        for _ in range(len(self.stack1) - 1):
            self.stack2.append(self.stack1.pop())
        val = self.stack1.pop() if remove else self.stack1[-1]
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return val

    def empty(self) -> bool:
        return len(self.stack1) == 0
