class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)

        adj = defaultdict(list)
        
        visits = set()

        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                adj[i].append((j, abs(x1-x2) + abs(y1-y2)))
                adj[j].append((i, abs(x1-x2) + abs(y1-y2)))
        
        heap = [(0, 0)]
        res = 0
        while n > 0:
            dis, index = heapq.heappop(heap)
            if index in visits:
                continue
            visits.add(index)
            n -= 1
            res += dis
            for itemI, itemD in adj[index]:
                heapq.heappush(heap, (itemD, itemI))

        return res


        
        