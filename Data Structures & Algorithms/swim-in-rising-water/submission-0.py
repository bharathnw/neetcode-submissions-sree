class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        minHeap = [(grid[0][0], 0, 0)]
        minH = 0
        maxH = 0
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visits = set()
        while minHeap:
            height, r, c = heapq.heappop(minHeap)
            minH = min(height, minH)
            maxH = max(height, maxH)
            if r == len(grid) - 1 and c == len(grid[0])-1:
                return maxH -minH 
            for dr, dc in dirs:
                row, col = dr+r, dc+c
                if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or (row, col) in visits:
                    continue
                visits.add((row, col))
                heapq.heappush(minHeap, (grid[row][col], row, col))

        return maxH - minH                
                

