class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:


        meetings.sort()

        heap = []

        rooms_used = defaultdict(int)

        for i in range(n):
            heapq.heappush(heap, (0, i))
        
        for st, end in meetings:
            while heap and heap[0][0] < st:
                _, room = heapq.heappop(heap)
                heapq.heappush(heap, (st, room))

            time, room = heapq.heappop(heap)
            heapq.heappush(heap, (time + (end - st), room))
            rooms_used[room] += 1

        res = -1
        maxVal = -1
        for key, val in rooms_used.items():
            if val > maxVal:
                res = key
                maxVal = val
        
        return res

        