class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0

        curr = '='
        prev = arr[0]
        curr_len = 1
        max_len = 1

        for i in range(1, len(arr)):
            if arr[i] == prev:
                curr = "="
                curr_len = 1
            elif ((arr[i] > prev and curr != '>') or (arr[i] < prev and curr != '<')):
                curr = '>' if arr[i] > prev else '<'
                curr_len += 1 
            else:
                curr_len = 2
                curr = '>' if arr[i] > prev else '<'
            max_len = max(curr_len, max_len)
            prev = arr[i]
        return max_len



        