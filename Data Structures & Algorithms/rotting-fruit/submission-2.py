class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        time = 0

        q = deque([])

        fresh = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        while q and fresh > 0:
            time += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = dr+r, dc+c
                    if nr < 0 or nc < 0 or nr == len(grid) or nc == len(grid[0]) or grid[nr][nc] != 1:
                        continue
                    fresh -= 1
                    grid[nr][nc] = 2
                    q.append((nr, nc))
        
        if fresh > 0:
            return -1
        else:
            return time
                    
                    

