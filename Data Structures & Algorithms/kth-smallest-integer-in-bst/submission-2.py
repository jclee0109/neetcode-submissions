# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # node, visited
        stack = [(root, False)]
        num = {}
        i = 0

        while stack:
            node, visited = stack.pop()
            
            if not visited:
                stack.append((node, True))

                if node.left:
                    stack.append((node.left, False))
                
                if node.right:
                    stack.append((node.right, False))
            
            if visited:
                if not node.left and not node.right:
                    num[node] = (0, 0)
                    continue
                
                left_total = 0
                right_total = 0

                if node.left:
                    left = num.get(node.left, (0,0))
                    left_total = left[0]+left[1]+1
                
                if node.right:
                    right = num.get(node.right, (0,0))
                    right_total = right[0]+right[1]+1

                num[node] = (left_total, right_total)

        while node:
            left_total, right_total = num[node]
            
            if left_total+1 == k:
                return node.val
            
            elif left_total+1 < k:
                node = node.right
                k -= (left_total+1)
            
            else:
                node = node.left
        
        return None


            