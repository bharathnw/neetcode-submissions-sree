class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        adj = defaultdict(list)

        for st, en, dis in roads:
            adj[st].append((en, dis))
            adj[en].append((st, dis))

        res = float('inf')
        visits = set([])

        stack = [1]

        while stack:
            node = stack.pop()
            
            visits.add(node)

            for nei, dis in adj[node]:
                if nei not in visits:
                    res = min(res, dis)
                    stack.append(nei)
        
        return res


        