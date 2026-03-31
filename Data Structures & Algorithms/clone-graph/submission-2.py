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
            return None

        mapper = {}

        def dfs(n):
            if not n:
                return None
            if n in mapper:
                return mapper[n]
            mapper[n] = Node(n.val)
            for nei in n.neighbors:
                mapper[n].neighbors.append(dfs(nei))
            return mapper[n]
        
        return dfs(node)