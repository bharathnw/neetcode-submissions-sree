class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        graph = defaultdict(list)
        wordList.append(beginWord)
        for i, word in enumerate(wordList):
            for j in range(i+1, len(wordList)):
                if word == wordList[j]:
                    continue
                cnt = 0
                for k in range(len(word)):
                    if wordList[j][k] != word[k]:
                        cnt += 1
                
                if cnt == 1:
                    graph[word].append(wordList[j])
                    graph[wordList[j]].append(word)
        visits = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for _ in range(len(q)):
                item = q.popleft()
                for word in graph[item]:
                    if word == endWord:
                        return res+1
                    if word not in visits:
                        visits.add(word)
                        q.append(word)
            res += 1
        return 0



        
        