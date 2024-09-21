"""
A phrase is a palindrome if, after converting all uppercase letters
into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric
characters.
Since an empty string reads the same forward and backward, it is a palindrome.



Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.


"""

import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        clear_str = ''.join(filter(self.letter, s)).lower()
        for i in range(len(clear_str)//2):
            if clear_str[i] != clear_str[-i-1]:
                return False
        return True

    def letter(self, c: str) -> bool:
        return c in string.ascii_letters or c in string.digits


def main() -> None:
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    print(solution.isPalindrome('0P'), '0P')
    assert solution.isPalindrome(s)
    assert solution.isPalindrome(' ')
    assert not solution.isPalindrome('race a car')
    assert solution.isPalindrome('0A man, a plan, a canal: Panama0')


if __name__ == "__main__":
    main()
