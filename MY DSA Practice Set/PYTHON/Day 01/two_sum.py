'''
🔥 Problem 1: Two Sum
Difficulty: Easy
Topic: Arrays, HashMap

Question:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9  
Output: [0,1] // Because nums[0] + nums[1] == 2 + 7 == 9
'''
# Brute Force Approach
def two_sum(nums, target):
    n = len(nums)
    for num1 in range(n):
        for num2 in range(num1, n):
            if nums[num1] + nums[num2] == target:
                return [num1, num2]
    return []
nums,target = [2,7,11,15],9
print(two_sum(nums, target))

# Optimal Approach
def two_sum(nums, target):
    num_set = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_set:
            return [num_set[complement],i]
        num_set[num] = i
nums,target = [2,7,11,15],9
print(two_sum(nums, target))