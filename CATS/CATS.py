#!/usr/bin/env python3

import tweepy
import time
import datetime
from tweepy.streaming import StreamListener
import pandas as pd
import sys
from csv import writer

# Twitter API keys
consumer_key = '*************************'
consumer_secret = '*************************************************'
access_token = '*******************-******************************'
secret_token_secret = '*********************************************'

# Gaining Twitter access
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, secret_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Places that should be included in geographical location
incl_places = pd.read_excel('pathname for incl_places.xlsx file')
incl_places = list(incl_places.place)
incl_places = [place.lower() for place in uk_places]

# Places that are to be filtered out from geographical location
excl_places = pd.read_excel('pathname for excl_place.xlsx').place.to_list()

# Keywords that will be used to search Twitter
keywords = ['keyword1', 'keyword2', 'keyword3']

# Function to create/append to dataset.csv
def append_list_as_row(file_name, list_of_elem):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)

# Class to run Twitter Streaming API
class MyStreamListener(StreamListener):
    # Setting running time to max 10 mins (600 sec)
    def __init__(self, time_limit=600):
        self.start_time = time.time()
        self.limit = time_limit
        self.api = api
        super(MyStreamListener, self).__init__()

    def on_status(self, status):
        if self.save_tweet == 1:
            try:
                if not hasattr(status, 'retweeted_status'):
                    try:
                        # Checking if tweet is not RT and keyword is in full tweet
                        if any(status.extended_tweet["full_text"].find(keyword) > -1 for keyword in keywords):
                            twt_creat = status.created_at
                            user_data.append(twt_creat)

                            sn = status.user.screen_name
                            user_data.append(sn)
                            
                            user_data.append(status.user.location)
                            
                            user_data.append(status.extended_tweet["full_text"])
                        
                            log_file.write(f"{datetime.datetime.now()}, {twt_creat}\n")
                            log_file.close()

                    # If no 'full tweet' attribute
                    except AttributeError:
                        # Checking if keyword is in tweet
                        if any(status.text.find(keyword) > -1 for keyword in keywords):
                            twt_creat = status.created_at
                            user_data.append(twt_creat)

                            sn = status.user.screen_name
                            user_data.append(sn)
                            
                            user_data.append(status.user.location)
                            
                            user_data.append(status.text)
                            
                            log_file.write(f"{datetime.datetime.now()}, {twt_creat}\n")
                            log_file.close()
                            
                        append_list_as_row('dataset.csv', user_data)
                except:
                    pass
        else:
            return False
        
myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener(), tweet_mode='extended')

myStream.filter(track=keywords, languages=['en'])



