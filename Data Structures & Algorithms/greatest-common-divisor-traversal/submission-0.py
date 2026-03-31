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

        def gcd(a, b):
            while b != 0:
                a, b = b, a%b
            return a
        uf = UnionFind(len(nums))
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if gcd(nums[i], nums[j]) > 1:
                    uf.union(i, j)
        
        return uf.isConnected()





        