class UnionFind:

    def __init__(self, n):
        self.parents = {}
        self.ranks = {}

        for i in range(n):
            self.parents[i] = i
            self.ranks[i] = 0
    
    def find(self,node):
        if self.parents[node] == node:
            return node
        else:
            self.parents[node] = self.find(self.parents[node])
            return self.parents[node]

    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)
        if p1 == p2:
            return False
        if self.ranks[p1] < self.ranks[p2]:
            self.parents[p1] = p2
        elif self.ranks[p2] < self.ranks[p1]:
            self.parents[p2] = p1
        else:
            self.parents[p1] = p2
            self.ranks[p2] += 1
        

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        uf = UnionFind(len(accounts))

        dic = {}

        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in dic:
                    uf.union(i, dic[email])
                else:
                    dic[email] = i

        emailGroup = defaultdict(list)
        for email, i in dic.items():
            leader = uf.find(i)
            emailGroup[leader].append(email)
        
        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))
        return res









