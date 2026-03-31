from collections import OrderedDict 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        maxCount = 0

        num_map = {}
        heap = []
        result = []

        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1
        for key, count in num_map.items():
            heapq.heappush(heap, (-1*count, key))
        
        for _ in range(k):
            _, key = heapq.heappop(heap)
            result.append(key)
        
        return result

  



        