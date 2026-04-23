class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        R = len(grid)
        C = len(grid[0])

        def bfs(r, c):
            q = deque([])
            q.append((r, c))
            visits = set()
            dis = 0
            while q:
                dis += 1
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr = dr+r
                        nc = dc+c
                        if nr < 0 or nc < 0 or nr == R or nc == C or grid[nr][nc] == -1 or grid[nr][nc] == 0 or (nr,nc) in visits:
                            continue
                        grid[nr][nc] = min(grid[nr][nc], dis)
                        visits.add((nr, nc))
                        q.append((nr, nc))

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    bfs(r, c)

        print(grid)
                
                            
        