class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        cache = {}

        for i in range(len(weight)):
            cache[(0, i)] = 0

        for i in range(capacity+1):
            if weight[0] <= i:
                cache[(i,0)] = profit[0]
            else:
                cache[(i,0)] = 0

        
        for m in range(1,len(weight)):
            for n in range(1, capacity+1):
                skip = cache[(n,m-1)]
                currWeight = weight[m]
                include = 0
                if n - currWeight >= 0:
                    include = profit[m] + cache[(n - currWeight,m-1)]
                cache[(n, m)] = max(include, skip)
        return cache[(capacity,len(weight)-1)]


