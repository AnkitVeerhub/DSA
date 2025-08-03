'''
🧠 Longest Substring Without Repeating Characters
(Real interview question at Amazon, Adobe, Flipkart, and Microsoft)

🔸 Problem Statement:
Given a string s, find the length of the longest substring without repeating characters.

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", which the length is 3.
'''
'''
Brute Force: O(n²) time, O(n) space
Optimal (Sliding Window): O(n) time, O(n) space
'''
# Brute force Approach
def length_of_longest_substring(s):
    n = len(s)
    max_len = 0
    start = 0
    for start in range(n):
        seen = set()
        for end in range(start, n):
            if s[end] in seen:
                break
            seen.add(s[end])
            max_len = max(max_len,end - start + 1)
        if max_len == n - start:
            break
    return max_len
s = "abcabcbb"
print(length_of_longest_substring(s))

# Optimal Approach
def longest_substring(s):
    seen = set()
    n = len(s)
    max_len = 0
    start = 0
    for end in range(n):
        while s[end] in seen:
            seen.remove(s[start])
            start += 1
        seen.add(s[end])
        max_len = max(max_len, end - start + 1)
    return max_len
s = "abcabcbb"
print(longest_substring(s))


            