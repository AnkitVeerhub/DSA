
'''
Problem Description

Given an expression string A, examine whether the pairs and the orders of “{“,”}”, ”(“,”)”, ”[“,”]” are correct in A.

Refer to the examples for more clarity.



Problem Constraints

1 <= |A| <= 100
'''

# validate_balanced_parentheses_bruteforce.py
def is_balanced_bruteforce(expression):
    if not expression:
        return True
    prev_length = -1
    while prev_length != len(expression):
        prev_length = len(expression)
        expression = expression.replace('()', "")
        expression = expression.replace('[]', "")
        expression = expression.replace('{}', "")
    return len(expression) == 0
print(is_balanced_bruteforce("[({}})]"))

# Another bruteforce approach using nested for loop

def isBalanced(A):
    bracket = list(A)
    pairs = {'{':'}','[':']','(':')'}
    while True:
        found = False
        i = 0
        while i < len(bracket) - 1:
            if bracket[i] in pairs and bracket[i+1] == pairs[bracket[i]]:
                bracket.pop(i+1)
                bracket.pop(i)
                found = True
                i = 0
            else:
                i+=1
        if not found:
            break
    return len(bracket) == 0
print(isBalanced("[{())[{[]}])}]"))


# Using stack
# Optimal Approach

def is_balanced_stack(A):
    stack = []
    pairs = {'(':')','[':']','{':'}'}
    for char in A:
        if char in pairs:
            stack.append(char)
        else:
            if not stack:
                return False
            top = stack.pop()
            if pairs[top] != char:
                return False
    return len(stack) == 0
print(is_balanced_stack("[{{((((([[[[{{{}}}}}]]]])))))}}]"))



def isBalanced(A):
    bracket = list(A)
    pairs = {'{': '}', '[': ']', '(': ')'}

    print("Initial expression:", "".join(bracket))
    step = 1

    while True:
        found = False
        i = 0
        while i < len(bracket) - 1:
            print(f"Step {step}: Checking {bracket[i]} and {bracket[i+1]}")
            if bracket[i] in pairs and bracket[i+1] == pairs[bracket[i]]:
                print(f"Removing pair: {bracket[i]}{bracket[i+1]} at index {i}")
                bracket.pop(i+1)
                bracket.pop(i)
                found = True
                print("  Current bracket list:", "".join(bracket))
                i = 0
                step += 1
            else:
                i += 1
        if not found:
            print("No more pairs found.")
            break

    if len(bracket) == 0:
        print("✅ Expression is balanced")
    else:
        print("❌ Expression is not balanced. Unmatched brackets left:", "".join(bracket))

    return len(bracket) == 0

# Test
isBalanced("[{([{[]}])}]")        # ✅ Balanced
isBalanced("[{{((((([[[[{{{}}}}}]]]])))))}}]")       # ❌ Not balanced (added error)
