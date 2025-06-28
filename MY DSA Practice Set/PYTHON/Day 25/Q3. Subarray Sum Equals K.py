'''
Q3. Subarray Sum Equals K
Problem Description

Given an array of integers A and an integer B.
Find the total number of subarrays having sum equals to B.

✅ Optimal Approach: Prefix Sum + HashMap

'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        prefix_sum = 0
        count = 0
        prefix_map = {0: 1}  # Initialize with base case for subarrays starting from index 0

        for num in A:
            prefix_sum += num  # Running prefix sum

            # Check if there is a prefix that if removed, leaves a sum of B
            if (prefix_sum - B) in prefix_map:
                count += prefix_map[prefix_sum - B]

            # Update the map with current prefix_sum
            if prefix_sum in prefix_map:
                prefix_map[prefix_sum] += 1
            else:
                prefix_map[prefix_sum] = 1

        return count
A = [1, 0, 1]
B = 1
sol = Solution()
print(sol.solve(A, B))

# Brute force approach - Time complexity = O(n²) → not good for large inputs.
arr = [1, 0, 1]
B = 1
n = len(arr)
count = 0
for i in range(n):
    for j in range(i, n):
        if sum(arr[i:j+1]) == B:
            count += 1
print(count)