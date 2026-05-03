class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort()    

        queries_map = []
        for i in range(len(queries)):
            queries_map.append((queries[i], i))
        
        res = [-1] * len(queries)

        queries_map.sort()
        heap = []
        i = 0
        for q, index in queries_map:
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(heap, (intervals[i][1]-intervals[i][0]+1, intervals[i]))
                i += 1
            while heap and heap[0][1][1] < q:
                heapq.heappop(heap)
            
            if not heap:
                continue
            
            res[index] = heap[0][0]
        
        return res
            

