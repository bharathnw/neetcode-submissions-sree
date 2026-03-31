class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}

        for i in range(n):
            adj[i] = []

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def cal_height(node):
            q = deque([node])
            visits = set()
            visits.add(node)
            height = 0
            while q:
                size = len(q)
                for _ in range(size):
                    n = q.popleft()
                    for nei in adj[n]:
                        if nei not in visits:
                            q.append(nei)
                            visits.add(nei)
                height += 1
            return height
        
        # counts = []
        # min_height = float('inf')
        # for i in range(n):
        #     h = cal_height(i)
        #     min_height = min(min_height, h)
        #     counts.append(h)
        
        # return [i for i in range(len(counts)) if counts[i] == min_height]
        
        edges_cnt = {}
        leaves = deque()
        for key, val in adj.items():
            if len(val) <= 1:
                leaves.append(key)
            edges_cnt[key] = len(val)
        while leaves:
            if n <= 2:
                return list(leaves)
            for _ in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in adj[node]:
                    edges_cnt[nei] -= 1
                    if edges_cnt[nei] == 1:
                        leaves.append(nei)
        return list(leaves)
