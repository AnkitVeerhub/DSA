'''
Monotonic Stack (Hard)
🎯 Interview Importance:
This is a high-frequency problem asked by:
💼 Company: Amazon,Google,Microsoft,Adobe,Samsung,Flipkart,Qualcomm,VMWare
💻 Platforms:
✅ LeetCode: Problem #84 - Largest Rectangle in Histogram

✅ GeeksforGeeks: Appears under Monotonic Stack and Histogram based problems.

✅ Codeforces: Variants of this problem appear in contests.

✅ InterviewBit and Coding Ninjas: Frequently practiced.
'''
# Brute force approach
def histogram(heights):
    n = len(heights)
    max_area = 0
    for i in range(n):
        height = heights[i]
        left = i
        while left > 0 and heights[left-1]>=height:
            left -= 1
        right = i
        while right < n - 1 and heights[right+1] >= height:
            right += 1
        width = right - left + 1
        area = width * height
        print(f"Index {i}: Height = {height}, Left = {left}, Right = {right}, Width = {width}, Area = {area}")
        max_area = max(max_area, area)
    return max_area
heights = [6,2,5,4,5,1,6]
print(histogram(heights))
'''
📊 Time Complexity:
Outer loop → O(n)

Each expansion can go O(n) in worst case →
Total: O(n²)
'''

# Optimal Approach
def largestRectangleArea(heights):
    # Add the 0 at the end to ensure all the rectangles are processed
    heights.append(0)
    stack = []
    max_area = 0
    for i, h in enumerate(heights):
        print(i,h)
        # Maintain an increasing stack
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop( )]
            # width is from the last smaller to current index
            width = i if not stack else i - stack[-1] - 1
            area = height * width
            max_area = max(max_area, area)
        stack.append(i)
    return max_area
# Example input
heights = [6, 2, 5, 4, 5, 1, 6]
print("Max Rectangle Area:", largestRectangleArea(heights))

'''
📊 Time and Space Complexity:
Time: O(n) → Each bar is pushed and popped at most once

Space: O(n) → Stack space in worst case
'''
