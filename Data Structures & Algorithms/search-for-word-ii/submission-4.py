class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = Trie()
                curr = curr.children[c]
        curr.isWord = True           


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = Trie()

        for word in words:
            root.addWord(word)
        
        R = len(board)
        C = len(board[0])
        visits = set()
        res_set = set()

        def dfs(r, c, curr, node):
        
            if r < 0 or c < 0 or r == R or c == C or (r, c) in visits:
                return
            if board[r][c] not in node.children:
                return
            res = curr+board[r][c]
            if node.children[board[r][c]].isWord:
                res_set.add(res)
            visits.add((r, c))
            for dr, dc in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = dr+r, dc+c
                dfs(nr, nc, res, node.children[board[r][c]])
            visits.remove((r, c))

        for r in range(R):
            for c in range(C):
                dfs(r, c, '', root)
        return list(res_set)

        