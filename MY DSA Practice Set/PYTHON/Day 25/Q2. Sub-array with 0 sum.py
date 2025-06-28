'''
🧠 Problem Statement:
Given an integer array A[], determine if there exists a subarray 
(contiguous elements) whose sum is 0.
Example Input
Input 1:
A = [1, 2, 3, 4, 5]
Input 2:
A = [4, -1, 1]
Example Output
Output 1:
0
Output 2:
1
Example Explanation
Explanation 1:
No subarray has sum 0.
Explanation 2:
The subarray [-1, 1] has sum 0.
📌 Platforms & Companies:
Platform: GeeksforGeeks, LeetCode (variation), InterviewBit
Asked In: Amazon, Paytm, Accolite, Snapdeal, MAQ Software, Adobe, Morgan Stanley
'''
'''
✅ Step-by-Step Plan:
🔹 Edge Case 1: Empty array
If array is empty: return False (no elements ⇒ no subarrays)

🔹 Edge Case 2: Single element 0
If array has only one element and it's 0 ⇒ return True

🔹 Edge Case 3: Element itself is zero
If any individual element is 0, return True immediately
'''
# Optimal Approach

def has_zero_sum_subarray(arr):
    seen = set()
    prefix_sum = 0
    for num in arr:
        prefix_sum += num
        # Edge COndition
        if prefix_sum == 0 or num == 0 or prefix_sum in seen:
            return True
        seen.add(prefix_sum)
    return False
print(has_zero_sum_subarray(arr=[4,2,-3,1,6]))

'''
✅ Time and Space Complexity:
Time: O(n)
Space: O(n) in worst case (set to store prefix sums)
'''

# 🔍 Alternate Approaches (For Comparison)
# ❌ Brute Force (Nested Loop)
def has_zero_sum_subarray(arr):
    n = len(arr)  # ✅ Define once outside the loop
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if curr_sum == 0:
                return True
    return False  # ✅ If no such subarray found

# Example test
print(has_zero_sum_subarray([4, 2, -3, 1, 6]))  # Output: True

'''
Time: O(n^2)
Space: O(1)
❗ This will fail in interviews for large input sizes due to TLE.
'''