'''
🧠 Platform: LeetCode
💼 Commonly Asked In: Amazon, Google, Microsoft
📂 Topic: Hashing / Arrays
🎯 Difficulty: Medium
🗣️ Interviewer Prompt:
“Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.”

Problem: Two Sum
Function Signature:
def two_sum(nums: List[int], target: int) -> List[int]:
Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, return [0, 1].
'''
# Brute force Approach
'''
🕒 Time Complexity: O(n²)
Two nested loops:

Outer loop runs n times.

Inner loop runs up to n times in the worst case.

So total comparisons ≈ n * n → O(n²).

🧠 Space Complexity: O(1)
You're not using any extra data structures (no arrays, sets, or hash maps).

Just variables like i, j, and return indices → constant space.
'''
def two_sum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if target == nums[i] + nums[j]:
                return [i,j]
    return []
nums, target = [2, 7, 11, 15], 9
print(two_sum(nums, target))

# Optimal Approach:
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for index, num in enumerate(nums):
        complement = target - num 
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index
nums, target = [2, 7, 11, 15], 9
print(two_sum(nums, target))