'''
Q1. Longest Substring Without
Problem Description
Determine the "GOOD"ness of a given string A, where the "GOOD"ness is defined by the length of the longest substring that contains no repeating characters. The greater the length of this unique-character substring, the higher the "GOOD"ness of the string.
Your task is to return an integer representing the "GOOD"ness of string A.
Note: The solution should be achieved in O(N) time complexity, where N is the length of the string.
Problem Constraints
1 <= size(A) <= 106
String consists of lowerCase,upperCase characters and digits are also present in the string A.
Input Format
Single Argument representing string A.
Output Format
Return an integer denoting the maximum possible length of substring without repeating characters.
Example Input
Input 1:
A = "abcabcbb"
Input 2:
A = "AaaA"
Example Output
Output 1:
3
Output 2:
2
Example Explanation
Explanation 1:
Substring "abc" is the longest substring without repeating characters in string A.
Explanation 2:
Substring "Aa" or "aA" is the longest substring without repeating characters in string A.
'''

class Solution:
	# @param A : string
	# @return an integer
    def lengthOfLongestSubstring(self, A):
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
A = "abcabcbb"
sol = Solution()
print(sol.lengthOfLongestSubstring(A))

# Bruteforce Approach
def longest_substring(A):
    max_len = 0
    for i in range(len(A)):
        for j in range(i, len(A)):
            char_set = set()
            substring = A[i: j+1]
            is_unique = True
            for char in substring:
                if char in char_set:
                    is_unique = False
                    break
                char_set.add(char)
            if is_unique:
                max_len = max(max_len, len(substring))
    return max_len
print(longest_substring(A = "abcabcbb"))


# Brute force approach without using Slicing
def longest_substring(A):
    max_len = 0
    for i in range(len(A)):
        char_set = set()
        for j in range(i, len(A)):
            if A[j] in char_set:
                break
            char_set.add(A[j])
            max_len = max(max_len, j - i + 1)
    return max_len
print(longest_substring(A = "abcabcbb"))

# Optimal Approach
def longest_substring(A):
    seen = set()
    left = 0
    max_len = 0
    for right in range(len(A)):
        while A[right] in seen:
            seen.remove(A[left])
            left += 1
        seen.add(A[right])
        max_len = max(max_len, right - left + 1)
    return max_len
# Test
print(longest_substring("abcabcbb"))