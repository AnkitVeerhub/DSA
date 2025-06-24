'''
Q1. Print paths in Staircase
Problem Description
You are climbing a staircase and it takes A steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
You need to return all the distinct ways to climb to the top in lexicographical order.
Problem Constraints
2 <= A <= 25
Output Format
Return an 2-D Integer Array, which denotes all the unique valid paths to reach the top.
Example Input
Input 1:
A = 2
Input 2:
A = 3
Example Output
Output 1:

[ [1, 1], [2] ]
Output 2:

[ [1, 1, 1], [1, 2], [2, 1] ]
Example Explanation
Explanation 1:
Distinct ways to reach top: 1 + 1, 2.
Explanation 2:

Distinct ways to reach top: 1 + 1 + 1, 1 + 2, 2 + 1.
'''

class Solution:
    def climbStairsWays(self, A: int) -> List[List[int]]:
        result = []

        def dfs(current_path, current_sum):
            if current_sum == A:
                result.append(current_path[:])
                return
            if current_sum > A:
                return
            # Try step 1
            current_path.append(1)
            dfs(current_path, current_sum + 1)
            current_path.pop()

            # Try step 2
            current_path.append(2)
            dfs(current_path, current_sum + 2)
            current_path.pop()

        dfs([], 0)
        result.sort() # Lexicographical sort
        return result

def climbStairsWays(A):
    result = []
    def dfs(current_path, current_sum):
        # base case: we reached exactly step A
        if current_sum == A:
            result.append(current_path[:])
            return
        # invalid case: we went too far
        if current_sum > A:
            return
        # recursive decisions
        for step in [1, 2]:
            current_path.append(step)
            dfs(current_path, current_sum + step)
            current_path.pop()
    dfs ([], 0)
    result.sort()
 # Lexicographical sort
    return result