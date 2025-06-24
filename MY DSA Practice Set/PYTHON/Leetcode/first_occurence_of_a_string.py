'''
✅ Problem: Find the Index of the First Occurrence in a String
💻 Platform: LeetCode
Link: LeetCode 28 - Find the Index of the First Occurrence in a String
💼 Asked By: Amazon, Microsoft, Google, Facebook
🔍 Problem Statement
Given two strings haystack and needle, 
return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.
🧠 Time and Space Complexity
Time: O(n * m) in the worst case (n = len(haystack), m = len(needle))
Space: O(1)
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_length ,needle_length = len(haystack), len(needle)
        # Edge Case
        if needle_length == 0:
            return needle_length
        for start_index in range(haystack_length - needle_length + 1):
            if haystack[start_index:start_index + needle_length] == needle:
                return start_index
        return -1
haystack, needle = "sadbutsad", "sad"
sol = Solution()
print(sol.strStr(haystack, needle))
'''
🔍 Dry Run
haystack = "sadbutsad", needle = "sad"
i = 0 → haystack[0:3] = "sad" → ✅ Match → return 0
Done.
'''