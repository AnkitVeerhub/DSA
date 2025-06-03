'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Note: For brute force, we will not focus on the time constraint yet.
'''
'''
 Interview-Style Explanation:
“Even though methods like top() and getMin() are intended to return integers,
I include a check for an empty stack to avoid runtime exceptions such as IndexError.
This is a defensive approach to ensure robustness in edge cases.”
'''
class MinStack:
    def __init__(self):
        # Primary Stack to store the elements
        self.stack = []
    def push(self, val: int) -> None:
        # Insert element at the top of the stack
        self.stack.append(val)
    def pop(self) -> None:
        if self.stack:
            # Remove the top most element
            self.stack.pop()
    def top(self) -> int:
        if self.stack:
            # Return the element at the top without removing it
            return self.stack[-1]
        return None
    def getMin(self):
        if self.stack:
            # Return the minimum element by scanning the entire stack
            return min(self.stack)
        return None
min_stack = MinStack()
min_stack.push(3)
min_stack.push(5)
print(min_stack.getMin())  # Output: 3
min_stack.push(2)
min_stack.push(1)
print(min_stack.getMin())  # Output: 1
min_stack.pop()
print(min_stack.getMin())  # Output: 2
print(min_stack.top())     # Output: 2

# Optimal Approach
class NimStack:
    def __int__(self):
        self.stack = []
        self.min_Stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push to min_Stack if empty or val <= current minimum
        if not self.min_Stack or val <= self.min_Stack[-1]:
            self.min_Stack.append(val)
    # Pop the top element from the main stack.
    # If the popped value is equal to the current minimum (top of min_stack),
    # also pop from the min_stack to keep both stacks in sync.
    # This ensures getMin() always reflects the correct minimum after a pop.


    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.min_Stack[-1]:
                self.min_Stack.pop()
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None
    def getMin(self) -> int:
        if self.min_Stack:
            return self.min_Stack[-1]
        return None
min_stack = MinStack()
min_stack.push(3)
min_stack.push(5)
print(min_stack.getMin())  # 3
min_stack.push(2)
min_stack.push(1)
print(min_stack.getMin())  # 1
min_stack.pop()
print(min_stack.getMin())  # 2
print(min_stack.top())     # 2
min_stack.pop()
print(min_stack.getMin())  # 3
