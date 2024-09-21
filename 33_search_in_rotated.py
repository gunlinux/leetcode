"""
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        print(target, nums)
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            #  left sorted
            #  nums = [4,5, 6, [7], 0, 1, 2]
            if nums[left] < nums[mid]:
                if nums[left] > target:
                    #  Числе только в правой части может быть
                    left = mid + 1
                else:
                    if target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
            else:
                if nums[right] < target:
                    # число только в левой может быть
                    right = mid - 1
                else:
                    if target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
        return -1


if __name__ == "__main__":
    s = Solution()
    nums = [1, 3]
    assert s.search(nums, 3) == 1
    nums = [3, 1]
    assert s.search(nums, 1) == 1
    nums = [4, 5, 6, 7, 0, 1, 2]
    assert s.search(nums, 0) == 4
    nums = [4, 5, 6, 7, 0, 1, 2]
    assert s.search(nums, 3) == -1
    nums = [1]
    assert s.search(nums, 0) == -1
