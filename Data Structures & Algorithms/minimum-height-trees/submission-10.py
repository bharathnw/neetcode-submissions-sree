class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = {}
        edges_map = {}
        for i in range(n):
            adj[i] = []
        
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        leaves = deque()
        for key in adj.keys():
            leaves_cnt = len(adj[key])
            edges_map[key] = leaves_cnt
            if leaves_cnt == 1:
                leaves.append(key)

        rem = n

        while leaves and rem > 2:

            for _ in range(len(leaves)):
                node = leaves.popleft()
                rem -= 1
                for nei in adj[node]:
                    edges_map[nei] -= 1
                    if edges_map[nei] == 1:
                        leaves.append(nei)
        
        return list(leaves)
    
