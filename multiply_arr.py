"""
"""

from typing import List


class Solution:
    def sortedSquares(self, arr: List[int]) -> List[int]:
        low = 0
        high = len(arr) - 1
        out = []
        while low <= high:
            ls = arr[low] ** 2
            hs =  arr[high] ** 2
            if hs > ls:
                out.append(hs)
                high -= 1
            else:
                out.append(ls)
                low += 1
        return list(reversed(out))


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 4]
    assert s.sortedSquares(nums) == [1, 4, 9, 16]
    nums = [-4, -1, 2, 3]
    assert s.sortedSquares(nums) == [1, 4, 9, 16]
