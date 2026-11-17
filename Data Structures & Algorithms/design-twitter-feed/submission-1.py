class Twitter:

    def __init__(self):
        self.users_info = {} # {user: {post:.. , follwer:.., followee}}
        self.cycle = 0
        # posts(heap) : [(self.cycle, tweetId))]
    def postTweet(self, userId: int, tweetId: int) -> None:
        user_info = self.users_info.get(
            userId, 
            {"posts": list(), "followers": set(), "followees": set()} 
        )
        self.users_info[userId] = user_info
        user_info["posts"].append((self.cycle, tweetId))

        self.cycle += 1

        return None

    def getNewsFeed(self, userId: int) -> List[int]:
        user_info = self.users_info.get(
            userId, 
            {"posts": list(), "followers": set(), "followees": set()} 
        )

        feed_themself = user_info["posts"] # queue 나올거임
        news_feed = feed_themself[:-11:-1]
        heapq.heapify(news_feed)
        followers = user_info["followers"]
        
        for follower in followers:
            feed = self.users_info.get(
                follower,
                {"posts": list(), "followers": set(), "followees": set()}
            )
            for cycle, tweetId in feed["posts"][:-11:-1]:
                if len(news_feed) < 10:
                    heapq.heappush(news_feed, (cycle, tweetId))
                elif news_feed[0][0] < cycle:
                    heapq.heapreplace(news_feed, (cycle, tweetId))
                else:
                    break # 더 최근게 힙에 못들어갔다면, 뒤에는 볼 필요가 없음
        
        sorted_list = []
        while news_feed:
            sorted_list.append(heapq.heappop(news_feed))

        return list(map(lambda x: x[1], sorted(sorted_list, key=lambda x: x[0], reverse=True)))
        

    def follow(self, followerId: int, followeeId: int) -> None:
        follower_info = self.users_info.get(
            followerId, 
            {"posts": list(), "followers": set(), "followees": set()} 
        )
        self.users_info[followerId] = follower_info
        follower_info["followers"].add(followeeId)
        
        followee_info = self.users_info.get(
            followeeId, 
            {"posts": list(), "followers": set(), "followees": set()} 
        )
        self.users_info[followeeId] = followee_info
        followee_info["followees"].add(followerId)

        return None

    def unfollow(self, followerId: int, followeeId: int) -> None:
        follower_info = self.users_info.get(
            followerId, 
            {"posts": list(), "followers": set(), "followees": set()} 
        )
        self.users_info[followerId] = follower_info
        print(follower_info)
        follower_info["followers"].discard(followeeId)

        followee_info = self.users_info.get(
            followeeId, 
            {"posts": list(), "followers": set(), "followees": set()} 
        )
        self.users_info[followeeId] = followee_info
        followee_info["followees"].discard(followerId)
        
        return None