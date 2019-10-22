import tweepy
import markovify
import time

# OAuth Authentication is the preferred way of authenticating with Twitter.

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, name of the account will be printed
print("Account: " + api.me().name)

# Get raw text as strings
with open("funfacts.txt") as f:
    text = f.read()

# Build the Markov Chain model
# Because the training data are made up of sentences separated with newlines,
# we use the markovify.NewlineText class instead of the markovify.Text class
text_model = markovify.NewlineText(text)

while True:

    # Generate a tweet
    status = text_model.make_sentence() + "."
    print(status)

    # If the app settings are set to r+w then this will tweet out the generated
    # text to the account's timline
    api.update_status(status)

    # Set the bot to tweet every x minutes
    time.sleep(1800)
