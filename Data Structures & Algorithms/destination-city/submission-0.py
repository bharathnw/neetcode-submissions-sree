class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        if not paths:
            return ''

        adj = {}

        for fr, to in paths:
            adj[fr] = to
        

        def dfs(node):
            if node not in adj:
                return node
            
            return dfs(adj[node])
        
        return dfs(paths[0][0])
