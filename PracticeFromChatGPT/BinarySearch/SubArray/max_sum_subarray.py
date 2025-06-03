'''
Find Max Subarray
A = [1,2,3,4] , output: 6
'''

def max_subarray_sum_brute(A):
    n = len(A)
    max_sum = float('-inf')
    for i in range(n):
        print(i)
        for j in range(i, n):
            print(j)
            curr_sum = 0
            for k in range(i, j + 1):
                print(k)
                curr_sum += A[k]
            max_sum = max(max_sum, curr_sum) 
    return max_sum
# Test
print(max_subarray_sum_brute([1,2,3,4]))  # Output: 6


def max_subarray_sum_kadane(A):
    current_sum = 0
    max_sum = float('-inf')
    
    for num in A:
        print(num)
        current_sum += num
        max_sum = max(max_sum, current_sum)
        
        if current_sum < 0:
            current_sum = 0
    return max_sum

# Test
print(max_subarray_sum_kadane([1,2,3]))  # Output: 6