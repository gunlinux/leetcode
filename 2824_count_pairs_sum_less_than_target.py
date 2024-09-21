from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        rez = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < target:
                    # print(i, j,  nums[i], nums[j])
                    rez += 1
        return rez

class Solution2:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        left = 0

        # Шаг 2: Итерируем по массиву
        for i in range(len(nums)):
            j = i + 1
            # Шаг 3: Используем бинарный поиск
            while j < len(nums) and nums[i] + nums[j] < target:
                j += 1
            count += (j - (i + 1))  # Все элементы от (i+1) до (j-1) подходят

        return count

    def fmin(self, nums, target, check, num, i):
        left = i
        




if __name__ == '__main__':
    '''
    Given a 0-indexed integer array nums of
    length n and an integer target,
    return the number of pairs (i, j)
    where 0 <= i < j < n and nums[i] + nums[j] < target.
    '''
    s = Solution2()
    assert s.countPairs([-1,1,2,3,1], target=2) == 3 
    assert s.countPairs([-6,2,5,-2,-7,-1,3], target=-2) == 10







