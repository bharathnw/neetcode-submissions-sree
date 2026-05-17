class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        

        i = 1
        prev = arr[0]
        symbol = ''
        res = 0
        chain = 0
        
        while i < len(arr):
            if prev > arr[i] and symbol != '>':
                res += 1
                symbol = '>'
            elif prev < arr[i] and symbol != '<':
                res += 1
                symbol = '<'
            elif prev == arr[i]:
                res = 0
                symbol = ''
            else:
                res = 0
                symbol = ''
                continue
            
            chain = max(chain, res)
            prev = arr[i]
            i += 1
        
        return chain+1
        