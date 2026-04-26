class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:


        adj = {}

        for i in range(n):
            adj[i] = []
        
        for sc, dest, price in flights:
            adj[sc].append((price, dest))
        
        prices = [float('inf')] * n
        prices[src] = 0
        q = deque([])

        if not adj[src]:
            return -1
        
        q = deque([(0, src, 0)])

        while q:
            for _ in range(len(q)):
                price, dest, stops = q.popleft()
                if stops > k:
                    continue
                for np, nd in adj[dest]:
                    if (price+np) < prices[nd]:
                        prices[nd] = price+np
                        q.append((price+np, nd, stops+1))
        
        return prices[dst] if prices[dst] != float('inf') else -1
                

        
        