class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adj = defaultdict(list)

        for src, des in sorted(tickets, reverse=True):
            adj[src].append(des)
        
        if 'JFK' not in adj:
            return []
        res = []
        
        def dfs(node):
            while adj[node]:
                nxt = adj[node].pop()
                dfs(nxt)
            res.append(node)
        dfs('JFK')
        return res[::-1]
        
        


        