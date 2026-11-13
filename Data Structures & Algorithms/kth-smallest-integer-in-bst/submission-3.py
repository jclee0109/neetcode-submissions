# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root
        cnt = 0

        while True:
            while node:
                stack.append(node)
                node = node.left

            # left node
            node = stack.pop()
            cnt += 1

            if cnt == k:
                return node.val

            node = node.right



