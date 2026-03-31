class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visits = set()

        def dfs(node):
            if node in visits:
                return
            visits.add(node)
            for subNode in adj[node]:
                dfs(subNode)
        res = 0
        for item in range(n):
            if item not in visits:
                res += 1
                dfs(item)
        
        return res