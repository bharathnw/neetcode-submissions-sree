class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        cords = {}
        prev = points[0]
        N = len(points)
        for i in range(N):
            cords[tuple(points[i])] = []
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dis = abs(x1-x2) + abs(y1-y2)
                cords[tuple(points[i])].append((dis, points[j]))
                cords[tuple(points[j])].append((dis, points[i]))
        
        heap = [(0,points[0])]
        visits = set()
        res = 0
        while len(visits) < N:
            dis, point = heapq.heappop(heap)
            if tuple(point) in visits:
                continue
            visits.add(tuple(point))
            res += dis
            for adjDis, adjPoint in cords[tuple(point)]:
                if tuple(adjPoint) not in visits:
                    heapq.heappush(heap, (adjDis, adjPoint))
        return res





