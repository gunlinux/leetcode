"""
Given an integer array nums and an integer k, 
return the k most frequent elements. You may return the answer in any order.
Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        stats = defaultdict(int)
        for el in nums:
            stats[el] = stats[el] + 1
        sorted_dict = sorted(stats, key = stats.get, reverse = True)
        return sorted_dict[:k]


if __name__ == "__main__":
    s = Solution()
    assert s.topKFrequent([9, 9, 9, 2, 2, 3], 2) == [9, 2]
    assert s.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert s.topKFrequent([1], 1) == [1]
