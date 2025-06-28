'''
Q4. First Repeating element
Problem Description

Given an integer array A of size N, find the first repeating element in it.
We need to find the element that occurs more than once and whose index of the first occurrence is the smallest.
If there is no repeating element, return -1.

Example Input
Input 1:
A = [10, 5, 3, 4, 3, 5, 6]
Input 2:
A = [6, 10, 5, 4, 9, 120]

Example Output
Output 1:
5
Output 2:
-1
Example Explanation
Explanation 1:
5 is the first element that repeats
Explanation 2:
There is no repeating element, output -1
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        seen = set()
        repeat = -1

        # Traverse from end to find the first element that repeats
        for i in reversed(range(len(A))):
            if A[i] in seen:
                repeat = A[i]  # update the most recent repeating element
            else:
                seen.add(A[i])

        return repeat
A = [10, 5, 3, 4, 3, 5, 6]
sol = Solution()
print(sol.solve(A))