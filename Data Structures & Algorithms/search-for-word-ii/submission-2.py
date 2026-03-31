class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        r, c = len(board), len(board[0])

        root = Trie()

        for word in words:
            root.insert(word)

        visits = set()
        res = set()

        def dfs(row, col, node, word):
            if row < 0 or row == r or col < 0 or col == c or (row, col) in visits :
                return
            if board[row][col] not in node.children:
                return
            visits.add((row, col))
            node = node.children[board[row][col]]
            word += board[row][col]
            if node.isWord:
                res.add(word)
            
            dfs(row+1, col, node, word)
            dfs(row-1, col, node, word)
            dfs(row, col+1, node, word)
            dfs(row, col-1, node, word)
            
            visits.remove((row, col))

        for i in range(r):
            for j in range(c):
                dfs(i, j, root.root, "")
        
        return list(res)

        