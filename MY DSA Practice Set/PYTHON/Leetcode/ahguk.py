from typing import List

class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        n = len(numWays)
        dp = [0] * (n + 1)
        dp[0] = 1  # base case: one way to make amount 0
        result = []

        for coin in range(1, n + 1):
            new_dp = dp[:]  # clone current dp state

            # Simulate adding coin to dp table
            for i in range(coin, n + 1):
                new_dp[i] += dp[i - coin]

            # Check if new_dp[i] ever exceeds numWays[i-1]
            exceeds = any(new_dp[i] > numWays[i - 1] for i in range(1, n + 1))
            if not exceeds:
                result.append(coin)
                dp = new_dp  # accept this coin

        # Final validation: does dp match numWays exactly?
        for i in range(1, n + 1):
            if dp[i] != numWays[i - 1]:
                return []

        return result
sol = Solution()
print(sol.findCoins([0,1,0,2,0,3,0,4,0,5]))
