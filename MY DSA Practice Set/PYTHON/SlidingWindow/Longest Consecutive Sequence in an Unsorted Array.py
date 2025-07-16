'''
Longest Consecutive Sequence in an Unsorted Array
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4].
'''

# Brute Force Approach
def longest_consecutive_sequence(arr):
    num_set = set(arr)
    max_len = 0
    for num in arr:
        current_num = num
        streak = 1
        while current_num + 1 in num_set:
            current_num += 1
            streak += 1
        max_len = max(max_len, streak)
    return max_len
arr = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_sequence(arr))

# Optimal Approach
def longest_consecutive_sequence(arr):
    num_set = set(arr)
    max_len = 0
    for num in arr:
        if num - 1 not in num_set:
            current_num = num
            streak = 1
            while current_num + 1 in num_set:
                current_num += 1
                streak += 1
            max_len = max(max_len, streak)
    return max_len
arr = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_sequence(arr))



