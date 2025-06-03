'''
Problem Description
Given an integer A. Find the list of all prime numbers in the range [1, A].
Problem Constraints
1 <= A <= 106
'''
# Brute force approach
class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        # Use list comprehension with helper function to check prime
        return [i for i in range(2, A+1) if self.is_Prime(i)]
    # Helper function to check if a number is prime
    def is_Prime(self, n):
        # Numbers less than or equal to 1 are not prime
        if n <= 1:
            return False
        # Check divisibility from 2 up to sqrt(n)
        for i in range(2, int(n**0.5)+1):
            # Found a divisor, not prime
            if n % i == 0:
                return False
        # No divisors found, it is prime
        return True
A = 10
sol = Solution()        # Create an object of Solution
print(sol.solve(A))