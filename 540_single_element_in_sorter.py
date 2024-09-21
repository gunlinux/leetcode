# Your solution must run in O(log n) time and O(1) space.
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            check = nums[mid]
            t = nums[mid-1]

            #  границы
            if mid - 1 < 0 and check != nums[mid +1 ]:
                print('left')
                return check
            if mid + 1 == len(nums) and check != nums[mid -1 ]:
                print('right')
                return check

            if check != nums[mid - 1] and check != nums[mid + 1]:
                print('in mid')
                return nums[mid]

            if check == nums[mid - 1]:
                if mid % 2 :
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if mid % 2 :
                    right = mid - 1
                else:
                    left = mid + 1
        return 0


if __name__ == "__main__":
    s = Solution()
    assert s.singleNonDuplicate([1,1,2,2,3]) == 3
    assert s.singleNonDuplicate([1, 1, 2]) == 2
    assert s.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2
    assert s.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]) == 10
