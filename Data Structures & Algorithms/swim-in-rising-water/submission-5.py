class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0

        heap = []

        heapq.heappush(heap,(grid[0][0], (0, 0)))

        minVal, maxVal = 0, 0

        visits = set()

        while heap:
            item = heapq.heappop(heap)
            minVal = min(item[0], minVal)
            maxVal = max(item[0], maxVal)
            
            r, c = item[1]

            if r == len(grid)-1 and c == len(grid[0])-1:
                return maxVal - minVal

            for nr, nc in [(0,1), (1,0), (-1,0), (0,-1)]: 
                dr, dc = nr+r, nc+c
                if dr < 0 or dc < 0 or dr == len(grid) or dc == len(grid[0]) or (dr,dc) in visits:
                    continue
                visits.add((dr,dc))
                heapq.heappush(heap, (grid[dr][dc], (dr, dc)))
        
        return maxVal-minVal
                                   
