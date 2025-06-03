'''
🎯 Problem 1: Standard Binary Search
Problem:
Given a sorted array A of integers and an integer B, find the index of B in A.
If B is not present, return -1.
(Assume no duplicates for now.)

Example:
Input: A = [1, 3, 5, 7, 9, 11], B = 5
Output: 2

Input: A = [1, 3, 5, 7, 9, 11], B = 6
Output: -1
'''

def find_index(A, B):
    left, right = 0, len(A) -1
    while left <= right:
        mid = left + (right - left)//2
        if A[mid] == B:
            return mid
        elif(A[mid] < B):
            left = mid + 1
        else:
            right = mid - 1
    return -1

A, B = [1, 3, 5, 7, 9, 11], 5
print(find_index(A, B))

'''
✅ Time complexity: O(log N)

✅ Space complexity: O(1)


'''