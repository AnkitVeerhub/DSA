'''
✅ Problem Name: Minimize Maximum Element After B Additions
💡 Data Structures: Heap (Min-Heap)
📂 Suggested File Name: minimize_max_after_b_additions.py
📈 Difficulty Level: Medium to Hard
🏢 Asked In: Amazon, Microsoft
🌐 Platforms: Found in variations on LeetCode, Codeforces, and InterviewBit
'''
from itertools import product

# Step 1: Define the brute force function
def min_max_element(A,B):
    N = len(A)
    original = A[:]
    print(original)
    min_max = float('inf')
    for distribution in product(range(B+1), repeat=N):
        if sum(distribution) != B:
            continue
        new_A = []
        for i in range(N):
            value = A[i] + distribution[i] * original[i]
            new_A.append(value)
        max_value = max(new_A)
        if max_value < min_max:
            min_max = max_value
    return min_max
A = [-2,-4,-8,-16]
B = 10
result = min_max_element(A, B)
print(f"\n🔚 Final answer (minimum possible max): {result}")

import heapq

arr = [3, 1, 5]
max_heap = [-x for x in arr]
print(max_heap)
heapq.heapify(max_heap)
print(max_heap)
max_val = -heapq.heappop(max_heap)  # gives you the actual max
print(max_val)
'''
✅ Question 6: What will be the result of popping all values from a heapified list?
Your statement:

"We will get the minimum heap value, that is result[-1] as an answer"

🔧 Let's improve that to a complete and correct explanation:

🎯 Refined Interview-Ready Answer:
If you repeatedly pop all elements from a heapified list using heapq.heappop(), you will retrieve the elements in increasing sorted order, starting from the smallest.

So, the sequence of popped values will be:

Sorted version of the original list (ascending order)

📌 In other words, heapq can be used as an efficient way to sort a list in ascending order (like a priority queue).

✅ Example:
python
Copy
Edit
import heapq

arr = [4, 1, 7, 3, 8, 5]
heapq.heapify(arr)

while arr:
    print(heapq.heappop(arr), end=" ")
💡 Output:

Copy
Edit
1 3 4 5 7 8
The list is sorted in increasing order — because it’s a Min Heap.
'''


import heapq
def minimize_maximum(A, B):
    n = len(A)
    original = A[:] # Keep the original array
    heap = []
    # Initialize the heap with (current_value, original_value)
    for i in range(n):
        heapq.heappush(heap, (A[i], original[i]))
    # Perform B Operations
    for _ in range(B):
        current, orig = heapq.heappop(heap)
        new_val = current + orig
        heapq.heappush(heap, (new_val, orig))
    # Extract final values to find the max
    max_val = max([val for val, _ in heap])
    return max_val
A = [8,6,4,2]
B = 8
print(minimize_maximum(A, B))  # Output: 9
'''
🎯 Explanation:

Start with [2, 3]

After 1st op: 2 → 4 → [3, 4]

After 2nd op: 3 → 6 → [4, 6]

After 3rd op: 4 → 6 → [6, 6] → max = 6 ✅

⏱ Time Complexity:

Building the heap: O(N)

Each of B operations: O(log N)

Final max calculation: O(N)

🧠 Overall: O(B log N + N)
'''