'''
Given a sorted array of intergers A where every element appears twice except for one element
which appears once, find and return this single element that appear only once.
Elements that are appearing twice are adjacent to each other.
Note: Users are expected to solve this in O(og (N)) time. 
Example Input
Input 1:
A = [1, 1, 7]
Input 2:
A = [2, 3, 3]
Example Output
Output 1:
 7
Output 2:
 2
'''

# Bruteforce Approach
def find_single_element(A):
    N = len(A)
    for i in range(0, N - 1, 2):
        if A[i] != A[i + 1]:
            return A[i]
    return A[-1]
print(find_single_element([1,1,2,2,3,3,4,5,5]))

# 💡 Time Complexity: O(n)
# 💾 Space Complexity: O(1)

# Let's Solve with Optimal Approach

def find_single_element(arr):
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2
        # Ensure mid is even
        if mid % 2 == 1:
            mid -= 1
        
        if arr[mid] == arr[mid + 1]:
            low = mid + 2
        else:
            high = mid

    return arr[low]

print(find_single_element([1,1,2,2,3,3,4,5,5]))
