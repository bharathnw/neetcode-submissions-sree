class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []

        def isPalindrome(s):
            l = 0
            r = len(s)-1
            while l <= r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        def dfs(i, arr):
            if i == len(s):
                res.append(arr[:])
                return
            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]):
                    arr.append(s[i:j+1])
                    dfs(j+1, arr)
                    arr.pop()
        dfs(0, [])
        return res

        
        