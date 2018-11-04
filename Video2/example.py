import tweepy

consumer_key = 'ZJeKLEf370VV2MWfqPfiqFlnl'
consumer_secret = 'HMEs2B9sOw8zMtYY7PnjfHvxo7YK3aQTZ0Jqxn7RXHZu63JQbl'

access_token = '38060521-I2Ves38viCdoY7CWHhWwrIyjZkUiGOSpPFvulbJ6M'
access_token_secret = 'vhJC7SYPJpjYRNpMqRfQNCrrlem4dmTxakniMl9zevz2N'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
