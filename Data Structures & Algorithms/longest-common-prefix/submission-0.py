class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ""

        minStr = min(strs, key=len)

        for i in range(len(minStr)):
            check = strs[0][i]
            for s in strs:
                if s[i] != check:
                    return res
            
            res += check
        
        return res