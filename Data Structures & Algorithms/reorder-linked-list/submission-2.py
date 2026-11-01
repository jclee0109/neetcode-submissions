# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None
            
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l2 = slow.next
        slow.next = None

        # 뒤 절반 reverse
        prev = None
        while l2:
            next_node = l2.next
            l2.next = prev
            prev = l2
            l2 = next_node
        
        l2 = prev
        l1 = head


        while l2:
            l1_next = l1.next
            l2_next = l2.next

            l1.next = l2
            l2.next = l1_next

            l1 = l1_next
            l2 = l2_next

        return None        