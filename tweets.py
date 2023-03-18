import tweepy
import json

# Fill in your Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Search for tweets with the hashtag #hacking
tweets = api.search(q='#hacking')

# Create a list of tweet dictionaries
tweet_list = []
for tweet in tweets:
    tweet_dict = {'text': tweet.text, 'user': tweet.user.screen_name}
    tweet_list.append(tweet_dict)

# Print the list of tweets as JSON
print(json.dumps(tweet_list))
