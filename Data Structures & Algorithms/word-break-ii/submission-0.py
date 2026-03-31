class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        word_set = set(wordDict)
        cur = []
        res = []
        def backtrack(i):
            if i == len(s):
                res.append(' '.join(cur))
                return

            for j in range(i, len(s)):
                curr = s[i:j+1]
                if curr in word_set:
                    cur.append(curr)
                    backtrack(j+1)
                    cur.pop()
            return
        backtrack(0)
        return res
            