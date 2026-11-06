# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        if root:
            stack.append(root)

        while stack:
            cur = stack.pop()
            
            left = cur.left
            right = cur.right

            cur.left = right
            cur.right = left

            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
            
        return root

