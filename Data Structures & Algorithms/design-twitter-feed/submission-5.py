class Twitter:

    def __init__(self):
        self.followMap = {}
        self.tweetMap = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetMap:
            self.tweetMap[userId] = []
        self.tweetMap[userId].append((self.count, tweetId))
        self.count += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.followMap:
            self.followMap[userId] = []
        following = self.followMap[userId]

        tweets = []
        if userId in self.tweetMap:
            tweets.extend(self.tweetMap[userId])
        for user in following:
            if user != userId:
                tweets.extend(self.tweetMap[user])

        heapq.heapify_max(tweets)
        result = []
        for i in range(10):
            if not tweets:
                break
            tweet = heapq.heappop_max(tweets)[1]
            if tweet not in result:
                result.append(tweet)
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = []
        if followeeId not in self.followMap[followerId]:
            self.followMap[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

