'''
🔹 Problem: Longest Substring Without Repeating Characters
🧠 Platform: LeetCode
🧠 Difficulty: Medium
📂 Tags: Hashing, Sliding Window, Strings
💼 Company Asked in: Amazon, Google, Adobe, Microsoft

🧾 Problem Statement
Given a string s, find the length of the longest substring without repeating characters.

🔒 Constraints
0 <= len(s) <= 5 * 10^4

s consists of English letters, digits, symbols, and spaces.
'''
# Bruteforce Approach
def longest_substring(S):
    if S == "":
        return 0
    n = len(S)
    max_length = 0
    for i in range(n):
        seen = set()
        for j in range(i , n):
            if S[j] in seen:
                break
            seen.add(S[j])
            max_length = max(max_length, j - i + 1)
    # ✅ Early exit: Can't get longer than this
        if max_length == n - i:
            break
    return max_length
S = "abcabcbb"
print(longest_substring(S))

# Optimal Approach
def longest_substring_optimal(A):
    seen = set()
    max_length = 0
    start = 0
    for end in range(len(A)):
        while A[end] in seen:
            seen.remove(A[start])
            start += 1
        seen.add(A[end])
        max_length = max(max_length, end - start + 1)
    return max_length
A = "abcbbcbbabc"
print(longest_substring_optimal(A))