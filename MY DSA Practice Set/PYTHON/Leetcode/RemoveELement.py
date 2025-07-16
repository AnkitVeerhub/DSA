'''
🧠 Problem: Remove Element (LeetCode #27)
🎯 Tags: Arrays, Two Pointers, In-Place Algorithm
🛠️ Concept: Modify the array in-place and remove all occurrences of a given value.

📌 Platforms:
- ✅ LeetCode: https://leetcode.com/problems/remove-element/
- ✅ GFG: Similar in-place array manipulation problems
  e.g., "Move all zeroes to end", "Remove duplicates", "Move negative numbers to left"
  
🧪 Input:
    nums = [3, 2, 2, 3]
    val_to_remove = 3

🎯 Output:
    New length = 2
    Modified nums = [2, 2, _, _] (values beyond length don’t matter)

🧩 Approach:
    - Use two pointers (read + write)
    - Traverse entire array and overwrite only valid elements
    - Return the count of non-val elements (i.e., new length)

👨‍💻 Used by companies like Amazon, Google, Meta, Flipkart, Microsoft
'''

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val_to_remove: int) -> int:
        # Pointer to place the next valid (non-val) element
        insert_position = 0

        for current_index in range(len(nums)):
            if nums[current_index] != val_to_remove:
                nums[insert_position] = nums[current_index]
                insert_position += 1

        return insert_position


# 🔍 Test Case
if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val_to_remove = 3

    sol = Solution()
    new_length = sol.removeElement(nums, val_to_remove)

    print(f"✅ New Length: {new_length}")
    print(f"🧾 Modified Array: {nums[:new_length]}")  # Output valid portion
