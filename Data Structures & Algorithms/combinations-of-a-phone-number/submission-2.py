class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res = []

        mapper = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(i, letters):
            if i == len(digits):
                res.append(letters)
                return
            
            for c in mapper[digits[i]]:
                backtrack(i+1, letters+ c)
        
        if digits:
            backtrack(0, '')
        

        return res
            
            
        