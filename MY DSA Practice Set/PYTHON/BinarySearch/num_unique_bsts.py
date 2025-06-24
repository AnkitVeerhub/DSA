'''
Problem 4: Count Unique BSTs
Company: Google
Filename: count_unique_bsts.py
Topic: Binary Search, Dynamic Programming
Time Complexity (Optimal): O(n²)
Space Complexity: O(n)
Problem Description

Given an integer A, how many structurally unique BST's (binary search trees) exist that can store values 1...A?
'''
class Solution:
    def numTrees(A):
        dp = [0] * (A+1)
        dp[0], dp[1] = 1, 1
        for n in range(2, A+1):
            for i in range(1, n + 1):
                dp[n] += dp[i - 1] * dp[n - i]
        return dp[A]
A = 3
print(Solution.numTrees(A))
