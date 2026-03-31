class Solution:
    def checkValidString(self, s: str) -> bool:
        
        leftAdd, leftRem, leftIgnore = 0,0,0

        for c in s:
            if c == '(':
                leftAdd += 1
                leftRem += 1
                leftIgnore += 1
            elif c == ')':
                leftAdd -= 1
                leftRem -= 1
                leftIgnore -= 1
            else:
                leftAdd += 1
                leftRem -= 1
            if leftAdd < 0:
                return False
            
            leftIgnore = max(0, leftIgnore)
            leftRem = max(0, leftRem)
        
        return leftIgnore == 0 or leftRem == 0
