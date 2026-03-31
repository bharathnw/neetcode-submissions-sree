class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adjList = defaultdict(list)

        for word in words:
            for ch in word:
                if ch not in adjList:
                    adjList[ch] = []

        for i in range(1, len(words)):
            a, b = 0, 0

            while a < len(words[i-1]) and b < len(words[i]):
                if words[i-1][a] == words[i][b]:
                    a += 1
                    b += 1
                    continue
                break
            if a < len(words[i-1]) and b == len(words[i]):
                return ""
            if a < len(words[i-1]) and b < len(words[i]):
                adjList[words[i-1][a]].append(words[i][b])
        
        visits = set()
        res = []
        visiting = set()

        def dfs(node):
            if node in visiting:
                return True
            if node in visits:
                return False
            
            visiting.add(node)
            for nei in adjList[node]:
                if dfs(nei):
                    return True
            visiting.remove(node)
            visits.add(node)
            res.append(node)
            return False
        
        for item in list(adjList.keys()):
            if dfs(item):
                return ""
        res.reverse()
        return ''.join(res)







