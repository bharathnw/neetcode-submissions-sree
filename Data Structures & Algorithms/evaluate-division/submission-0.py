class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adj = defaultdict(list)
        res = []

        for i, (a,b) in enumerate(equations):
            adj[a].append((b, values[i]))
            adj[b].append((a, 1/values[i]))
        
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            q = deque([(src, 1)])
            visits = set(src)

            while q:
                node, w = q.popleft()
                
                if node == target:
                    return w
                
                for nei, weight in adj[node]:
                    if nei not in visits:
                        q.append((nei, weight*w))
                        visits.add(nei)
            return -1
        
        for a, b in queries:
            res.append(bfs(a, b))
        
        return res


