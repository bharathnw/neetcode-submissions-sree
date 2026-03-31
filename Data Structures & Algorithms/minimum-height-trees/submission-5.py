class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}

        for i in range(n):
            adj[i] = []

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

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
