from collections import deque
class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        q = deque()
        fresh = 0
        rows = len(grid)
        cols = len(grid[0])
        time = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    if dr+r < 0 or dc+c < 0 or dr+r == rows or dc+c == cols or grid[dr+r][dc+c] != 1:
                        continue  
                    grid[dr+r][dc+c] = 2
                    q.append((dr+r, dc+c))
                    fresh -= 1    
            time += 1
        return time if fresh == 0 else -1
              





