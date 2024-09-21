class Solution:
    def mySqrt(self, x: int) -> int:
        ret = left = 0
        right = x
        while (left <= right):
            mid = left + (right - left) // 2
            temp = mid**2
            if temp == x:
                return mid
            if temp < x:
                ret = mid
                left = mid + 1
            else:
                right = mid - 1
        return ret

    def mySqrtBad(self, x: int) -> int:
        temp = []
        for i in range(0, x // 2 + 1):
            tempn = i**2
            if tempn == x:
                print("x: ", x, i)
                return i
            temp.append(tempn)
            if tempn >= x:
                break
        for i in range(len(temp) - 1, 0, -1):
            if temp[i] < x:
                return i
        return 1

    def mySqrtProd(self, x: int) -> int:
        return int(x**0.5)


if __name__ == "__main__":
    tests = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 2),
        (5, 2),
        (6, 2),
        (7, 2),
        (8, 2),
        (9, 3),
        (10, 3),
        (11, 3),
        (12, 3),
        (13, 3),
        (14, 3),
        (15, 3),
        (16, 4),
        (17, 4),
        (18, 4),
        (19, 4),
        (20, 4),
        (21, 4),
        (22, 4),
        (23, 4),
        (24, 4),
        (25, 5),
    ]
    s = Solution()
    for q, a in tests:
        print(q, a)
        assert s.mySqrt(q) == a
