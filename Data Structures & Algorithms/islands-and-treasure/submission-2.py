class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        R = len(grid)
        C = len(grid[0])
        treasure_q = deque()
        INF = (1<<31) -1
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    grid[i][j] = INF
                    treasure_q.append((0, (i, j)))
        
        while len(treasure_q) > 0:
            for _ in range(len(treasure_q)):
                dis, cords = treasure_q.popleft()
                r, c = cords
                if r < 0 or c < 0 or r == R or c == C or grid[r][c] != INF:
                    continue
                grid[r][c] = dis
                treasure_q.append((dis+1, (r+1, c)))
                treasure_q.append((dis+1, (r-1, c)))
                treasure_q.append((dis+1, (r, c+1)))
                treasure_q.append((dis+1, (r, c-1)))
    
        
