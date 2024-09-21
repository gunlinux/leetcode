"""
"""

from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        out = []
        if not strs:
            return ''
        for s in strs:
            for c in s:
                out.append(chr(ord(c) + 1))
            out.append('\01')
        return ''.join(out)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        pre = s.split('\01')[:-1]
        out = []
        print(f'f{pre}')
        for s in pre:
            temp = []
            for c in s:
                temp.append(chr(ord(c) - 1))
            out.append(''.join(temp))
        return out


if __name__ == "__main__":
    s = Solution()
    a = ["neet", "code", "love", "you"]
    b = ["we", "say", ":", "yes"]
    print(s.encode(a))
    print(s.decode(s.encode(a)))
    assert s.decode(s.encode(a)) == a
    assert s.decode(s.encode(b)) == b

    big = ["","   ","!@#$%^&*()_+","LongStringWithNoSpaces","Another, String With, Commas"]
    assert s.decode(s.encode(big)) == big
