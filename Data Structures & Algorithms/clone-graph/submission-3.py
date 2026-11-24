"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        root = Node(node.val, [])
        nodes = {node.val : root} # node_val(int): node(class Node)
        visited = set([node.val])
        queue = deque([node])

        while queue:
            node = queue.popleft()
            
            for neighbor in node.neighbors:
                if neighbor.val not in nodes:
                    new_node = Node(neighbor.val, []) # 새로만들고
                    nodes[neighbor.val] = new_node # 사전에 등록
                    nodes[node.val].neighbors.append(new_node) # 이웃 연결
                else:
                    nodes[node.val].neighbors.append(nodes[neighbor.val]) # 이웃 연결

                if neighbor.val not in visited:
                    visited.add(neighbor.val)
                    queue.append(neighbor)

        return root