class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.upper()

        l, r = 0, len(s)-1

        while l <= r:
            while l < r and (s[l] == ' ' or not s[l].isalnum()):
                l+=1
            while r > l and (s[r] == ' ' or not s[r].isalnum()):
                r-=1
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
    
        
        return True
        