class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        heap = []
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for sr, dt, price in flights:
            adj[sr].append((price, dt))
        #cost, stops, dest
        heap = [(0, 0, src)]

        while heap:
            cost, stops, dest = heapq.heappop(heap)
            if stops > k +1:
                continue
            else:
                if dest == dst:
                    return cost
                for neiCost, neiDest in adj[dest]:
                    heapq.heappush(heap, (neiCost+cost, stops+1, neiDest))

        return -1 
        