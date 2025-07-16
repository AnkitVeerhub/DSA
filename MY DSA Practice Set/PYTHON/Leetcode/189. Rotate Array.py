'''
189. Rotate Array
'''

# Brute force approach
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # We'll implement logic here
        n = len(nums)
        k = k % n
        for _ in range(k):
            last = nums[-1] # Save the last element
            # Shift all the elements to the right
            for i in range(n - 1, 0, -1):
                nums[i] = nums[i - 1]
            nums[0] = last
nums, k = [1, 2, 3, 4, 5], 1
sol = Solution()
sol.rotate(nums, k)
print(nums)  # ✅ Output: [5, 1, 2, 3, 4]

# Optimal Approach

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # Handle k > n

        # Helper function to reverse elements in-place
        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        # Apply the 3-step reverse trick
        reverse(0, n - 1)       # Reverse the whole array
        reverse(0, k - 1)       # Reverse the first k elements
        reverse(k, n - 1)       # Reverse the rest
nums, k = [1, 2, 3, 4, 5], 1
sol = Solution()
sol.rotate(nums, k)
print(nums)