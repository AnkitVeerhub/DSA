'''
Distribute Candy to the chile
Greedy Algirithm
Problem Description
N children are standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum number of candies you must give?
Problem Constraints
1 <= N <= 10^5
-10^9 <= A[i] <= 10^9

💼 Companies Asked:
Amazon, Salesforce, Google, Adobe

Very common on LeetCode, InterviewBit, GeeksForGeeks

🧠 How to Present in Interviews:
“I approached the problem using a greedy strategy by ensuring every child has at least one candy.
Then, I traversed the list twice—first from left to right to satisfy the left neighbor condition, and then right to left for the right neighbor.
This ensures both conditions are met in O(N) time and space.”
'''
# Bruteforce approach
def main_candies_bruteforce(ratings):
    n = len(ratings)
    if n == 0:
        return 0
    candies = n * [1]
    updated = True
    while updated:
        updated = False
        # Left to Right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
                candies[i] = candies[i - 1] + 1
                updated = True
        # Right to Left
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1
                updated = True
    return sum(candies)
# Test it
print(main_candies_bruteforce([1, 2, 2]))  # Output should be 4

# Optimal Approach
def candy(large_ratings):
    n = len(large_ratings)
    candies = [1] * n
    for i in range(1, n):
        if large_ratings[i] > large_ratings[i - 1]:
            candies[i] = candies[i-1] + 1
    for i in range(n - 2, -1, -1):
        if large_ratings[i] > large_ratings[i + 1] and candies[i] <= candies[i+1]:
            candies[i] = candies[i+1] + 1
    return sum(candies)
import random

# Generate random ratings list of size 10^5 (max constraint)

large_ratings = [random.randint(-10**9, 10**9) for _ in range(10**5)]
# large_ratings = [1,0,2]
print(candy(large_ratings))