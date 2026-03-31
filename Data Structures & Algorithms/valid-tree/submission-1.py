class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodes = {}
        for i in range(n):
            nodes[i] = set()

        for u, v in edges:
            nodes[u].add(v)
            nodes[v].add(u)
        
        visits = set()
        def dfs(node, parent):
            if node in visits:
                return False
            visits.add(node)
            for u in nodes[node]:
                if u == parent:
                    continue
                if dfs(u, node) == False:
                    return False
            return True
        
        return dfs(0, -1) and len(visits) == n
        