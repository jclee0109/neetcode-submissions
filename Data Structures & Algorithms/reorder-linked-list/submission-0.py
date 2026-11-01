# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        node = head

        while node:
            arr.append(node)
            node = node.next
        
        for i in range((len(arr)-1)//2 + 1):
            current = arr[i]
            next_node = arr[len(arr)-1-i]

            if i == len(arr)-1-i:
                current.next = None
                break
            
            current.next = next_node

            if i == (len(arr)-1)//2:
                next_node.next = None
            else:
                next_node.next = arr[i+1]
                
