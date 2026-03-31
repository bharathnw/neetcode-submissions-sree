class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        adj = {}

        for i in range(1, len(words)):

            before = words[i-1]
            curr = words[i]
            l, r = 0, 0

            while r < len(curr) and l < len(before) and before[l] == curr[r]:
                l += 1
                r += 1
            
            if r == len(curr):
                return False
            adj[before[l] if l < len(before) else ''] = curr[r]
        
        hash_set = set()
        for c in order:
            if c in adj and adj[c] in hash_set:
                return False
            hash_set.add(c)
        
        return True



