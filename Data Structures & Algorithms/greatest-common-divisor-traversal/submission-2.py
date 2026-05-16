class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:

        def get_prime_factors(n):
            factors = []
            if n % 2 == 0:
                factors.append(2)
                while n % 2 == 0:
                    n //= 2
            
            factor = 3

            while factor * factor <= n:
                if n % factor == 0:
                    factors.append(factor)
                    while n % factor == 0:
                        n //= factor
                factor += 2

            if n > 1:
                factors.append(n)
            return factors

        adj = defaultdict(list)

        for i, num in enumerate(nums):
            factors = get_prime_factors(num)
            for factor in factors:
                adj[('i', i)].append(('f', factor))
                adj[('f', factor)].append(('i', i))
        
        visits = set()

        def dfs(node):
            if node in visits:
                return
            visits.add(node)
            for nei in adj[node]:
                dfs(nei)
        
        dfs(('i', 0))

        for i in range(len(nums)):
            if ('i', i) not in visits:
                return False
        
        return True










