import tweepy
import markovify
import time
import sys

#OAuth authentication is the preferred way of authenticating with Twitter

consumerKey = ''
consumerSecret = ''

accessToken = ''
accessTokenSecret = ''

# Creates an OAuth handler with access token
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

# If the authentication was successful, print name of the account
print(f'Account: {api.me().name}')

# Load in corpora
with open("funfacts.txt") as f:
    text = f.read()

# Build the Markov Chain model
# Corpora is made up of sentences separated by newlines,
# so use NewlineText() method instead of Text()
textModel = markovify.NewlineText(text)

while True:

    try:
        # Generate a random sentence
        status = textModel.make_sentence() + '.'
        print(status)

        # If the app settings are set to r+w, this will tweet the
        # generated sentence to the account's timeline
        api.update_status(status)

        # Have the bot wait before creating a new tweet
        time.sleep(300)

    except KeyboardInterrupt:
        sys.exit()
