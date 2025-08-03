'''
✅ Problem Name: Maximum Subarray Sum
(Also known as Kadane’s Algorithm)
📌 LeetCode: 53. Maximum Subarray

🔍 Problem Statement (Simplified)
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum and return its sum.

A = [1,2,3,4] , output: 10
'''
'''
| Company       | Asked In Interview |
| ------------- | ------------------ |
| Amazon        | ⭐⭐⭐⭐         |
| Google        | ⭐⭐⭐            |
| Microsoft     | ⭐⭐⭐            |
| Facebook      | ⭐⭐⭐            |
| Adobe         | ⭐⭐              |
| Goldman Sachs | ⭐⭐              |

'''
# Brute force Approach
# Time Complexity : O(N^2)
def max_subarray_sum_brute(A):
    n = len(A)
    max_sum = float('-inf')
    for i in range(n):
        for j in range(i, n):
            curr_sum = 0
            for k in range(i, j + 1):
                curr_sum += A[k]
            max_sum = max(max_sum, curr_sum) 
    return max_sum
# Test
print(max_subarray_sum_brute([2,1,5,1,3,2]))  # Output: 10

# Optimal Approach
# Time Complexity: O(N)

def max_subarray_sum_kadane(A):
    current_sum = 0
    max_sum = float('-inf')
    
    for num in A:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        
        if current_sum < 0:
            current_sum = 0
    return max_sum

# Test
print(max_subarray_sum_kadane([1,2,3,4]))  # Output: 6