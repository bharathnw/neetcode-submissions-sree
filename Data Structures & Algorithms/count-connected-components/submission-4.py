class UnionFind:
    def __init__(self, n):
        self.size = n
        self.par = {}
        self.rank = {}
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, node):
        par = self.par[node]
        while par != self.par[par]:
            par = self.par[par]
        
        return par
    
    def union(self, u, v):
        p1 = self.find(u)
        p2 = self.find(v)
        if p1 == p2:
            return False
        self.size -= 1
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        elif self.rank[p2] < self.rank[p1]:
            self.par[p2] = p1
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        return True
    
    def get_size(self):
        return self.size


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        uf = UnionFind(n)


        for u, v in edges:
            uf.union(u, v)

        return uf.get_size()