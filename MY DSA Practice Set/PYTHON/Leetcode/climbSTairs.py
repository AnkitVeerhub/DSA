'''
✅ Problem 70: Climbing Stairs
🔗 LeetCode 70 – Climbing Stairs
Category: Dynamic Programming
Difficulty: Easy
Interview Frequency: ⭐⭐⭐⭐ (Google, Meta, Amazon)
🧠 For Interviews:
You can also mention:

“This is a classic Fibonacci-style problem”

“We optimize space by storing only the last two states”

“This gives us O(n) time and O(1) space complexity”
'''
def climb_Stairs(n):
    if n <= 2:
        return n
    ways1, ways2 = 1, 2
    for ways in range(3, n + 1):
        ways1, ways2 = ways2, ways1 + ways2
    return ways2
print(climb_Stairs(n=4))

# DP Approach
def climb_Stairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
print(climb_Stairs(n=6))
