# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        depth = {root: 0}

        current_depth = 0
        ans = []
        tmp = []

        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
                depth[node.left] = depth[node] + 1
            if node.right:
                queue.append(node.right)
                depth[node.right] = depth[node] + 1

            if depth[node] == current_depth:
                tmp.append(node.val)
            
            if depth[node] > current_depth:
                ans.append(tmp)
                tmp = [node.val]
                current_depth += 1
        
        ans.append(tmp)

        return ans
                


        