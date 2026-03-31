class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        cache = [[float('inf')] * (len(grid[0])+1)]*(len(grid)+1)

        cache[len(grid)-1][len(grid[0])-1] = grid[-1][-1]
        

        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])-1, -1, -1):
                if (i == len(grid)-1) and j == (len(grid[0])-1):
                    continue
                cache[i][j] = grid[i][j] + min(cache[i+1][j], cache[i][j+1])
        
        return cache[0][0]



