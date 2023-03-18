import tweepy
import json

# Fill in your Twitter API credentials
consumer_key = '77UdiVpfBQpFZDvxuPlgvMFHs'
consumer_secret = 'AvycXqpzW6eMv0sjZA6nkLGwqOh4Gh0WRCId0JAKVnABgxP3gb'
access_token = '1531544153275785216-ei4xlrXO8sKVb3QXbkE3Mm12o6W6Jx'
access_token_secret = 'qpA5x82cFKlTnOCqSwwgdQQtzjpRECwkYYV4Ki4NHxAOv'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

tweets = api.search_tweets(q='#hacking', count=1)

# Create a list of tweet dictionaries
tweet_list = []
for tweet in tweets:
    tweet_dict = {'text': tweet.text, 'user': tweet.user.screen_name}
    tweet_list.append(tweet_dict)

# Print the list of tweets as JSON
print(json.dumps(tweet_list))
