'''
Given an array of integers A, find and return the peak element in it.
An array element is considered a peak if it is not smaller than its
neighbors. For corner elements, we need to consider only one neighbor.
Input 1:
A = [1, 2, 3, 4, 5]
Output 1:
5
Input 2:
A = [5, 101, 100, 11]
Output 2:
 100
'''

# Idea 1:
# condition: 100 > 17 and 100 > 11
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