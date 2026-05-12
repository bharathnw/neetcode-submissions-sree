class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        res = 0

        tot = 0

        counter = {0:1}

        for num in nums:
            tot += num
            diff = tot -k

            res += counter.get(diff, 0)

            counter[tot] = counter.get(tot, 0) + 1
        
        return res
            
            
        