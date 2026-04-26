class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        digits_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }



        res = []
        arr = []

        def backtrack(i, arr):
            if i == len(digits):
                res.append(''.join(arr[:]))
                return
            for j in digits_map[digits[i]]:
                arr.append(j)
                backtrack(i+1, arr)
                arr.pop()
        backtrack(0, [])
        return res

