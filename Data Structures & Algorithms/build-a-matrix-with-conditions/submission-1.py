class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        rowAdj = defaultdict(list)
        colAdj = defaultdict(list)

        for row in rowConditions:
            rowAdj[row[0]].append(row[1])

        for col in colConditions:
            colAdj[col[0]].append(col[1])

        visited = set()
        visiting = set()
        res = []
        def dfs(node, adj):
            if node in visiting:
                return False
            if node in visited:
                return True
            visiting.add(node)
            visited.add(node)
            for nei in adj[node]:
                if not dfs(nei, adj):
                    return False
            visiting.remove(node)
            res.append(node)
            return True
        sol = [[0] * k for _ in range(k)]

        for src in range(1, k+1):
            if src not in visited:
                if not dfs(src, rowAdj):
                    return []
        rowOrder = {}
        for i, num in enumerate(reversed(res)):
            rowOrder[num] = i

        visited = set()
        visiting = set()
        res = []

        for src in range(1, k+1):
            if src not in visited:
                if not dfs(src, colAdj):
                    return []

        colOrder = {}
        for i, num in enumerate(reversed(res)):
            colOrder[num] = i
        
        for num in range(1, k+1):
            r, c = rowOrder[num], colOrder[num]
            sol[r][c] = num
        
        return sol

        

