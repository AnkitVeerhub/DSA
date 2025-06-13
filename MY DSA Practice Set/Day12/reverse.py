'''
Problem Description
Given a string A, you are asked to reverse the string and return the reversed string.
Problem Constraints
1 <= |A| <= 10^5
String A consist only of lowercase characters.
'''
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        reverse = ""
        for i in A:
            reverse = i + reverse
        return reverse
sol = Solution()
A = "Aman"
print(sol.solve(A))

# Using Optimal
class Solution:
    # @param A : string
    # @return a string
    def solve(self, A):
        chars = list(A)     # Convert string to list
        left, right = 0, len(chars) - 1
        
        # Reverse the list in-place using two pointers
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        
        return ''.join(chars)  # Join list back to string
sol = Solution()
A = "Aman"
print(sol.solve(A))
'''
🧠 Interview Tip:
If asked why not use A[::-1], explain that it’s Pythonic and concise 
but might be seen as a built-in shortcut rather than an algorithmic solution.
Use the two-pointer approach to demonstrate core algorithm understanding.

🎯 Interview Tip:
When asked:
“How else can you reverse a string?”
Say:
“There’s the brute force approach using character-by-character construction.”
“I also know a two-pointer method (optimal).”
“We can do it recursively or with Pythonic slicing — though 
recursion can be inefficient and slicing might be considered a shortcut.”
'''