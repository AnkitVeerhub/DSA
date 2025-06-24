'''
Reverse the given string using both brute force and optimal approach

💬 Interviewer Perspective:
Brute force: O(n²) time (due to string immutability and repeated concatenation).

Optimal: O(n) time and O(n) space using two-pointer technique.
'''
# Brute force approach
def reverse_string(string):
    reverse = ""
    for index in string:
        reverse = index + reverse
    return reverse 
string = "Ankit ki baili Kajali"
print(reverse_string(string))

# Optimal Approach
def reverse_string(string):
    reverse_stack = list(string)
    left, right = 0, len(string) - 1
    while left < right:
        reverse_stack[left], reverse_stack[right] = reverse_stack[right], reverse_stack[left]
        left += 1
        right -= 1

    return "".join(reverse_stack)
string = "Ankit ki baili Kajali"
print(reverse_string(string))