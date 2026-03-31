class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        cache[0] = 1

        for num in nums:
            newMap = {}
            for key, val in cache.items():
                newMap[key+num] = newMap.get(key+num,0)+val
                newMap[key-num] = newMap.get(key-num,0)+val
            cache = newMap
        return cache.get(target,0)


