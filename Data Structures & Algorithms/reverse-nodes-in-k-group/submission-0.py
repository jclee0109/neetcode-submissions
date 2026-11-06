# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack = deque()
        i = 0
        
        dummy = ListNode(val=0, next=head)
        node = dummy.next
        tail = dummy

        while node:
            stack.append(node)
            next_node = node.next

            if len(stack) == k:
                while stack:
                    current = stack.pop()
                    tail.next = current  
                    tail = current
                tail.next = next_node
            node = next_node

        while stack:
            current = stack.popleft()
            tail.next = current
            tail = current

        return dummy.next

        
        
