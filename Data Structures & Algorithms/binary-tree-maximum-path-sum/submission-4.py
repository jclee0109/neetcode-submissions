# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        stack = [(root, False)] # node, visited
        path_sum = {} # node: (oneway, max_so_far)

        while stack:
            node, visited = stack.pop()

            if not visited:
                stack.append((node, True))
            
                if node.left:
                    stack.append((node.left, False))
                
                if node.right:
                    stack.append((node.right, False))
            
            else: # visited
                if not node.left and not node.right:
                    oneway = node.val
                    max_so_far = node.val
                    path_sum[node] = (oneway, max_so_far)
                    continue
                left = path_sum.get(node.left, (-float('inf'), -float('inf')))
                right = path_sum.get(node.right, (-float('inf'), -float('inf')))

                left_oneway = max(left[0], 0)
                right_oneway = max(right[0], 0)

                if left_oneway > right_oneway:
                    oneway_max = left_oneway+node.val
                    twoway_include = oneway_max + right_oneway
                else:
                    oneway_max = right_oneway+node.val
                    twoway_include = oneway_max + left_oneway
                    
                twoway_not_include = max(left[1], right[1])
                twoway = max(twoway_include, twoway_not_include)
                path_sum[node] = (oneway_max, max(max_so_far, twoway))
        
        return path_sum[root][1]
        