class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.node = Trie()
        

    def addWord(self, word: str) -> None:
        curr = self.node
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.isWord = True
        

    def search(self, word: str) -> bool:
        curr = self.node
        def dfs(i, node):
            if i == len(word):
                return node.isWord
            c = word[i]
            if c == '.':
                for child in node.children.values():
                    return dfs(i+1, child)
            if c not in node.children:
                return False
            else:
                return dfs(i+1, node.children[c])
        return dfs(0, curr)
                

        
