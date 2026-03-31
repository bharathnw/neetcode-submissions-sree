class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}

        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0
    
    def find(self, node):
        if node == self.parent[node]:
            return node
        else:
            self.parent[node] = self.find(self.parent[node])
            return self.parent[node]
    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)
        if p1 == p2:
            return False
        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        elif self.rank[p2] < self.rank[p1]:
            self.parent[p2] = p1
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        uf = UnionFind(n)
        res = set()
        for x,y in edges:
            uf.union(x,y)

        for i in range(n):
            res.add(uf.find(i))
        
        return len(res)
        
        