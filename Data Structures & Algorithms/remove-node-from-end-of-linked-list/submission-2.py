# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        fast = dummy
        slow = dummy

        # fast가 n+1번째 앞에 있으면 slow를 바로 삭제하면 됨
        for _ in range(n+1):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        prev = slow
        current = slow.next
        next_node = slow.next.next # n>=1 (fast가 n+1칸 >= 2칸 이상은 앞서있음)

        prev.next = next_node
        return dummy.next


