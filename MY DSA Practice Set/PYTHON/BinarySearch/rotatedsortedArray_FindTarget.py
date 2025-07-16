'''
Given a sorted array of integer A of size N and an integer B,
Where array A is rotated at some certain pivot unknown beforehand
for example : the array [0,1,2,3,4,5,6,7] might become [4,5,6,7,0,1,2].

your task is to search for the target value B in the array.
If found, return it's index; otherwise return -1.

You can assume that no duplicates exist in the array.

Example Input
Input 1:

A = [4, 5, 6, 7, 0, 1, 2, 3]
B = 4 
Input 2:
A : [9, 10, 3, 5, 6, 8 ]
B : 5

Example Output
Output 1:
 0 
Output 2:
 3
'''
# Bruteforce Approach
def bruteforce_Search_Target(A, B):
    N = len(A)
    for i in range(N):
        if A[i] == B:
            return i
    return -1
print(bruteforce_Search_Target([9, 10, 3, 5, 6, 8], 5))

def search_rotated_target_element(A, B):
    for i in range(len(A)):
        if A[i] == B:
            return i
    return -1
print(search_rotated_target_element([4, 5, 6, 7, 0, 1, 2, 3], 4))

# ✅ Optimal Approach
def search_rotated_sorted_array(A, B):
    left , right = 0, len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == B:
            return mid
        # Left half is sorted
        if A[left] <= A[mid]:
            if A[left] <= B < A[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if A[mid] < B <= A[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

# ✅ Test Case
print(search_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2, 3], 0))  # Expected output: 4

def search_rotated_sorted_array(A, B):
    left , right = 0, len(A) - 1
    while left <= right:
        mid = (left+(right - left))//2
        if A[mid] == B:
            return mid
        if A[left] <= A[mid]:
            if A[left] <= B < A[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if A[mid] < B <= A[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
print(search_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2, 3], 2))
