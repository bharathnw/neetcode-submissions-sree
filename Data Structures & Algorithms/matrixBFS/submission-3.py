from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visits = set()
        q = deque()
        q.append((0,0))
        visits.add((0,0))
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        length = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                if r == rows-1 and c == cols-1:
                    return length

                for dr, dc in directions:
                    if r+dr == rows or c+dc == cols or r+dr <0 or c+dc < 0 or (r+dr, c+dc) in visits or grid[r+dr][c+dc] == 1:
                        continue
                    visits.add((r+dr, c+dc))
                    q.append((r+dr, c+dc))
            length +=1
        return -1 

