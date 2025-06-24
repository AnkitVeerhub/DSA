'''
Problem: LeetCode #121 - Best Time to Buy and Sell Stock

Given an array prices where prices[i] is the price of a stock on the ith day,
find the maximum profit you can achieve from one transaction (i.e., buy once and sell once).
Example:
Input: [7,1,5,3,6,4]
Output: 5  # (Buy at 1, Sell at 6)
'''
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price # Buy Here
            else:
                profit = price - min_price # Sell Here
                max_profit = max(max_profit, profit)
        return max_profit

sol = Solution()
print(sol.maxProfit(prices=[7,1,5,3,6,4]))
