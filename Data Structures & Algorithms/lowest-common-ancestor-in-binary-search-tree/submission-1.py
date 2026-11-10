# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return False
        
        parents = {}
        queue = deque()
        queue.append(root)

        p_flag = False
        q_flag = False

        while queue:
            node = queue.popleft()
            
            left = node.left
            right = node.right

            if left:
                parents[left] = node
                queue.append(left)
            if right:
                parents[right] = node
                queue.append(right)
            
            if left is p or right is p:
                p_flag = True
            
            if left is q or right is q:
                q_flag = True
            
            if p_flag and q_flag:
                break
        
        p_parents = set([root])

        while p is not root:
            p_parents.add(p)
            p = parents[p]

        while q is not root:
            if q in p_parents:
                return q
            
            q = parents[q]

        return p
            



