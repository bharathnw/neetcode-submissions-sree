class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        self.comp = n

        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0
    
    def find(self, node):
        parent = self.parent[node]
        while parent != self.parent[parent]:
            self.parent[parent] = self.parent[self.parent[parent]]
            parent = self.parent[parent]
        return parent
    
    def union(self, u, v):
        p1 = self.find(u)
        p2 = self.find(v)
        if p1 == p2:
            return False
        self.comp -= 1
        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        elif self.rank[p2] < self.rank[p1]:
            self.parent[p2] = p1
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        return True
    
    def getComponents(self):
        return self.comp - 1

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        uf = UnionFind(n)

        for u, v in edges:
            if uf.union(u, v) == False:
                return False
        
        return uf.getComponents() == 0
        

        