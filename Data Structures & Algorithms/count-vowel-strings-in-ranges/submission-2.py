class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        res_arr = []

        vowels = set(['a', 'e', 'i', 'o', 'u'])

        cnt = 0

        for word in words:
            curr_cnt = 0
            if word[0] in vowels and word[-1] in vowels:
                curr_cnt += 1
                cnt += 1
            res_arr.append(cnt)
        
        res = []
        
        for st, end in queries:
            sub = None
            if st > 0:
                sub = res_arr[st-1]

            end_set = res_arr[end]
            if sub:
                end_set -= sub

            res.append(end_set)
        
        return res


                
        