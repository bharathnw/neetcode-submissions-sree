class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        word_set = set(wordDict)
        res = []
        cur = []
        def dfs(i):
            if i == len(s):
                res.append(' '.join(cur))
                return
            
            for j in range(i+1, len(s)+1):
                word = s[i:j]
                if word in word_set:
                    cur.append(word)
                    dfs(j)
                    cur.pop()

        dfs(0)
        return res
        