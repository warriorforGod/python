import tweepy

consumer_key = 'OV3XirRBZeAR6SUjIOa2kufec'
consumer_secret = 'FPyjXX111PRvq2idEWISYcywQDeOKO0kr733gScZHt8N5UKIRV'
access_token = '1091914164-LXCuLB6R9eOSwSlEpJNkcUB1HtWpEjQJCYrDrms'
access_token_secret = 'BdTQSP33G7dn6eCyy9tBlnGKxYmHZsjJACCImWtVNz3xM'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)


print("\n\n\n\n\n\n")


searchQuery = 'Hawkeye OR hawkeye'

new_tweets = api.search(q=searchQuery, count=100,
						result_type = "recent",
						lang = "en")


for tweet in new_tweets:
	print(tweet.text)
