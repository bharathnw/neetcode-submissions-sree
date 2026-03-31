class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        if not heights:
            return 0
        visits = set()

        heap = []
        
        heapq.heappush(heap, (0,0,0))

        while heap:
            val, r, c = heapq.heappop(heap)
            if r == len(heights)-1 and c == len(heights[0]) -1:
                return val
            if (r,c) in visits:
                continue
            visits.add((r, c))

            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dr, dc in dirs:
                if (dr+r, dc+c) in visits or dr+r < 0  or dc+c < 0 or dr+r == len(heights) or dc+c == len(heights[0]):
                    continue

                heapq.heappush(heap, (max(abs(heights[r][c]-heights[dr+r][dc+c]), val), dr+r, dc+c)) 

        return -1

        