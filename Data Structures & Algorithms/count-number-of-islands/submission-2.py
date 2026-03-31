class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        def bfs(r, c):
            q = deque([(r, c)])
            dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            while q:
                row, col = q.popleft()
                grid[row][col] = '0'
                for dr, dc in dirs:
                    if (dr+row) < 0 or (dr + row) == len(grid) or (dc+col) < 0 or (dc+col) == len(grid[0]):
                        continue
                    if grid[dr+row][dc+col] == '1':
                        q.append((dr+row, dc+col))
        res = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    bfs(i, j)
                    res += 1
        return res 
                


        