# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        candid1 = list1
        candid2 = list2

        if candid1.val > candid2.val :
            head = candid2
            if candid2.next is None:
                candid2.next = candid1
                return head
            candid2 = candid2.next
        else:
            head = candid1
            if candid1.next is None:
                candid1.next = candid2
                return head
            candid1 = candid1.next
        current = head

        while candid1 is not None and candid2 is not None:    
            if candid1.val <= candid2.val:
                current.next = candid1
                if candid1.next is not None:
                    current = candid1
                    candid1 = candid1.next
                else:
                    candid1.next = candid2
                    break
            else:
                current.next = candid2             
                if candid2.next is not None:
                    current = candid2
                    candid2 = candid2.next
                else:
                    candid2.next = candid1
                    break
        
        return head


