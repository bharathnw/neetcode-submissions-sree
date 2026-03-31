class Twitter:

    def __init__(self):
        self.relations = defaultdict(set)
        self.tweets = []
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweets,(-1*self.time, tweetId, userId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.relations[userId]
        currTweets = self.tweets[:]
        newsFeed = []
        while len(newsFeed) < 10 and len(currTweets) > 0:
            time, tweetId, uId = heapq.heappop(currTweets)
            if uId in followees or uId == userId:
                newsFeed.append(tweetId)
        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.relations[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.relations[followerId].discard(followeeId)
        
