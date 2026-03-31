class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = TrieNode()
        words = set(dictionary)
        for word in words:
            trie.addWord(word)

        cache = {}
        def dfs(i):
            if i >= len(s):
                return 0
            if i in cache:
                return cache[i]
            curr = trie
            res = len(s)

            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.isEnd:
                    res = min(res, dfs(j+1))
            
            #skipping 1st character
            res = min(1 + dfs(i+1), res)
            cache[i] = res
            return res
        
        return dfs(0)

            
             

        