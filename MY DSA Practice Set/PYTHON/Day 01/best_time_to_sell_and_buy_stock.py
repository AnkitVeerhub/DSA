'''
🔥 Problem 2: Best Time to Buy and Sell Stock
Difficulty: Easy
Topic: Arrays, Sliding Window

Question:
You are given an array prices where prices[i] is the price of a given stock on the i-th day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Example:
Input: prices = [7,1,5,3,6,4]  
Output: 5  
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
'''
def stock_profit(stock_prices):
    max_profit = 0
    n = len(stock_prices)
    for buy_day in range(n):
        for sell_day in range(buy_day+1, n):
            profit = stock_prices[sell_day] - stock_prices[buy_day]
            max_profit = max(max_profit, profit)
    return max_profit
print(f"Your Maximum Profit is:",stock_profit(stock_prices=[0,2,5,9,7]))
# Bruteforce Approach
def calculate_max_profit_bruteforce(stock_prices):
    max_possible_profit = 0
    total_days = len(stock_prices)

    for buy_day in range(total_days):
        for sell_day in range(buy_day + 1, total_days):
            profit_today = stock_prices[sell_day] - stock_prices[buy_day]
            max_possible_profit = max(max_possible_profit, profit_today)

    return max_possible_profit

stock_prices = [7,1,5,3,6,4]
print(calculate_max_profit_bruteforce(stock_prices))

# Time Complexity: O(N^2)
# Space Complexity: O(1)

# Optimal Approach
def calculate_max_profit(stock_prices):
    min_price_seen = float('inf')
    max_possible_profit = 0

    for current_price in stock_prices:
        min_price_seen = min(min_price_seen, current_price)
        potential_profit = current_price - min_price_seen
        max_possible_profit = max(max_possible_profit, potential_profit)

    return max_possible_profit

stock_prices = [7,1,5,3,6,4]
print(calculate_max_profit(stock_prices))


# Time Complexity: O(N)
# Space Complexity: O(1)


# Brute Force Approach
def calculate_max_profit_bruteforce(prices):
    n = len(prices)
    max_profit = 0
    for buy_day in range(n):
        for sell_day in range(buy_day+1, n):
            profit_today = prices[sell_day] - prices[buy_day]
            max_profit = max(max_profit, profit_today)
    return max_profit
print(f"Your Profit is:", calculate_max_profit_bruteforce(prices=[7,1,5,3,6,4]))
# Time Complexity: O(N^2)
# Space Complexity: O(1)

# Optimal Approach
def calculate_max_profit_optimal(stock_prices):
    min_price = float('inf')
    max_possible_profit = 0
    for current_price in stock_prices:
        min_price = min(min_price, current_price)
        profit = current_price - min_price
        max_possible_profit = max(max_possible_profit, profit)
    return max_possible_profit
print(f"Your Profit is:",calculate_max_profit_optimal(stock_prices=[7,1,5,3,6,4]))
# Time Complexity: O(N)
# Space Complexity: O(1)


def stock_profit(stock_prices):
    min_price = float('inf')
    max_profit = 0
    for price in stock_prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit
print(f"Your Maximum Profit is:",stock_profit(stock_prices=[0,2,5,9,7]))

