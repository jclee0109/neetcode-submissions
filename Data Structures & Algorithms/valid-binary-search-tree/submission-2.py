# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        stack = [(root, False)] # node, visited
        min_max_so_far = {root: (float('inf'), -float('inf'))} # min, max so far

        while stack:
            node, visited = stack.pop()

            if not visited:
                stack.append((node, True))

                if node.left:
                    if node.left.val >= node.val:
                        return False
                    stack.append((node.left, False))
                
                if node.right:
                    if node.right.val <= node.val:
                        return False
                    stack.append((node.right, False))

            
            else: # visited다 (자식노드들 계산 끝났다.)
                if node.left and node.right:
                    if min_max_so_far[node.left][1] >= node.val or min_max_so_far[node.right][0] <= node.val:
                        return False
                    
                    min_max_so_far[node] = (min_max_so_far[node.left][0], min_max_so_far[node.right][1])

                elif node.left:
                    if min_max_so_far[node.left][1] > node.val:
                        return False
                    min_max_so_far[node] = (min_max_so_far[node.left][0], node.val)

                elif node.right:
                    if min_max_so_far[node.right][0] < node.val:
                        return False
                    min_max_so_far[node] = (node.val, min_max_so_far[node.right][1])

                else:
                    min_max_so_far[node] = (node.val, node.val)
        
        return True


