class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        R = len(board)
        C = len(board[0])
        visits = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r == R or c == C or (r, c) in visits:
                return False
            if word[i] != board[r][c]:
                return False
                
            visits.add((r, c))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = dr+r
                nc = dc+c
                if dfs(nr, nc, i+1):
                    return True
            visits.remove((r, c))
            return False

        for i in range(R):
            for j in range(C):
                if dfs(i, j, 0) == True:
                    return True
        
        return False
