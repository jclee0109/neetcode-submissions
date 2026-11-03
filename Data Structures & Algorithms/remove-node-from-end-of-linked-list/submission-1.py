# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        total = 0

        while current:
            total += 1
            current = current.next
        
        target = total-n
        prev = None
        current = head
        idx = 0

        while current:
            if idx == target:
                next_node = current.next

                if not prev:
                    return next_node

                prev.next = next_node
                return head

            prev = current
            current = current.next

            idx += 1

        return head        
        
            