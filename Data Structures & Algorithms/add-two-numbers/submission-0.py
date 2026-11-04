# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_current = l1
        l2_current = l2
        overhead = 0
        end_dummy = ListNode(val=0, next=None)
        start_dummy = ListNode(val=0, next=None)
        ans = start_dummy

        while l1_current or l2_current or overhead != 0:
            if not l1_current:
                l1_current = end_dummy
            if not l2_current:
                l2_current = end_dummy
            sum_digit = l1_current.val + l2_current.val + overhead
            val = sum_digit%10
            overhead = sum_digit//10

            ans_node = ListNode(val=val, next=None)
            ans.next = ans_node
            ans = ans.next

            l1_current = l1_current.next
            l2_current = l2_current.next
        
        return start_dummy.next