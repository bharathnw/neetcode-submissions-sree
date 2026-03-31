class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pac_set = set()
        atl_set = set()


        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    pac_set.add((i, j))
                if i == len(heights)-1 or j == len(heights[0])-1:
                    atl_set.add((i, j))


        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def bfs(check_set):
            q = deque(list(check_set))
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    if dr + r < 0 or dc + c < 0 or dr+r == len(heights) or dc+c == len(heights[0]) or (dr+r, dc+c) in check_set or heights[dr+r][dc+c] < heights[r][c]:
                        continue
                    check_set.add((dr+r, dc+c))
                    q.append((dr+r, dc+c))
            return check_set
        
        pacific = bfs(pac_set)
        atlantic = bfs(atl_set)
        return list(atlantic & pacific)



            
