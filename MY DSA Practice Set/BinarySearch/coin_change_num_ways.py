'''
Problem Description

You are given a set of coins A. In how many ways can you make sum B assuming you have infinite amount of each coin in the set.

NOTE:

Coins in set A will be unique. Expected space complexity of this problem is O(B).
The answer can overflow. So, return the answer % (106 + 7).
'''

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def coinchange2(self, A, B):
        MOD = 10**6 + 7
        dp = [0] * (B + 1)
        dp[0] = 1  # 1 way to make sum 0

        for coin in A:
            for amount in range(coin, B + 1):
                dp[amount] = (dp[amount] + dp[amount - coin]) % MOD

        return dp[B]