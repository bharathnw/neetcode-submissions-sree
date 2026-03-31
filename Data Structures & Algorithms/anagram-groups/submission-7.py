class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = {}

        for word in strs:
            alph_count = [0] * 26
            for c in word:
                alph_count[ord(c) - ord('a')] += 1
            sorted_key = tuple(alph_count)
            res[sorted_key] = res.get(sorted_key, []) + [word]
        return list(res.values())
        