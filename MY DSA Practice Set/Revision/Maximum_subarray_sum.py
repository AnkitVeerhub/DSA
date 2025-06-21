'''
Maximum subarray sum
'''
# Bruteforce Approach
def max_sum_subarray(A):
    n = len(A)
    max_sum = float('-inf')
    for i in range(n):
        for j in range(i, n):
            curr_sum = 0
            for k in range(i, j + 1):
                curr_sum += A[k]
            max_sum = max(max_sum, curr_sum)
    return max_sum
print(max_sum_subarray([1,2,3,4]))

# Optimal Approach
def max_subarray_sum_optimal(A):
    curr_sum = 0
    max_sum = float('-inf')
    for num in A:
        curr_sum += num
        max_sum = max(max_sum, curr_sum)
        if curr_sum < 0:
            curr_sum = 0
    return max_sum
print(max_subarray_sum_optimal([1,2,3,4]))

# Brute force Approach
A = [1,2,3,4]
def get_max_sum_subarray(A):
    n, max_sum = len(A), float('-inf')
    for i in range(n):
        for j in range(i, n):
            current_sum = 0
            for k in range(i, j + 1):
                current_sum += A[k]
            max_sum = max(max_sum, current_sum)
    return max_sum
    
print(get_max_sum_subarray(A))

# Optimal Approach
def max_sum_of_all_subarray(A):
    max_sum = float('-inf')
    current_sum = 0
    for i in A:
        current_sum += i
        max_sum = max(current_sum, max_sum)
        if current_sum < 0:
            current_sum = 0

    return max_sum

A = [1,2,3,4]
print(max_sum_of_all_subarray(A))