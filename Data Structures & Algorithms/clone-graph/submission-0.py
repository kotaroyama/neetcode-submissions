"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        hash_map = {}
        visited = set()

        def dfs(node):
            if node in visited:
                return

            new_node = Node(val=node.val)
            visited.add(node)
            hash_map[node] = new_node
            for neighbor in node.neighbors:
                 dfs(neighbor)
                 new_node.neighbors.append(hash_map[neighbor])
            
            return new_node

        return dfs(node)
