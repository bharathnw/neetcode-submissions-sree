class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        accToIndex = {}

        for index, account in enumerate(accounts):
            for acc in account[1:]:
                if acc in accToIndex:
                    accToIndex[acc].append(index)
                else:
                    accToIndex[acc] = [index]
        
        adjList = defaultdict(list)

        for acc, val in accToIndex.items():
            for index in range(1, len(val)):
                adjList[val[index]].append(val[index-1])
                adjList[val[index-1]].append(val[index])
        
        print(adjList)
        actMap = {}
        visits = set()

        def dfs(node):
            visits.add(node)
            res = set(accounts[node][1:])
            for nei in adjList[node]:
                if nei not in visits:
                    res |= dfs(nei)
            return res

        results = []
        
        for i in range(len(accounts)):
            if i not in visits:
                actMap[i] = dfs(i)
                results.append([accounts[i][0]] + sorted(list(actMap[i])))
        
        return results
        




        