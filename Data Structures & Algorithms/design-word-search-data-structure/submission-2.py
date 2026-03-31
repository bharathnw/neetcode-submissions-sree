class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.node = Trie()
        

    def addWord(self, word: str) -> None:
        curr = self.node

        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.isEnd = True
        

    def search(self, word: str) -> bool:
        curr = self.node

        def dfs(i, node):
            if i == len(word):
                return node.isEnd
            c = word[i]

            if c == '.':
                for val in node.children.values():
                    if dfs(i+1, val):
                        return True
                return False
            if c in node.children:
                return dfs(i+1, node.children[c])
            else:
                return False
        
            
        return dfs(0, curr)