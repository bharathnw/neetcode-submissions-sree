class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {}
        minTimes = {}
        for i in range(1, n+1):
            adjList[i] = []
            minTimes[i] = float('inf')
        
        for u,v,t in times:
            adjList[u].append((t, v))

        res = -float('inf')

        minHeap = []
        for s in adjList[k]:
            heapq.heappush(minHeap, s)
        minTimes[k] = 0
        visits = set()
        while len(minHeap) > 0:
            t, v = heapq.heappop(minHeap)

            if v in visits:
                continue
            visits.add(v)
            minTimes[v] = min(minTimes[v], t)
            
            for time, n2 in adjList[v]:
                heapq.heappush(minHeap,(t+time,n2))
        
        for val in minTimes.values():
            if val == float('inf'):
                return -1
            res = max(val, res)
        return res