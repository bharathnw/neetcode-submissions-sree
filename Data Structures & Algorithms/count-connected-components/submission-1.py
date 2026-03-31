class UnionFind:
    def __init__(self, n):
        self.rank = {}
        self.parent = {}
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n]) 
        return self.parent[n]

    def union(self, n1, n2):
        par1 = self.find(n1)
        par2 = self.find(n2)

        if par1 == par2:
            return False
        if self.rank[par1] < self.rank[par2]:
            self.parent[par1] = par2
        elif self.rank[par1] > self.rank[par2]:
            self.parent[par2] = par1
        else:
            self.parent[par2] = par1
            self.rank[par1] += 1
        return True



class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union = UnionFind(n)
        res = n
        for n1, n2 in edges:
            if union.union(n1,n2):
                res -= 1
        
        return res
             
        