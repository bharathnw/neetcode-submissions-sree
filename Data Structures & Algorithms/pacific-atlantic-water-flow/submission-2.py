class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pac_set = set()
        atl_set = set()

        #Adding Pacific cordinates
        for i in range(len(heights)):
            pac_set.add((i, 0))
            atl_set.add((i, len(heights[0])-1))
        for j in range(len(heights[0])):
            pac_set.add((0, j))
            atl_set.add((len(heights)-1, j))
        
        def dfs(r, c, visits, dest):
            if (r,c) in dest:
                return True
            if (r, c) in visits:
                return False
            if r < 0 or c < 0 or r == len(heights) or c == len(heights[0]):
                return False

            visits.add((r,c))
            
            dirs = [(1,0), (0,1), (-1,0), (0,-1)]

            for dr, dc in dirs:
                if dr+r < len(heights) and dc+c < len(heights[0]) and heights[dr+r][dc+c] <= heights[r][c]:
                    if dfs(dr+r, dc+c, visits, dest) == True:
                        return True
            
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if dfs(i, j, set(), pac_set) == True:
                    pac_set.add((i, j))
                if dfs(i, j, set(), atl_set) == True:
                    atl_set.add((i, j))
        res = []
        for r, c in pac_set & atl_set:
            res.append([r,c])
        
        return res
                

            

        