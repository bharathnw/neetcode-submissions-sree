class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {}
        for i in range(1, n+1):
            adjList[i] = []
        
        for u,v,t in times:
            adjList[u].append((t, v))

        res = -float('inf')

        minHeap = [(0, k)]

        visits = set()
        while len(minHeap) > 0:
            t, v = heapq.heappop(minHeap)
            if v in visits:
                continue
            res = t
            visits.add(v)

            for time, n2 in adjList[v]:
                heapq.heappush(minHeap,(t+time,n2))

        return -1 if len(visits) != n else res