'''
✅ Problem Statement (Simplified):
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
✅ Approach: Frequency HashMap
Count frequency of each char in both strings.
Compare the two maps.
If same → return true, else false.
Input: s = "anagram", t = "nagaram"
Output: True
'''

# BruteForce Approach
def isAnagram(s, t):
    return sorted(s) == sorted(t)
print(isAnagram(s = "listen", t = "silent"))
'''
🧠 Time & Space:
Time Complexity: O(n log n) due to sorting
Space Complexity: O(1) if we ignore sorting space
📌 Use case in interviews:
Good for initial brute-force discussion
Interviewers might ask you to improve it
'''
# Optimal Approach
'''
Optimal Approach (HashMap / Frequency Counter)
💡 Idea:
Count the frequency of characters in both strings. If they match, it's an anagram.
'''
def isAnagram(s,t):
    if len(s) != len(t):
        return False
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    for ch in t:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False
    return True
print(isAnagram(s = "listen", t = "silent"))

def isAnagram(s,t):
    if len(s) != len(t):
        return False
    count = {}
    for ch in s:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    for ch in t:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False
    return True
print(isAnagram(s = "listen", t = "silent"))




