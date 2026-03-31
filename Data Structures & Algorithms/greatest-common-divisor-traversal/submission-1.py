class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.size = {}
        for i in range(n):
            self.parent[i] = i
            self.size[i] = 0
    
    def find(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node
    
    def union(self, u, v):
        p1 = self.find(u)
        p2 = self.find(v)
        if p1 == p2:
            return False
        if self.size[p1] > self.size[p2]:
            self.parent[p2] = p1
        elif self.size[p1] < self.size[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.size[p1] += 1 
        return True

    def isConnected(self):
        root = self.find(0)
        for i in self.parent:
            if self.find(i) != root:
                return False
        return True

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:

        uf = UnionFind(len(nums))
        
        factors = {}
        for i, num in enumerate(nums):
            f = 2
            while f*f <= num:
                if num % f == 0:
                    if f in factors:
                        uf.union(i, factors[f])
                    else:
                        factors[f] = i
                    while num % f == 0:
                        num = num // f
                f += 1
            if num > 1:
                if num in factors:
                    uf.union(factors[num], i)
                else:
                    factors[num] = i
            
        return uf.isConnected()