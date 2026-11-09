# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSametree(p, q):
            if not p or not q:
                return p is q
            
            if p.val != q.val:
                return False
            
            return isSametree(p.left, q.left) and isSametree(p.right, q.right)

        if not subRoot:
            return True
        if not root: # subRoot는 None이 아님
            return False

        if isSametree(root, subRoot):
            return True
        
        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )
        
        
        