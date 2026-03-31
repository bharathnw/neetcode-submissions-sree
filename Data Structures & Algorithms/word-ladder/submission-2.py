class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0

        adjList = defaultdict(list)

        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                adjList[pattern].append(word)
        
        visits = set()
        q = deque([beginWord])
        res = 0
        while q:
            res += 1
            for _ in range(len(q)):
                item = q.popleft()
                if item == endWord:
                    return res
                if item in visits:
                    continue
                visits.add(item)

                for i in range(len(item)):
                    pattern = item[:i] + '*' + item[i+1:]
                    for neighbor in adjList[pattern]:
                        if neighbor not in visits:
                            q.append(neighbor)
                
        return 0

