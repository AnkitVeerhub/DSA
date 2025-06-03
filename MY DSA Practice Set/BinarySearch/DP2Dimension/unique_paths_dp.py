'''
Given: Grid of size m x n
Goal: Count how many unique paths from top-left (0, 0) to bottom-right (m-1, n-1) only by moving right or down.
'''
class Solution:
	# @param A : list of list of integers
	# @return an integer
	def uniquePathsWithObstacles(self, A):
        n, m = len(A), len(A[0])
        dp = [[0]*m for _ in range(n)]
        dp[0][0] = 1 if A[0][0] == 0 else 0

        for j in range(1, m):
            dp[0][j] = dp[0][j - 1] if A[0][j] == 0 else 0

        for i in range(1, n):
            dp[i][0] = dp[i-1][0] if A[i][0] == 0 else 0

        for i in range(1, n):
            for j in range(1, m):
                if A[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0

        return dp[n-1][m-1]
       

# def unique_paths(m, n):
#     # Step 1: Initialize the DP table
#     dp = [[1]*n for _ in range(m)]

#     # Step 2: Fill the DP table using recurrence
#     for i in range(1, m):
#         for j in range(1, n):
#             dp[i][j] = dp[i-1][j] + dp[i][j-1]

#     # ✅ Print the answer first (top of output)
#     # print(f"Unique paths from (0, 0) to ({m-1}, {n-1}): {dp[m-1][n-1]}\n")

#     # Optional: Debug - show how we filled the DP table
#     print("DP Table:")
#     for i in range(m):
#         for j in range(n):
#             print(f"dp[{i}][{j}] = {dp[i][j]}", end="\t")
#         print()
    
#     return dp[m-1][n-1]

# # Example
# m, n = 3, 3
# unique_paths(m, n)

def unique_paths(m, n):
    # Step 1: Initialize the DP table with all 1s for the first row and first column
    dp = [[1]*n for _ in range(m)]
    print(dp)

    print("Initial DP Table:")
    for row in dp:
        print(row)
    print("\nFilling the DP table...\n")

    # Step 2: Fill the table using the recurrence relation
    # for i in range(1, m):
    #     for j in range(1, n):
            # The cell dp[i][j] is the sum of the cell above and the cell to the left
    #         dp[i][j] = dp[i-1][j] + dp[i][j-1]
    #         print(f"dp[{i}][{j}] = dp[{i-1}][{j}] + dp[{i}][{j-1}] --> {dp[i][j]} = {dp[i-1][j]} + {dp[i][j-1]}")

    # print("\nFinal DP Table:")
    # for row in dp:
    #     print(row)

    # return dp[m-1][n-1]

# Example usage:
m, n = 3, 3
print(f"\nTotal unique paths from (0,0) to ({m-1},{n-1}): {unique_paths(m, n)}")
