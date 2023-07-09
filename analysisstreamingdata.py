Here's an example of Python code that performs real-time sentiment analysis on streaming data using the TextBlob library:

```python
from textblob import TextBlob
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Create a custom StreamListener class
class SentimentListener(StreamListener):
    def on_status(self, status):
        # Get the tweet text
        tweet = status.text
        # Perform sentiment analysis using TextBlob
        analysis = TextBlob(tweet)
        sentiment = analysis.sentiment.polarity
        if sentiment > 0:
            print("Positive sentiment")
        elif sentiment < 0:
            print("Negative sentiment")
        else:
            print("Neutral sentiment")

    def on_error(self, status_code):
        print("Error:", status_code)

# Create an OAuthHandler instance
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create a Stream object with the OAuthHandler instance and the custom StreamListener class
stream = Stream(auth, SentimentListener())

# Filter the stream to track tweets containing specific keywords
stream.filter(track=["keyword1", "keyword2"])
```

Make sure to replace the placeholder values for the Twitter API credentials with your own. Also, modify the `track` parameter in the `stream.filter()` method to specify the keywords you want to track in the streaming data.

This code uses the `TextBlob` library to perform sentiment analysis on each tweet received in real-time. The sentiment polarity is a floating-point value between -1 and 1, where values closer to 1 indicate positive sentiment, values closer to -1 indicate negative sentiment, and values close to 0 indicate neutral sentiment. The code then prints the sentiment category for each tweet based on its polarity value.