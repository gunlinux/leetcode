"""
"""
from typing import List


class Solution:
    def __init__(self):
        self.memo = {}

    def climbStairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        if n < 3:
            return n
        r = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.memo[n] = r
        return r

        #
class SolutionI:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        a = 1
        b = 2
        for i in range(2, n):
            b,a = a + b, b
        return b


if __name__ == "__main__":
    s = SolutionI()
    assert s.climbStairs(1) == 1
    assert s.climbStairs(2) == 2
    assert s.climbStairs(3) == 3
    assert s.climbStairs(4) == 5
    assert s.climbStairs(5) == 8
