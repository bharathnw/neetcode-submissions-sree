class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)

        for num in nums:
            if num in res:
                res[num] += 1
            else:
                res[num] = 1
        sorted_res = dict(sorted(res.items(),key = lambda item:item[1],reverse = True)) 
        
        list_res= list(sorted_res.keys())
        return list_res[:k]
