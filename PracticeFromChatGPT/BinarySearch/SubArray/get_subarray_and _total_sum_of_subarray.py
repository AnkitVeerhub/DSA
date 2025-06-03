'''
Get the all subarray and total sum of subarray
Find Max Subarray
A = [1,2,3,4] , output: 55
'''

def max_sub_array_brute_force(A):
    n = len(A)
    total_sum = 0
    for i in range(n):
        for j in range(i,n):
            curr_sum = 0
            for k in range(i,j+1):
                curr_sum += A[k]
            total_sum += curr_sum
    return total_sum

A = [1,2,3,4]
print(max_sub_array_brute_force(A))



