class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(list)
        totCnt = n
        for src, target, time in times:
            adj[src].append((time, target))
        
        visits = set()
        visits.add(k)
        n = n -1
        heap = []
        for node in adj[k]:
            heapq.heappush(heap, node)

        while heap:
            minItem = heapq.heappop(heap)
            time, target = minItem
            if target in visits:
                continue
            n -= 1
            if n == 0:
                return time
            visits.add(target)
            for item_t, item_target in adj[target]:
                heapq.heappush(heap, (time+item_t, item_target))
        
        return -1
            
            

        


