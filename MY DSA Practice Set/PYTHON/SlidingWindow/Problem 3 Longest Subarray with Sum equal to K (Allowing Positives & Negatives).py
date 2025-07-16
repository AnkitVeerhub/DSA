'''
🚀 Problem 3: Longest Subarray with Sum = K (Allowing Positives & Negatives)
Problem Statement:
Given an array of integers and an integer k, return the length of the longest subarray whose sum equals k. Elements can include positive, negative, and zero.
Example:
Input:
arr = [1, -1, 5, -2, 3]
k = 3
Explanation:
The subarray [1, -1, 5, -2] sums to 3.
1 + (-1) + 5 + (-2) = 3
Length = 4
Output:
4
Another Example:
Input:
arr = [-2, -1, 2, 1]
k = 1
Explanation:
Subarray [-1, 2] sums to 1.
Another subarray [1] also sums to 1.
The longest subarray is [-1, 2], length 2.
Output:
2
'''
# Brute Force Approach
def Longest_Subarray(arr, k):
    n = len(arr)
    longest = 0
    if n == 0:
        return 0
    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += arr[end]
            if current_sum == k:
                longest = max(longest, end - start + 1)
    return longest
arr = [1, -1, 5, -2, 3]
k = 3
print(Longest_Subarray(arr, k))
# Optimal Approach
def Longest_Subarray(arr, k):
    prefix_sum = 0
    max_len = 0
    prefix_map = {}
    for i in range(len(arr)):
        prefix_sum += arr[i]
        if prefix_sum == k:
            max_len = i + 1
        if (prefix_sum - k) in prefix_map:
            max_len = max(max_len, i - prefix_map[prefix_sum - k])
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i
    return max_len
arr = [1, -1, 5, -2, 3]
k = 3
print(Longest_Subarray(arr, k))