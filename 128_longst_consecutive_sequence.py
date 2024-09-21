"""
"""

from typing import List


class SolutionBad:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        rez = [1] * len(nums)
        nums = sorted(nums)
        print(nums)
        j = 0
        """
        [0,1,2,3,10,11]
        [1,1,1,3,1,2]
        [1,3,1,1,2,1]
        [1,3,3,3,2,2]
        """
        for i, el in enumerate(nums[:-1]):
            if j:
                if nums[i + 1] == nums[i] + 1:
                    j += 1
                    rez[i] = j
                elif nums[i + 1] != nums[i]:
                    j += 1
                    rez[i] = j
                    j = 0
            else:
                if nums[i + 1] == nums[i] + 1:
                    j += 1
        print(rez, max(rez))
        rez[i + 1] = j + 1
        return max(rez)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_l: int = 0
        temp_nums = set(nums)
        for el in temp_nums:
            if (el - 1) not in temp_nums:
                length = 1
                while (el + length) in temp_nums:
                    length += 1
                max_l = max(length, max_l)
        return max_l


if __name__ == "__main__":
    s = Solution()
    nums = [0, 1, 2, 3, 10, 11]
    assert s.longestConsecutive(nums) == 4
    nums = [100, 4, 200, 1, 3, 2]
    assert s.longestConsecutive(nums) == 4
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    assert s.longestConsecutive(nums) == 9
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    assert s.longestConsecutive(nums) == 9
