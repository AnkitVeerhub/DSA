'''
# Brute force approach
'''
def largest_consecutive_sequence(nums):
    n = len(nums)
    max_length = 0
    for i in range(n):
        current_element = nums[i]
        length = 1
        while current_element + 1 in nums:
            current_element+=1
            length += 1
        max_length = max(max_length, length)
    return max_length
print(largest_consecutive_sequence([100,2,3,4,300,1]))

# Using Hash set
'''
    ✅ Why we check num - 1 not in num_set:
    We check whether the current number has a predecessor in the set.

    If it does (num - 1 in num_set) → 
    This means the current number is part of an existing sequence, so we skip it to avoid redundant work.

    If it doesn't (num - 1 not in num_set) →
    This means the current number could be the start of a new consecutive sequence, so we begin counting from it.
'''
def Largest_Consecutive_Sequence_Optimal(nums):
    num_set = set(nums)
    max_length = 0
    for num in num_set:
        if num - 1 not in num_set:
            current = num
            length = 1
            while current + 1 in num_set:
                current += 1
                length += 1
            max_length = max(max_length, length)
    return max_length
print(Largest_Consecutive_Sequence_Optimal([100,2,3,4,200,1]))


'''
✅ Optimized Steps – Longest Consecutive Sequence (Optimal Approach)
1. Put all elements in a set
→ num_set = set(nums) (removes duplicates, enables O(1) lookups)

2. Initialize longest streak → longest = 0

3. For each number in the set:

    a.) If num - 1 not in set → it's the start of a sequence

    b.) Count the sequence using while num + 1 in set

    c.) Update longest with max streak

4. Return the longest streak
'''
# Longest Consecuting Sequence Optimal Approach
def Longest_Consecuting_Sequence(A):
    num_set = set(A)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            longest = max(longest, current_streak)
    return longest
A = [100,2,3,4,300,1,0]
print(Longest_Consecuting_Sequence(A))


# Pr1:
def longestConsecutive(nums):
    # Using hashset to skipping the duplicates values and constant time lookup
    num_set = set(nums)
    longest_streak = 0
    # starting of for loop
    for num in num_set:
        current_num = num
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)
    return longest_streak
nums = [100, 2, 3, 4, 200, 1]
print(longestConsecutive(nums))



            


