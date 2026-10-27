class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0

        q = []

        m = len(grid)
        n = len(grid[0])

        heapq.heappush(q, (grid[0][0], 0, 0))

        visited = set()

        while q:
            
            for _ in range(len(q)):

                val, r, c = heapq.heappop(q)

                if r == m-1 and c == n-1:
                    return val

                if (r, c) in visited:
                    continue
                
                visited.add((r, c))
                
                if r + 1 < m and (r + 1, c) not in visited:
                    heapq.heappush(q, (val + grid[r + 1][c], r + 1, c))
                    
                if c + 1 < n and (r, c + 1) not in visited:
                    heapq.heappush(q, (val + grid[r][c + 1], r, c + 1))

        
        return -1
            

