class Solution:
    def isPalindrome(self, s: str) -> bool:

        L, R = 0, len(s)-1

        while L < R:
            while L < R and not s[L].isalnum():
                L += 1
            while R > L and not s[R].isalnum():
                R -= 1
            if s[L].upper() == s[R].upper():
                L += 1
                R -= 1
            else:
                return False
        
        return True