class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s)-1
        while L < R:
            while L < R and s[R].isalnum() == False:
                R -= 1
            while L < R and s[L].isalnum() == False:
                L += 1
            if s[L].upper() != s[R].upper():
                return False
            L += 1
            R -= 1
        return True
        