
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        sortedStones = [-x for x in stones]
        print(sortedStones)

        heapq.heapify(sortedStones)
        print(sortedStones)

        while len(sortedStones) > 1:
            x = -heapq.heappop(sortedStones)
            y = -heapq.heappop(sortedStones)

            if x == y:
                continue
            else:
                heapq.heappush(sortedStones, -abs(y-x))
        return -sortedStones[0] if sortedStones else 0

            

        