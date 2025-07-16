'''
✅ Question 1: Sliding Window (Medium)
Problem:

Given a string s, return the length of the longest substring without repeating characters.
'''
# Brute force approach
def longest_substring_without_repeating(s):
    max_len = 0
    n = len(s)
    start = 0
    for start in range(n): 
        seen = set()
        for end in range(start, n):
            if s[end] in seen:
                break
            seen.add(s[end])
            max_len = max(max_len, end - start + 1)
        if max_len == n - start:
            break
    return max_len
s = "abcabcbb"
print(longest_substring_without_repeating(s))
# Optimal Approach
def longest_substring(s):
    max_len = 0
    seen = set()
    n = len(s)
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