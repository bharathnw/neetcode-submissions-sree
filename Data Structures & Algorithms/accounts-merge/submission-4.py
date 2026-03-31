class UnionFind:
    
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 1
    
    def findParent(self, node):
        p = self.parent[node]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, u, v):
        p1, p2 = self.findParent(u), self.findParent(v)
        if p1 == p2:
            return False
        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        elif self.rank[p2] < self.rank[p1]:
            self.parent[p2] = p1
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        accToIndex = {}

        uf = UnionFind(len(accounts))

        for index, account in enumerate(accounts):
            for acc in account[1:]:
                if acc in accToIndex:
                    uf.union(index, accToIndex[acc])
                else:
                    accToIndex[acc] = index
        
        adjList = defaultdict(list)

        for acc, val in accToIndex.items():
            leader = uf.findParent(val)
            adjList[leader].append(acc)

        results = []

        for i, emails in adjList.items():
            results.append([accounts[i][0]] + sorted(emails))

        return results
        




        