"""
You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significann
left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.


Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""

from collections import deque


class Solution:
    def plusOneFast(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            k = digits[i]
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                if i == 0:
                    digits[i] = 1
                    digits.append(0)
                else:
                    digits[i] = 0
            print(k)
        return digits

    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[len(digits)-1] != 9:
            digits[len(digits)-1] = digits[len(digits)-1] + 1
            return digits
        out = deque()
        over = 1
        i = len(digits) - 1
        while i >= 0 or over:
            if i >= 0:
                over += digits[i]
                i -= 1
            out.appendleft(over % 10)
            over //= 10
        return list(out)

    def plusOneCheat(self, digits: list[int]) -> list[int]:
        new_int = str(int("".join(map(str, digits)), 10) + 1)
        return [int(c) for c in new_int]


if __name__ == "__main__":
    s = Solution()
    a = [1, 2, 3]
    assert s.plusOneCheat(a) == s.plusOneFast(a)
