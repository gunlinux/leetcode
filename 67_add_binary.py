"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinaryFast(self, a: str, b: str) -> str:
        f = self.addBinary(a, b)
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        sum_ = []
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            sum_.append(str(carry % 2))
            carry = carry // 2
        return "".join(reversed(sum_))


if __name__ == "__main__":
    s = Solution()
    # print(s.addBinaryFast("10", "1"))
    print(s.addBinaryFast("1", "1"))
    exit()
    print(s.addBinary("1", "1"))
    print(s.addBinary("1", "11"))
    print(100)
    print(s.addBinary("1", "10"))
    print(s.addBinaryFast("1", "10"))
    print(10000)
    print(s.addBinary("101", "1011"))
    print(s.addBinaryFast("101", "1011"))

    assert s.addBinary("1", "11") == s.addBinaryFast("1", "11")
