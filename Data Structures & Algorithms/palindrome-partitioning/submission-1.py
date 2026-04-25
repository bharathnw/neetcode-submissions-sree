class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalind(w):
            if len(w) < 2:
                return True
            if w[0] != w[-1]:
                return False
            return isPalind(w[1:-1])
        
        arr = []
        res = []
        def dfs(i):
            if i == len(s):
                res.append(arr[:])
                return

            for j in range(i, len(s)):
                word = s[i:j+1]
                if isPalind(word):
                    arr.append(word)
                    dfs(j+1)
                    arr.pop()
                
        dfs(0)
        return res