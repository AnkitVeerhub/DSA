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