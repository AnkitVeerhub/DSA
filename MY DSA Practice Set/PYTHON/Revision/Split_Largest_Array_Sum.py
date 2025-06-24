'''
Split Largest Array Sum
'''
def split_array_largets_sum(nums, k):
    def can_split(max_sum):
        count, total = 1, 0
        for num in nums:
            if total + num > max_sum:
                count += 1
                total = num
            else:
                total += num
        return count <= k
    low, high = max(nums), sum(nums)
    answer = high
    while low <= high:
        mid = (low + high) // 2
        if can_split(mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    return answer

# Define the input
nums = [7, 2, 5, 10, 8]
k = 2


# Call the method
print(split_array_largets_sum(nums, k))
