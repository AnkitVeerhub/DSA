'''
🧩 Day 1 – Problem 3: Max Consecutive Ones
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The longest run of 1s is from index 3 to 5.
'''
def max_consecutive_ones(nums):
    count = 0
    max_count = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count
print(max_consecutive_ones(nums=[1,1,1,2,3,0,0,1,1,11,9,0,0,1,1,1,1,10,1,1,1,1,1,1,1,1]))
# Optimal Approach - TC: O(N) | SC: O(1)
# def Max_Consecutive_Ones(nums):
#     count = 0
#     max_count = 0
#     for i in range(len(nums)):
#         if nums[i] == 1:
#             count += 1
#             max_count = max(max_count, count)
#         else:
#             count = 0
#     return max_count
# print(Max_Consecutive_Ones(nums=[1,1,1,1,1,0,1,1,1,1]))