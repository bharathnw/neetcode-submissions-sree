class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        nodes = {}

        if not words:
            return ""
        prev = words[0]
        for wordIndex in range(1, len(words)):
            for i in range(min(len(prev), len(words[wordIndex]))):
                if prev[i] != words[wordIndex][i]:
                    if prev[i] in nodes:
                        nodes[prev[i]].append(words[wordIndex][i])
                    else:
                        nodes[prev[i]] = [words[wordIndex][i]]
                    break
                else:
                    if len(prev) > len(words[wordIndex]):
                        return "" 
            prev = words[wordIndex]
        for word in words:
            for c in word:
                if c not in nodes:
                    nodes[c] = []
        res = []
        visits = set()
        visiting = set()
        def dfs(key):
            if key in visiting:
                return True
            if key in visits:
                return
            visits.add(key)
            visiting.add(key)
            for neighbor in nodes.get(key, []):
                if dfs(neighbor) == True:
                    return True
            res.append(key)
            visiting.remove(key)
        
        for key in nodes.keys():
            if dfs(key) == True:
                return ""
        
        return "".join(res[::-1])
