class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.counter = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.counter += 1
        self.tweets[userId].append((self.counter, tweetId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop(0) 
        

    def getNewsFeed(self, userId: int) -> List[int]:

        heap = []
        users_to_check = self.followers[userId] | {userId}
        for followee in users_to_check:
            for id, tweet in self.tweets[followee]:
                heapq.heappush(heap, (-1*id, tweet))
        res = []  
        while heap and len(res) < 10:
            res.append(heapq.heappop(heap)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
        
