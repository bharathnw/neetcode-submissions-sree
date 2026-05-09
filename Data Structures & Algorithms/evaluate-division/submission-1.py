class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:


        adj = defaultdict(list)

        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            adj[a].append((b, values[i]))
            adj[b].append((a, 1/values[i]))

        visits = set()
        def dfs(src, target):
            if src not in adj or target not in adj:
                return -1
            if src == target:
                return 1
            visits.add(src)
            for nei, w in adj[src]:
                if nei not in visits:
                    res = dfs(nei, target)
                    if res != -1:
                        visits.remove(src)
                        return w * res
            visits.remove(src)
            return -1

        res = []
        for src, target in queries:
            res.append(dfs(src, target))
        
        return res


            

         