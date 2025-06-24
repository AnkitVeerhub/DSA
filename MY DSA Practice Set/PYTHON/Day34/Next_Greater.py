'''
Problem Description

Given an array A, find the next greater element G[i] for every element A[i] in the array.
The next greater element for an element A[i] is the first greater element on the right side of A[i] in the array, A.


More formally:

G[i] for an element A[i] = an element A[j] such that 
    j is minimum possible AND 
    j > i AND
    A[j] > A[i]
Elements for which no greater element exists, consider the next greater element as -1.

Example Input

Input 1:

 A = [4, 5, 2, 10] 
Input 2:

 A = [3, 2, 1] 



Example Output

Output 1:

 [5, 10, 10, -1] 
Output 2:

 [-1, -1, -1] 


Example Explanation

Explanation 1:

For 4, the next greater element towards its right is 5.
For 5 and 2, the next greater element towards their right is 10.
For 10, there is no next greater element towards its right.
Explanation 2:

As the array is in descending order, there is no next greater element for all the elements.
'''

# Optimal Approach
def nextGreater(A):
    n = len(A)
    result = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):  # Traverse from right to left
        while stack and stack[-1] <= A[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(A[i])

    return result

A = [4, 5, 2, 10] 
print(nextGreater(A))

'''
Leetcode problem:
Given two arrays nums1 and nums2, where nums1 is a subset of nums2,
find the next greater element for each element in nums1 from nums2.

Input:
nums1 = [4,1,2]
nums2 = [1,3,4,2]

Output:
[-1, 3, -1]

Explanation:
- 4 → no greater element to the right of 4 in nums2 → -1
- 1 → next greater is 3
- 2 → no greater → -1

'''
'''
🏢 Companies That Asked This Problem
Company Name	Frequency
Amazon	⭐⭐⭐⭐
Google	⭐⭐⭐
Adobe	⭐⭐⭐
Microsoft	⭐⭐
Samsung	⭐⭐
Cisco	⭐
Flipkart
'''
# Bruteforce Approach
def next_greater_element(nums1, nums2):
    result = []
    for num in nums1:
        found = False
        next_greater = -1
        for i in range(len(nums2)):
            if nums2[i] == num:
                found = True
            if found and nums2[i] > num:
                next_greater = nums2[i]
                break
        result.append(next_greater)
    return result

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(next_greater_element(nums1, nums2))

# Optimal Approach
def next_greater_ele(nums1, nums2):
    next_greater_map = {}
    stack = []
    for num in nums2:
        while stack and num > stack[-1]:
            smaller = stack.pop()
            next_greater_map[smaller] = num
        stack.append(num)
    for num in stack:
        next_greater_map[num] = -1
    return [next_greater_map[num] for num in nums1]
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(next_greater_ele(nums1, nums2))