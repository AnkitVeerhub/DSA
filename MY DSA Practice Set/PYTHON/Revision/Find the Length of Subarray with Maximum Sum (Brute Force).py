'''
📄 Problem: Find the Length of Subarray with Maximum Sum (Brute Force)
Difficulty: Easy-Medium
Category: Arrays, Subarrays, Brute Force

📝 Problem Statement:
Given an array of integers nums, find the length of the subarray which has the maximum sum among all possible subarrays.
Return the length of such a subarray. If there are multiple subarrays with the same maximum sum, return the length of the first one found.
'''
# Bruteforce Approach
def maximum_subarray_sum_length(nums):
    n = len(nums)
    max_length = 0
    max_sum = float('-inf')
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            # Calculating Current Subarray Sum 
            current_sum += nums[j]
            if current_sum > max_sum:
                max_sum = current_sum
                max_length = j - i + 1
    return max_length
print(maximum_subarray_sum_length(nums = [-2,1,-3,4,-1,2,1,-5,4]))