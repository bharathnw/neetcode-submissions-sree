class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        dic = defaultdict(list)

        for item in strs:
            keys = [0] * 26
            for c in item:
                keys[(ord('a') - ord(c))] += 1
            dic[tuple(keys)].append(item)
        
        res = []

        for item in dic.values():
            res.append(item)
        
        return res
            

        