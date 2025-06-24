'''
💼 Asked In:
Google, Facebook, Amazon, Flipkart, Uber
🚀 Let's Start
👨‍💻 Platform: InterviewBit (Simulated Interview)
💼 Interviewer says:
"Let's test your understanding of arrays and hash maps. Solve this in under 20 minutes with an optimal solution ready after the brute force one."
🧩 Problem: 1. Longest Consecutive Sequence
📁 Filename: longest_consecutive_sequence.py
🎯 Problem Statement:
Given an unsorted array of integers, find the length of the longest sequence of consecutive elements (regardless of order).
You must write an O(n) solution.
📋 Constraints:
1 <= len(A) <= 10^5
-10^9 <= A[i] <= 10^9
🧠 Expected Approach:
First try a brute force method (likely sorting or nested loops).
Then aim for an O(n) hash set-based solution.
'''

def longest_Consecutive(nums: list[int]) -> int:
    if not nums:
        return 0
    max_length = 0
    n = len(nums)
    for i in range(n):
        current = nums[i]
        length = 1
        nex_num = current + 1
        while nex_num in nums:
            length += 1
            nex_num += 1
        max_length = max(max_length, length)
    return max_length
'''
🧠 Interview Tip:
If the interviewer asks "Why is this brute force?", say:
“Because for each element I do a linear scan (next_num in nums) which is O(n), 
and I repeat this for every element — making total time complexity O(n²) in worst case.”
'''
nums = [100,2,4,3,200,1]
print(longest_Consecutive(nums))
'''
⏱️ Time Complexity:
Each in operation takes O(n) → O(n²) worst-case.
You can still optimize this later using a HashSet and O(n) approach — we'll do that next.
'''
# optimal
def largest_consecutive(nums):
    if not nums:
        return 0
    nums_set = set(nums)
    max_length = 0
    for num in nums_set:
        if num - 1 not in nums_set:
            current_num = num
            current_length = 1
            while current_num + 1 in nums_set:
                current_num += 1
                current_length += 1
            max_length = max(max_length, current_length)
    return max_length
nums = [100,2,4,3,200,1]
print(largest_consecutive(nums))