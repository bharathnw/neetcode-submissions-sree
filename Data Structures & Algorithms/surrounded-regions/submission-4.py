class Solution:
    def solve(self, board: List[List[str]]) -> None:

        q = deque([])
        m, n = len(board), len(board[0])

        for r in range(m):
            for c in [0, n-1]:
                if board[r][c] == 'O':
                    q.append((r, c))

        for c in range(1, n-1):
            for r in [0, m-1]:
                if board[r][c] == 'O':
                    q.append((r, c))

        borders = set()
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                borders.add((r,c))
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = dr+r, dc+c
                    if nr < 0 or nc < 0 or nr == len(board) or nc == len(board[0]) or board[nr][nc] == 'X' or (nr, nc) in borders:
                        continue

                    q.append((nr, nc))

        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r, c) in borders:
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'
        