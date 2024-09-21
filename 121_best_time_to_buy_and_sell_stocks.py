"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

from typing import List


class SolutionN2:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if prices[j] - prices[i] > profit:
                    profit = prices[j] - prices[i]
        return profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        m = prices[0]
        for i in range(1, len(prices)):
            if m > prices[i]:
                m = prices[i]
            if profit < prices[i] - m:
                profit = prices[i] - m
        return profit


if __name__ == "__main__":
    s = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    assert s.maxProfit(prices) == 5

    prices = [7, 6, 4, 3, 1]
    assert s.maxProfit(prices) == 0
