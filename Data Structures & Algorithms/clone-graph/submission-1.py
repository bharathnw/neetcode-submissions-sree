"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        clonedGraph = {}

        def dfs(n):
            if n in clonedGraph:
                return clonedGraph[n]
            new = Node(n.val)
            clonedGraph[n] = new 
            for neigh in n.neighbors:
                new.neighbors.append(dfs(neigh))
            return clonedGraph[n]
        return dfs(node) if node else None
            
        

