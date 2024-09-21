"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        end = 0
        while i >= 0:
            if not end:
                if s[i] != " ":
                    end = i
            else:
                if s[i] == " ":
                    print("ret via in")
                    return end - i
            i -= 1
        print("ret via end", end, i, len(s))
        return end - i

    def lengthOfLastWordProd(self, s: str) -> int:
        return len(s.split()[-1])


if __name__ == "__main__":
    tests = {
        # " W": 1,
        # "Hello World": 5,
        # "   fly me   to   the moon  ": 4,
        # "luffy is still joyboy": 6,
        "loki": 4,
        " loki": 4,
        "  loki": 4,
    }
    s = Solution()
    for test, value in tests.items():
        print(s.lengthOfLastWord(test), value, test)

    for test, value in tests.items():
        assert s.lengthOfLastWordProd(test) == value
        # assert s.lengthOfLastWord(test) == value
