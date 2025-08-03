'''
✅ Maximum Sum Subarray of Fixed Size K
'''
def maximum_sum_subarray_of_size_k(nums, k):
    max_sum = float('-inf')
    start, window_sum = 0, 0
    for end in range(len(nums)):
        window_sum += nums[end]
        if end - start + 1 == k:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[start]
            start  += 1
    return max_sum
print(maximum_sum_subarray_of_size_k(nums=[2,1,5,1,3,2], k = 3))