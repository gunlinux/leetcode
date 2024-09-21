"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.


"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        k = 0
        for i in range(min(map(len, strs))):
            temp = [c[i] for c in strs]
            if not all(e == temp[0] for e in temp):
                return strs[0][:i]
            k += 1
        rez = strs[0][:k] if k >= 1 else ''
        return rez


if __name__ == "__main__":
    solution = Solution()
    assert solution.longestCommonPrefix(strs=["a"]) == 'a'
    assert solution.longestCommonPrefix(strs=["ab"]) == 'ab'
    assert solution.longestCommonPrefix(strs=["ab", "a"]) == 'a'
    assert solution.longestCommonPrefix(strs=["dog", "racecar", "car"]) == ''
    assert solution.longestCommonPrefix(strs=["flower", "flow", "flight"]) == 'fl'
