def find_unique(A):
    n = len(A)
    if n == 1:
        return A[0]
    if A[0] != A[1]:
        return A[0]
    if A[n-1] != A[n-2]:
        return A[n-1]
    low, high = 1, n - 2
    while low <= high:
        mid = (low+high)//2
        if A[mid] != A[mid-1] and A[mid] != A[mid+1]:
            return A[mid]
        if A[mid] == A[mid - 1]:
            mid = mid - 1
        if mid % 2 == 0:
            low = mid + 2
        else:
            high = mid - 1
    return A[mid]
A = [3,3,1,1,8,8,10,10,9,6,6,2,2,4,4]
print(find_unique(A))


# def find_unique(A):
#     nums = 0
#     for num in A:
#         nums = num^nums
#     return nums
# A = [3,3,1,1,8,8,10,10,9,6,6,2,2,4,4]
# print(find_unique(A))