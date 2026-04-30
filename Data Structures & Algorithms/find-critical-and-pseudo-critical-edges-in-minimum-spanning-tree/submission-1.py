class UnionFind:

    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        self.components = 0
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0
    
    def find(self, node):
        par = self.parent[node]
        while par != self.parent[par]:
            self.parent[par] = self.parent[self.parent[par]]
            par = self.parent[par]
        return par
    
    def union(self, u, v):
        p1 = self.find(u)
        p2 = self.find(v)
        if p1 == p2:
            return False
        self.components += 1
        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        elif self.rank[p2] < self.rank[p1]:
            self.parent[p2] = p1
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        for i in range(len(edges)):
            edges[i].append(i)

        edges.sort(key=lambda x: x[2])
        critical, pseudo = [], []
        mst_weight = 0
        uf = UnionFind(n)
        for a, b, w, _ in edges:
            if uf.union(a, b):
                mst_weight += w
        
        for a, b, w, i in edges:
            uf = UnionFind(n)
            skipped_wt = 0
            for i_a, i_b, i_w, i_i in edges:
                if i_i != i:
                    if uf.union(i_a, i_b):
                        skipped_wt += i_w
            if skipped_wt > mst_weight or uf.components < n-1:
                critical.append(i)
                continue
            uf = UnionFind(n)
            uf.union(a, b)
            included_wt = w
            for i_a, i_b, i_w, i_i in edges:
                if i_i != i:
                    if uf.union(i_a, i_b):
                        included_wt += i_w
            if included_wt == mst_weight:
                pseudo.append(i)
        
        return [critical, pseudo]
        