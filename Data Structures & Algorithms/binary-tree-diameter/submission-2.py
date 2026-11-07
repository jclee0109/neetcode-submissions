# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    # stack으로 구현
        if not root:
            return 0
        
        stack = [(root, False)]
        depth = {}
        diameter = 0

        while stack:
            node, visited = stack.pop()

            if not visited:
                stack.append((node, True))

                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
            
            else:
                left_depth = depth.get(node.left, 0)
                right_depth = depth.get(node.right, 0)

                depth[node] = 1 + max(left_depth, right_depth)

                diameter = max(
                    diameter,
                    left_depth + right_depth
                )
        
        return diameter


