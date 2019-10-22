import tweepy
import markovify

# OAuth Authentication is the preferred way of authenticating with Twitter.

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#print(api.me().name) TODO

# Get raw text as strings
with open("funfacts.txt") as f:
    text = f.read()

# Build the Markov Chain model
# Becauase the training data are made up of sentences separated with newlines,
# we use the markovify.NewlineText class instead of the markovify.Text class
text_model = markovify.NewlineText(text)

# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 200 characters
for i in range(3):
    print(text_model.make_short_sentence(200))

#api.update_status(status = 'Updating using OAuth authentication via Tweepy!')
