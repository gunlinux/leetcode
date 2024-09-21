"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        parents = {"(": ")", "[": "]", "{": "}"}
        for c in s:
            if c in parents:
                stack.append(c)
            if c in parents.values():
                if not stack or parents.get(stack.pop()) != c:
                    return False
        return not stack


if __name__ == "__main__":
    a = Solution()
    assert a.isValid("()")
    assert a.isValid("lc(loki)l")
    assert a.isValid("()[]{loki}")
    assert a.isValid("([]{loki})")
    assert a.isValid("")
    assert not a.isValid("lcloki)l")
    assert not a.isValid("()[{loki}")
    assert not a.isValid("[]{loki})")
