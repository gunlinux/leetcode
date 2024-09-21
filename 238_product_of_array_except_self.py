"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


"""

from typing import List
from functools import reduce


def divide_by_subtraction(x, y):
    quotient = 0
    while x >= y:
        if y < 0:
            break
        x -= y
        quotient += 1
    return quotient


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        You must write an algorithm that runs in O(n) time and without using the division operation.
        2 <= nums.length <= 105
        -30 <= nums[i] <= 30
        """

        big = 1
        zero = False
        double = False
        for x in nums:
            if x != 0:
                big = big * x
            else:
                if zero:
                    double = True
                    break
                zero = True

        out: List[int] = [big] * len(nums) if not zero else [0] * len(nums)
        if double:
            return out

        for i, el in enumerate(out):
            if zero:
                if nums[i] == 0:
                    out[i] = big
                continue
            if nums[i] != 0:
                out[i] = int(out[i] / nums[i])
        return out

if __name__ == "__main__":
    s = Solution()
    ai = [1, 2, 3, 4]
    ao = [24, 12, 8, 6]
    #assert s.divide_by_subtraction(30, 5) == 6
    #assert s.divide_by_subtraction(24, 2) == 12
    #assert s.divide_by_subtraction(18, 3) == 6
    print(ao)
    assert s.productExceptSelf(ai) == ao
    bi = [-1, 1, 0, -3, 3]
    bo = [0, 0, 9, 0, 0]
    assert s.productExceptSelf(bi) == bo
