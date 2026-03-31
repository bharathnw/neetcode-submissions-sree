class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        maxHeap = []

        for i in range(len(position)):
            heapq.heappush(maxHeap, (-1 * position[i], -1 * speed[i]))

        res = 0
        currTime = 0

        while maxHeap:
            maxItem = heapq.heappop(maxHeap)
            time = (target - (-1*maxItem[0]))/(-1*maxItem[1])
            if time > currTime:
                currTime = time
                res += 1
        
        return res