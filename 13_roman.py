"""
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        symbols: dict[str, int] = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        summ: int = 0
        prev: int = 4000

        for c in s:
            cur_val = symbols.get(c, 0)
            # print(f'prev: {prev} cur { cur_val}', end='')
            if cur_val <= prev:
                summ += cur_val  #  // добавляем число
                prev = cur_val  # // запоминаем
            else:
                summ -= prev  #  // убираем число предыдущее т.к. оно относится к текущему
                summ += (cur_val - prev) #  // прибавляем текущее числоb
                prev = 4000      #// обнуляем прев
        print('sum:', summ)
        return summ



if __name__ == "__main__":
    tests = {
        "VIII": 8,
        "IX": 9,
        # Explanation: L = 50, V= 5, III = 3.
        "LVIII": 58,
        # M = 1000, CM = 900, XC = 90 and IV = 4.
        "MCMXCIV": 1994,
    }
    s = Solution()
    for test, value in tests.items():
        print(s.romanToInt(test) == value, test, value)
