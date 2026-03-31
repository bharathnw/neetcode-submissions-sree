class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        res = 0
        count = 0
        symbol = None

        for i in range(1, len(arr)):
            if not symbol:
                if arr[i-1] < arr[i]:
                    symbol = '<'
                    count += 1
                elif arr[i-1] > arr[i]:
                    symbol = '>'
                    count += 1
                else:
                    symbol = '='
                    count = 0
            else:
                if arr[i-1] < arr[i]:
                    if symbol != '<':
                        count += 1
                    else:
                        count = 1
                    symbol = '<'
                elif arr[i-1] > arr[i]:
                    if symbol != '>':
                        count += 1
                    else:
                        count = 1
                    symbol = '>'
                else:
                    symbol = '='
                    count = 0
            res = max(count, res)
        return res+1

        