class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        row, col = len(board), len(board[0])
        visits = set()
        def dfs(r, c, w):
            if word == w:
                return True
            if r < 0 or c < 0 or r == row or c == col or (r,c) in visits:
                return False
            visits.add((r,c))
            w += board[r][c]
            found = (dfs(r+1, c, w) or dfs(r, c+1, w) or dfs(r-1, c, w) or dfs(r, c-1, w))
            visits.remove((r,c))  
            return found              
        
        for r in range(row):
            for c in range(col):
                if dfs(r, c, ""):
                    return True
        
        return False
         
        