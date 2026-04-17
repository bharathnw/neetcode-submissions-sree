class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        total = n
        adj = defaultdict(list)
        counter = defaultdict(int)
        for src, dest in trust:
            adj[src].append(dest)
            counter[dest] += 1
        
        for num in range(1, n+1):
            if num not in adj and counter[num] == (n-1):
                return num
        
        return -1

        