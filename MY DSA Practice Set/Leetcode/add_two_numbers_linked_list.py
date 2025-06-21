'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

📊 Time and Space Complexity
Metric	Value
Time	O(max(N, M))
Space	O(max(N, M))
Where N and M are lengths of l1 and l2.
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        dummy_head = ListNode()
        current = dummy_head
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10) 
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy_head.next
    
# Practice
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumber(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        dummy_head = ListNode()
        current = dummy_head
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy_head.next
# ✅ Helper to convert list → linked list
def build_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next
# ✅ Helper to print linked list
def print_linked_list(node):
    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    print(" → ".join(result))

# Build input linked lists
l1 = build_linked_list([2,4,3])
l2 = build_linked_list([5,6,4])

# Call and print result
sol = Solution()
result = sol.addTwoNumber(l1, l2)
print_linked_list(result)  # Output: 7 → 0 → 8
