'''
Find the Peak Element in an Array

An element is called a peak if it is strictly greater than its neighbors.
Given an input array A, find and return a peak element.
If there are multiple peaks, return any of them.
(You can assume the array is non-empty.)

Example:
Input: A = [1, 3, 20, 4, 1, 0]
Output: 20 (peak at index 2)

Input: A = [1, 2, 3, 1]
Output: 3 (peak at index 2)
'''
'''
Idea:
To find the peak element we need to iterate first half element and compare it if that elment is grate than it's left element
or not if Yes then it will be obvious that the first half others element will be smaller than mid value so we need to check right half if 
'''
# Brute Force Approach
# Brute Force Approach
def find_peak_element(A):
    n = len(A)
    
    # If List is Empty
    if n == 0:
        return -1  # No peak
    
    # If there is only one element in the list 
    if n == 1:
        return 0
    
    # If there are only two elements
    if n == 2:
        return 0 if A[0] > A[1] else 1
    
    # Check the first element
    if A[0] > A[1]:
        return 0

    # Check the middle elements
    for i in range(1, n - 1):
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            return i
    
    # Check the last element
    if A[n - 1] > A[n - 2]:
        return n - 1

    return -1  # fallback, though problem guarantees at least one peak

# Test
A = [1, 3, 20, 4, 1, 0]
print(find_peak_element(A))  # Output should be 2 (20 is a peak)


# Optimal Approach
def find_peak_element(A):
    left, right = 0, len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] > A[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return A[left]
A = [1, 3, 20, 4, 1, 0]
print(find_peak_element(A))

# Optimal Approach
def find_peak_element(nums):
    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        return 0
    start, end = 0, len(nums) - 1
    while start < end:
        mid = (start+end)//2
        if nums[mid] > nums[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return start
            
nums = [1, 3, 20, 4, 1, 0]
print(find_peak_element(nums))
