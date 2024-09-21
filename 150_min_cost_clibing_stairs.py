"""
You are given an array of integers cost where cost[i] is the
cost of taking a step from the ith floor of a staircase.
After paying the cost, you can step
    to either the (i + 1)th floor or the (i + 2)th floor.

You may choose to start at the index 0 or the index 1 floor.

Return the minimum cost to reach the top of the staircase, i.e. just past the last index in cost.
"""
'''
kurwa

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])

'''

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        start = 0
        pos = -1
        price = 0
        while pos < len(cost) - 2:
            cost_one_step = cost[pos + 1]
            cost_two_step = cost[pos + 2]
            #  count extra one
            extra_one = cost[pos + 2] if (pos + 2 < len(cost)) else 0
            extra_two = cost[pos + 3] if (pos + 3 < len(cost)) else 0
            extra2_one = cost[pos + 3] if (pos + 3 < len(cost)) else 0
            extra2_two = cost[pos + 4] if (pos + 4 < len(cost)) else 0

            if cost_one_step + min(extra_one, extra_two) < cost_two_step + min(extra2_one, extra2_two):
                print(f'step one, next pos {pos + 1} {cost_one_step}')
                price += cost_one_step
                pos += 1
            else:
                print(f'step two, next pos {pos + 2} {cost_two_step}')
                price += cost_two_step
                pos += 2
        print(f'price = {price}')
        return price


if __name__ == "__main__":
    s = Solution()
    assert s.minCostClimbingStairs([1, 0, 2, 2]) == 2 
    assert s.minCostClimbingStairs([1, 2, 3]) == 2
    assert s.minCostClimbingStairs([1, 2, 1, 2, 1, 1, 1]) == 4
    assert s.minCostClimbingStairs([1,3,5,15,2]) == 8
