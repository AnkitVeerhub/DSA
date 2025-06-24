'''
410. Split Array Largest Sum
Hard
Topics
Greedy, Binary Seach on Answer
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.
Return the minimized largest sum of the split.
A subarray is a contiguous part of the array.
Example 1:

Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
'''

# Brute Force Approach
def split_array_bruteforce(nums, k):
    # Imports lru_cache for memoization — it helps avoid recalculating overlapping subproblems in recursion.
    from functools import lru_cache

    n = len(nums)

    # Precompute prefix sums for quick subarray sum lookup
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    # Get sum from i to j
    def get_sum(i, j):
        return prefix[j + 1] - prefix[i]

    @lru_cache(None)
    def dfs(start, k):
        # Base case: 1 partition left, take the rest
        if k == 1:
            return get_sum(start, n - 1)

        min_largest = float('inf')
        # Try all possible partition points
        for end in range(start, n - k + 1):
            left_sum = get_sum(start, end)
            right = dfs(end + 1, k - 1)
            largest = max(left_sum, right)
            min_largest = min(min_largest, largest)

        return min_largest

    return dfs(0, k)

nums = [7, 2, 5, 10, 8]
k = 2
print(split_array_bruteforce(nums, k))
# You will get TLE error for the bruteforce approach solution

# Optimal Approach
def splitArray(nums: list[int], k: int) -> int:
    def can_split(max_sum):
        count, total = 1, 0
        for num in nums:
            if total + num > max_sum:
                count += 1
                total = num
            else:
                total += num
        return count <= k
    low, high = max(nums), sum(nums)
    answer = high
    while low <= high:
        mid = (low + high)//2
        if can_split(mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    return answer

# Define the input
nums = [7, -2, 5, 10, 8]
k = len(nums)

# Call the method
print(splitArray(nums, k))











