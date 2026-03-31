class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [(math.sqrt((coords[0])**2 + (coords[1])**2), coords) for coords in points]
        heapq.heapify(points)
        output = []
        for i in range(k):
            output.append(heapq.heappop(points)[1])
        return output


        