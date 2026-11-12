# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, root.val)]
        cnt = 1

        while stack:
            node, max_num = stack.pop() # max_num은 지금 node까지 거쳐오면서 만났던 가장 큰 수

            if node.left:
                if max_num > node.left.val: # 왼쪽이 더 작을 때
                    stack.append((node.left, max_num))
                else:
                    cnt += 1
                    stack.append((node.left, node.left.val))

            if node.right:
                if max_num > node.right.val:
                    stack.append((node.right, max_num))
                else:
                    cnt += 1
                    stack.append((node.right, node.right.val))
            
        return cnt
