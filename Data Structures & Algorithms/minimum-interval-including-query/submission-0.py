class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        res = [-1] * len(queries)

        new_queries = [(queries[i], i) for i in range(len(queries))]

        new_queries.sort()

        minHeapInt = []
        intervals.sort()
        i = 0

        for q in new_queries:
            query, index = q
            while i < len(intervals) and intervals[i][0] <= query:
                heapq.heappush(minHeapInt, ((intervals[i][1]- intervals[i][0]+1), intervals[i]))
                i += 1
            while minHeapInt and minHeapInt[0][1][1] < query:
                heapq.heappop(minHeapInt)
            if minHeapInt:
                res[index] = minHeapInt[0][0]
        return res
        



        