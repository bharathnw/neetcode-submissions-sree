class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights:
            return 0
        minHeap = []
        visits = set()
        #distance, row, col
        heapq.heappush(minHeap, (0, (0,0)))


        while minHeap:
            currDis, (row, col) = heapq.heappop(minHeap)

            if row == (len(heights)-1) and col == (len(heights[0])-1):
                return currDis

            if (row, col) in visits:
                continue

            visits.add((row, col))

            for r, c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:

                dr = row + r
                dc = col + c
                if dr < 0 or dc < 0 or dr == len(heights) or dc == len(heights[0]) or (dr,dc) in visits:
                    continue
                
                dis = max(abs(heights[dr][dc] - heights[row][col]), currDis)
      
                heapq.heappush(minHeap, (dis, (dr, dc)))
        return 0

