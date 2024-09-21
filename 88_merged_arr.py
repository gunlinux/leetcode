from typing import Optional


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> list:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        out_i = m + n - 1
        left_i = m - 1
        right_i = n - 1

        while out_i >= 0 and left_i >= 0 and right_i >= 0:
            if nums1[left_i] >= nums2[right_i]:
                nums1[out_i] = nums1[left_i]
                nums1[left_i] = 0
                left_i -= 1
            elif nums2[right_i] >= nums1[left_i]:
                nums1[out_i] = nums2[right_i]
                right_i -= 1
            out_i -= 1
        while out_i >= 0 and right_i >= 0:
            if nums2[right_i] > nums1[out_i] or nums1[out_i] == 0:
                nums1[out_i] = nums2[right_i]
            out_i -= 1
            right_i -= 1
        print(nums1)
        return nums1


if __name__ == "__main__":
    a = [0]
    s = Solution()
    assert [1] == s.merge(a, 0, [1], n=1)
    a = [0, 0]
    assert [1, 2] == s.merge(a, 0, [1, 2], n=2)

    a = [1, 2, 3, 0, 0, 0]
    assert [1, 2, 2, 3, 5, 6] == s.merge(a, 3, [2, 5, 6], n=3)

    a = [2, 0]
    assert [1, 2] == s.merge(a, 1, [1], n=1)

    a = [4, 5, 6, 0, 0, 0]

    assert [1, 2, 3, 4, 5, 6] == s.merge(a, 3, [1, 2, 3], n=3)

    a = [0, 0, 3, 0, 0, 0, 0, 0, 0]
    k = [-1, 0, 0, 1, 1, 1, 2, 3, 3] == s.merge(a, 3, [-1, 1, 1, 1, 2, 3], n=6)
    print(k)
