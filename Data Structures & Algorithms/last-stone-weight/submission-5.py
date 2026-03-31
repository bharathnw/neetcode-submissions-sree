class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)


        while len(stones) > 1:
            max1 = heapq.heappop(stones)
            max2 = heapq.heappop(stones)
            res = max1 - max2
            if res != 0:
                heapq.heappush(stones, res)
        if len(stones) > 0:
            return abs(stones[0])
        return 0
        