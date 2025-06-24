'''
Problem 2:
Find the first occurrence of a target element in a sorted array (with possible duplicates).

Given a sorted array A (may contain duplicates) and a number B,
find the index of the first occurrence of B in A.
If B is not present, return -1.

Example:
Input: A = [2, 4, 4, 4, 6, 8, 10], B = 4
Output: 1 (first occurrence at index 1)

Input: A = [1, 1, 1, 1, 1], B = 1
Output: 0

Input: A = [1, 2, 3, 5, 6], B = 4
Output: -1
'''
def find_first_occurrence(A, B):
    first_occurence, left, right = -1, 0, len(A) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if A[mid] == B:
            first_occurence = mid
            right = mid - 1
        elif A[mid] < B:
            left = mid + 1
        else:
            right = mid - 1
    return first_occurence
A, B = [1, 1, 1, 1, 1], 1
print(find_first_occurrence(A,B))
'''
✅ Time complexity: O(log N)

✅ Space complexity: O(1)
'''