"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current = head
        translate = {}

        while current:
            translate[current] = Node(x=current.val, next=None, random=None)
            current = current.next
        
        current = head
        while current:
            new_next = translate[current.next] if current.next else None
            new_random = translate[current.random] if current.random else None
            translate[current].next = new_next
            translate[current].random = new_random

            current = current.next
        
        return translate[head] if head else None
            
        
