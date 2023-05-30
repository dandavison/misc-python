# https://leetcode.com/problems/tweet-counts-per-frequency


# ["TweetCounts","recordTweet","recordTweet","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","recordTweet","recordTweet","recordTweet","recordTweet"]
# [[],["tweet0",33],["tweet1",89],["tweet2",99],["tweet3",53],["tweet4",3],["hour","tweet0",89,3045],["tweet0",28],["tweet0",91],["tweet0",9],["tweet1",6]]

# output: [null,null,null,null,null,null,[0,1],null,null,null,null]

# expected: [null,null,null,null,null,null,[0],null,null,null,null]

from collections import defaultdict


class TweetCounts:
    def __init__(self):
        self.tweets = defaultdict(list)
        self.strides = {
            "minute": 60,
            "hour": 60 * 60,
            "day": 24 * 60 * 60,
        }

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(
        self, freq: str, tweetName: str, startTime: int, endTime: int
    ) -> List[int]:

        try:
            stride = self.strides[freq]
        except KeyError:
            raise KeyError(f"Invalid freq key: {freq}")

        chunks = []
        curr_chunk = 0
        count = 0
        times = sorted(self.tweets[tweetName])
        for time in times:
            if time > endTime:
                break
            chunk = (time - startTime) // stride
            if chunk != curr_chunk:
                chunks.append(count)
                curr_chunk = chunk
                count = 0
            count += 1
        chunks.append(count)
        return chunks
