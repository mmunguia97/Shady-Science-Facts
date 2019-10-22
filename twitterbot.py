import tweepy
import markovify

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#print(api.me().name)

#api.update_status(status = 'Updating using OAuth authentication via Tweepy!')
