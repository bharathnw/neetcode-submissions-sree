class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:


        adj = {}

        for i in range(1, len(words)):
            x = 0
            while x < min(len(words[i-1]), len(words[i])) and words[i-1][x] == words[i][x]:
                x += 1
            if x == min(len(words[i-1]), len(words[i])):
                if len(words[i-1]) > len(words[i]):
                    return False
                continue
            
            adj[words[i-1][x]] = words[i][x] if x < len(words[i]) else ''


        
        count_set = set()
        for c in order:
            count_set.add(c)
            if c in adj and adj[c] in count_set:
                return False
        
        return True
        


        