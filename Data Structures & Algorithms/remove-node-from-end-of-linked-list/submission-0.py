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
        
        prev = None
        current = head
        cnt = 0

        while current:
            if cnt == total - n:
                next_node = current.next
                if prev:
                    prev.next = next_node
                    return head
                else:
                    current.next = None
                    return next_node
                break

            prev = current
            current = current.next

            cnt += 1
        
        
            