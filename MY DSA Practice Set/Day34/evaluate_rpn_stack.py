'''
Problem Description

An arithmetic expression is given by a string array A of size N. Evaluate the value of an arithmetic expression in Reverse Polish Notation.


Valid operators are +, -, *, /. Each string may be an integer or an operator.

Note: Reverse Polish Notation is equivalent to Postfix Expression, where operators are written after their operands.



Problem Constraints

1 <= N <= 10^5

Example Input

Input 1:
A =   ["2", "1", "+", "3", "*"]
Input 2:
A = ["4", "13", "5", "/", "+"]


Example Output

Output 1:
9
Output 2:
6


Example Explanation

Explaination 1:
starting from backside:
    * : () * ()
    3 : () * (3)
    + : (() + ()) * (3)
    1 : (() + (1)) * (3)
    2 : ((2) + (1)) * (3)
    ((2) + (1)) * (3) = 9
Explaination 2:
starting from backside:
    + : () + ()
    / : () + (() / ())
    5 : () + (() / (5))
    13 : () + ((13) / (5))
    4 : (4) + ((13) / (5))
    (4) + ((13) / (5)) = 6
'''

# Brute force Approach
def evaluate_rpn_bruteforce(A):
    while len(A) > 1:
        for i in range(len(A)):
            if A[i] in "+-*/":
                operand1 = int(A[i-2])
                operand2 = int(A[i-1])
                operator = A[i]

                if operator == "+":
                    result = operand1 + operand2
                elif operator == "-":
                    result = operand1 - operand2
                elif operator == "*":
                    result = operand1 * operand2
                elif operator == "/":
                    result = int(operand1 / operand2)

                A = A[:i-2] + [str(result)] + A[i+1:]
                break
    return int(A[0])
A =   ["2", "1", "+", "3", "*"]
A = ["4", "13", "5", "/", "+"]
print(evaluate_rpn_bruteforce(A))

# Using Stack optimal
class Solution:
    def evalRPN(self, A):
        stack = []
        for token in A:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # Ensure truncation towards 0 like in Python int division
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]
obj = Solution()
A =   ["2", "1", "+", "3", "*"]
A = ["4", "13", "5", "/", "+"]
print(obj.evalRPN(A))