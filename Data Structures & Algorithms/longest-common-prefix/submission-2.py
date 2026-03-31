class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = ''
        i = 0
        while i < len(min(strs)):
            curr = strs[0][i]
            for word in strs[1:]:
                if word[i] != curr:
                    return res
            res += curr
            i += 1
        
        return res
                
            

        