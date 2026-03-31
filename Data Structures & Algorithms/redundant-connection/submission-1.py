class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        for i in range(1, n+1):
            self.parent[i] = i
            self.rank[i] = 1
    
    def findParent(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

        
    def union(self, u, v):
        uParent = self.findParent(u)
        vParent = self.findParent(v)
        if uParent == vParent:
            return False
        if self.rank[uParent] > self.rank[vParent]:
            self.parent[vParent] = uParent
        elif self.rank[uParent] < self.rank[vParent]:
            self.parent[uParent] = vParent
        else:
            self.parent[uParent] = vParent
            self.rank[vParent] += 1

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges)+1)
        for u, v in edges:
            if uf.union(u,v) == False:
                return [u, v]


        