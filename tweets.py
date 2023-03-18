import tweepy
import json

# Fill in your Twitter API credentials
consumer_key = 'b23TzGMScmTbIz90KPD6ma6HX'
consumer_secret = '5ZCvIIneI5po2UZ9v4uPNS0XzqFGpvr0peCytiaztOOksb0lsv'
access_token = '969358132605579264-h6Fd9o3BJhdUfr8ceepSU4t22kMW3hi'
access_token_secret = 'Pq4XeT8sXBpVkL53u6df7gMt4YZYRXKKzMqvWU50NEAla'

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
