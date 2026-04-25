class TreeNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        

    def insert(self, word: str) -> None:
        head = self.root

        for c in word:
            if not c in head.children:
                head.children[c] = TreeNode()
            head = head.children[c]
        head.isWord = True


    def search(self, word: str) -> bool:
        head = self.root
        for c in word:
            if c in head.children:
                head = head.children[c]
            else:
                return False
        return head.isWord
        

    def startsWith(self, prefix: str) -> bool:
        head = self.root
        for c in prefix:
            if c in head.children:
                head = head.children[c]
            else:
                return False
        return True

        
        