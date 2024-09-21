"""
"""

from typing import List, Optional


class MinStack:

    def __init__(self):
        self.data: List[tuple[int, int]] = []

    def push(self, val: int) -> None:
        if not self.data:
            self.data.append((val, val))
            return
        self.data.append((val, min(self.data[-1][1], val)))

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == "__main__":
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    stack.getMin() == -3
    stack.pop()
    print(stack.top())
    assert stack.getMin() == -2
