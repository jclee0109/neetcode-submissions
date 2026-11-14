# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # bfs (Queue)
        queue = deque([root])
        nodes = []

        while queue:
            node = queue.popleft()
            if node:
                nodes.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                nodes.append(None)
        
        for node in reversed(nodes):
            if node is None:
                nodes.pop()
            else:
                break
        
        ans = ''
        for node in nodes:
            if node is None:
                ans += "null"
            else:
                ans += str(node)
            
            ans+=","
        print(ans[:-1])
        return ans[:-1]
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(',')
        tree_nodes = []
        for i in range(len(nodes)):
            if nodes[i] == 'null':
                tree_nodes.append(None)
            else:
                tree_nodes.append(TreeNode(val=nodes[i], left=None, right=None))
        print(list(map(lambda x: x.val if x else None, tree_nodes)))
        null_cnt = 0
        for i in range(len(tree_nodes)):
            tree_node = tree_nodes[i]
            if tree_node is None:
                null_cnt += 1
                continue

            left_idx = 2*(i-null_cnt) + 1
            right_idx = 2*(i-null_cnt) + 2

            if not(left_idx >= len(nodes) or tree_nodes[left_idx] is None):
                tree_node.left = tree_nodes[left_idx]

            if not(right_idx >= len(nodes) or tree_nodes[right_idx] is None):
                tree_node.right = tree_nodes[right_idx]

        return tree_nodes[0]
                
