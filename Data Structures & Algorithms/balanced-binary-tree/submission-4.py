# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left = depth(node.left)
            right = depth(node.right)

            if left == -1 or right == -1 or abs(left - right) >= 2:
                return -1

            return max(left, right) + 1

        if not root:
            return True

        left = depth(root.left)
        right = depth(root.right)

        if left == -1 or right == -1 or abs(left-right) >= 2:
            return False
        return True