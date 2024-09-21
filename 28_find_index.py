"""
28. Find the Index of the First Occurrence in a String
Easy
Topics
Companies

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

 

Constraints:

    1 <= haystack.length, needle.length <= 104
    haystack and needle consist of only lowercase English characters.


"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[0]:
                for j in range(len(needle)):
                    print(needle[j], haystack[i+j])
                    if needle[j] != haystack[i+j]:
                        print(needle[j])
                        break
                else:
                    return i
            i += 1
        return -1 


if __name__ == "__main__":
    s = Solution()
    print(s.strStr("nuffsadlosaldosasad", "sad"))
    print(s.strStr("sadfsadlosaldosasad", "sad"))
    print(s.strStr("xsadfsadlosaldosasad", "sad"))
    print(s.strStr("mississippi", "issipi"))
    print(s.strStr("leetcode", "leeto"))
