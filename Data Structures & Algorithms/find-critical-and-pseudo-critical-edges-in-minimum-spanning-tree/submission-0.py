class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:


        
        def get_mst(skipEdge=None, includeEdge=None):

            adj = defaultdict(list)
            for i, (u, v, w) in enumerate(edges):
                if i == skipEdge:
                    continue
                adj[u].append((w, v))
                adj[v].append((w, u))
            heap = [(0,0)]
            visits = set()
            mst_weight = 0
            if includeEdge:
                heap = []
                w, u, v = includeEdge
                visits.add(u)
                visits.add(v)
                mst_weight += w
                for neiW, neiNode in adj[u]:
                    if neiNode in visits:
                        continue
                    heapq.heappush(heap, (neiW, neiNode))
                for neiW, neiNode in adj[v]:
                    if neiNode in visits:
                        continue
                    heapq.heappush(heap, (neiW, neiNode))
            
            while heap:
                weight, node = heapq.heappop(heap)
                if node in visits:
                    continue
                visits.add(node)
                mst_weight += weight
                for neiW, neiNode in adj[node]:
                    if neiNode in visits:
                        continue
                    heapq.heappush(heap, (neiW, neiNode))
            if len(visits) != n:
                return float('inf')
            
            return mst_weight
        
        actual_mst = get_mst()
        critical = []
        pseudo = []

        for i, (u, v, w) in enumerate(edges):
            if get_mst(i) > actual_mst:
                critical.append(i)
            elif get_mst(None, (w, u, v)) == actual_mst:
                pseudo.append(i)
        
        return [critical, pseudo]

        


                


        

        