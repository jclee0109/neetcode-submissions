# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        seen = set()

        while current is not None:
            next = current.next
            if next is None:
                return False
            
            if next in seen:
                return True

            seen.add(next)
            current = next
        
        return False
        