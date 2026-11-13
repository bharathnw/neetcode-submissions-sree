class Solution:
    def customSortString(self, order: str, s: str) -> str:

        s_set = set(order)
        

        s_mapper = {}

        for i in range(len(s)):
            s_mapper[s[i]] = s_mapper.get(s[i], 0) + 1
        
        
        res = ''
        rem = ''
        for c in order:
            if c in s_mapper and s_mapper[c] > 0:
                res += c * s_mapper[c]
                del s_mapper[c]
            
        for x in s:
            if x not in s_set:
                rem += x


        return res + rem
        