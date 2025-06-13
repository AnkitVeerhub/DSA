'''
Problem Description
Given 2 integers A and B and an array of integers C of size N. Element C[i] represents the length of ith board.
You have to paint all N boards [C0, C1, C2, C3 … CN-1]. There are A painters available and each of them takes B units of time to paint 1 unit of the board.
Calculate and return the minimum time required to paint all boards under the constraints that any painter will only paint contiguous sections of the board.
NOTE:
1. 2 painters cannot share a board to paint. That is to say, a board cannot be painted partially by one painter, and partially by another.
2. A painter will only paint contiguous boards. This means a configuration where painter 1 paints boards 1 and 3 but not 2 is invalid.
Return the ans % 10000003.

Example Input

Input 1:

 A = 2
 B = 5
 C = [1, 10]
Input 2:

 A = 10
 B = 1
 C = [1, 8, 11, 3]


Example Output

Output 1:

 50
Output 2:

 11


Example Explanation

Explanation 1:

 Possibility 1:- One painter paints both blocks, time taken = 55 units.
 Possibility 2:- Painter 1 paints block 1, painter 2 paints block 2, time take = max(5, 50) = 50
 There are no other distinct ways to paint boards.
 ans = 50 % 10000003
Explanation 2:

 Each block is painted by a painter so, Painter 1 paints block 1, painter 2 paints block 2, painter 3 paints block 3 
 and painter 4 paints block 4, time taken = max(1, 8, 11, 3) = 11
 ans = 11 % 10000003
'''
class Solution:
    def solve(self, A, B, C):
        def isPossible(timeLimit):
            painters, totalTime = 1, 0
            for length in C:
                totalTime += length * B
                if totalTime > timeLimit:
                    painters+=1
                    totalTime = length * B
                    if painters > A:
                        return False
            return True
        if A >= len(C):
            return (max(C) * B) % 10000003
        left, right = max(C) * B , sum(C) * B
        while left <= right:
            mid = (left + right) // 2
            if isPossible(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans % 10000003
solution = Solution()
A = 2  # Number of painters
B = 5  # Time per unit length
C = [1, 10]  # Lengths of boards

print(solution.solve(A,B,C))


'''
🧠 Problem Recap:
You’re given:
An array of board_lengths, each representing the length of a board.
k painters.
Painters can paint only contiguous sections of boards.
Goal: Minimize the time taken by the painter with the maximum workload.
'''

# Brute Force Approach
def find_min_time_bruteforce(boards, k):
    def helper(index, k):
        if k == 1:
            return sum(boards[index:])
        min_time = float('inf')
        total = 0
        for i in range(index, len(boards) - k + 1):
            total += boards[i]
            max_time = max(total, helper(i + 1, k - 1))
            min_time = min(min_time, max_time)
        return min_time
    return helper(0,k)

boards = [10, 20, 30, 40]
k = 2
print("Minimum time (Brute Force):", find_min_time_bruteforce(boards, k))