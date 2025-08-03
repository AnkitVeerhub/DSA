'''
🔥 Problem 3: Maximum Subarray (Kadane’s Algorithm)
Difficulty: Easy-Medium
Topic: Arrays, DP / Sliding Window
Question:
Given an integer array nums, find the subarray with the largest sum and return its sum.
Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]  
Output: 6  
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

# Bruteforce Approach
def maximum_subarray_sum(nums):
    n = len(nums)
    max_sum = float('-inf')
    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += nums[end]
            max_sum = max(max_sum, current_sum)
    return max_sum
print(maximum_subarray_sum(nums = [2,1,5,1,3,2]))

# Time Complexity: O(N^2)
# Space Complexity: O(1)

# Optimal Approach
def maximum_subarray_sum(nums):
    max_sum = float('-inf')
    current_sum = 0
    for num in nums:
        current_sum += num
        max_sum = max(max_sum,current_sum)
        if current_sum < 0:
            current_sum = 0
    return max_sum
print(maximum_subarray_sum(nums = [-2,1,-3,4,-1,2,1,-5,4]))
# Time Complexity: O(N)
# Space Complexity: O(1)


def best_time_to_buy_and_sell_stock_with_days(prices):
    if not prices:
        return 0, -1, -1  # No profit, invalid days

    min_price = float('inf')
    max_profit = 0
    buy_day = sell_day = 0
    temp_buy_day = 0

    for current_day, price in enumerate(prices):
        if price < min_price:
            min_price = price
            temp_buy_day = current_day  # potential new buy day

        profit_today = price - min_price
        if profit_today > max_profit:
            max_profit = profit_today
            buy_day = temp_buy_day
            sell_day = current_day

    return max_profit, buy_day, sell_day

# Test
prices = [1, 7, 2, 1, 5]
profit, buy, sell = best_time_to_buy_and_sell_stock_with_days(prices)
print(f"Max Profit: {profit}, Buy Day: {buy}, Sell Day: {sell}")
