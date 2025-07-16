'''
🧠 Problem: 26. Remove Duplicates from Sorted Array
📚 Platform: LeetCode – https://leetcode.com/problems/remove-duplicates-from-sorted-array/

🎯 Problem Statement:
Given a sorted array `nums`, remove the duplicates **in-place** such that each unique element appears only once. 
The relative order of the elements should be kept the same.
Return the number of unique elements (`new_length`), and modify `nums` such that the first `new_length` elements are the result.

🚫 Note:
- You must **not use extra space** — do this in-place with O(1) extra memory.

---

🔍 Example 1:
Input: nums = [1,1,2]  
Output: 2, nums = [1,2,_]

🔍 Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]  
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

---

🛠️ Approach:
- Use Two Pointers (Slow & Fast):  
  - `read_idx` scans through the array  
  - `write_idx` writes only unique values forward
- Compare each number with its previous; if different, it’s unique
- Overwrite duplicate positions

📌 Time Complexity: O(n)  
📌 Space Complexity: O(1) – in-place

---

🏢 Asked In:
- Google 🔍
- Amazon 🛒
- Microsoft 🪟
- Adobe 🧑‍🎨
- Flipkart 🛍️
- and many more top MNCs

'''

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0  # Handle empty array edge case

        write_idx = 1  # Position to write next unique element

        for read_idx in range(1, len(nums)):
            if nums[read_idx] != nums[read_idx - 1]:
                nums[write_idx] = nums[read_idx]
                write_idx += 1

        return write_idx


# 🔍 Example Test
if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    sol = Solution()
    new_len = sol.removeDuplicates(nums)

    print(f"✅ Unique Count: {new_len}")
    print(f"🧾 Final Array: {nums[:new_len]}")
