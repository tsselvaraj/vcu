from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from datetime import datetime

from elasticsearch import Elasticsearch
es = Elasticsearch()

#Please get the API keys from https://apps.twitter.com

consumer_key="Your Key"
consumer_secret="Your Secret"

access_token="Token"
access_token_secret="Token Secret"

class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        #print (data[5:10])
        es.index(index="test", doc_type='tweet', body=data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['basketball'])
