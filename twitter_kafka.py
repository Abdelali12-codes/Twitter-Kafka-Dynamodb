

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092') #Same port as your Kafka server

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


topic_name = "firsttopic"


class twitterAuth():
    """SET UP TWITTER AUTHENTICATION"""

    def authenticateTwitterApp(self):
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        return auth



class TwitterStreamer():

    """SET UP STREAMER"""
    def __init__(self):
        self.twitterAuth = twitterAuth()

    def stream_tweets(self , query):
        while True:
            listener = ListenerTS()
            auth = self.twitterAuth.authenticateTwitterApp()
            stream = Stream(auth, listener)
            stream.filter(track=[query], stall_warnings=True, languages= ["en"])


class ListenerTS(StreamListener):

    def on_data(self, raw_data):
            producer.send(topic_name, str.encode(raw_data))
            print(str.encode(raw_data))
            return True


if __name__ == "__main__":
    TS = TwitterStreamer()
    twitt = input("Insert the twitt you want to look for :")
    TS.stream_tweets(twitt)