class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid:
            return -1

        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        timer = 0
        while fresh > 0 and len(q) > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                    if not (dr+r < 0 or dc+c < 0 or dr+r == ROWS or dc+c == COLS) and grid[dr+r][dc+c] == 1:
                        grid[dr+r][dc+c] = 2
                        fresh -= 1
                        q.append((dr+r,dc+c))
            timer += 1
        return timer if fresh == 0 else -1
        