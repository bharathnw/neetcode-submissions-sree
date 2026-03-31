class Solution:
    def solve(self, board: List[List[str]]) -> None:
        safe = deque()

        R = len(board)
        C = len(board[0])

        for i in range(1,C-1):
            if board[0][i] == 'O':
                safe.append((0, i))
            if board[R-1][i] == 'O':
                safe.append((R-1, i))

        for i in range(R):
            if board[i][0] == 'O':
                safe.append((i, 0))
            if board[i][C-1] == 'O':
                safe.append((i, C-1))
        dirs = [(1,0), (0, 1), (-1, 0), (0, -1)]
        while len(safe) > 0:
            for _ in range(len(safe)):
                x, y = safe.popleft()
                board[x][y] = 'S'
                for dr, dc in dirs:
                    if x+dr < 0 or x+dr == R or y+dc < 0 or y+dc == C:
                        continue
                    if board[x+dr][y+dc] == 'O':
                        safe.append((x+dr, y+dc))

        for i in range(R):
            for j in range(C):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        
                



        
        