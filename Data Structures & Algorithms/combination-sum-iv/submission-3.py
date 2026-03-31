class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        cache = {0:1}

        for tot in range(1, target+1):
            cache[tot] = 0
            for num in nums:
                cache[tot] += cache.get(tot-num, 0)

        return cache[target]

                
        