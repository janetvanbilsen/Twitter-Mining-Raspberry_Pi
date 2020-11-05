#!/usr/bin/env python3

import tweepy
import time
import datetime
from tweepy.streaming import StreamListener
import pandas as pd
import sys
from csv import writer

# Twitter API keys
consumer_key = 'uEgngDaydm9A5upXp44j6L2XM'
consumer_secret = 'lCMlwFbT0d4FTElh33wuay1NCHNC5W9b49regjGH7RJ40BXTer'
access_token = '1306187660592123905-KHAcQ4Cyiw5IcB64Tys95Hb03sSYbe'
secret_token_secret = 'c4qxlhQsjsf02l4CrEJfzPcdHIReHZYgHmqrkUnP1QXct'

# Gaining Twitter access
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, secret_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Places that should be included in geographical location
uk_places = pd.read_excel('/home/pi/Sync/twitter/Places_UK.xlsx')
uk_places = list(uk_places.Place)
uk_places = [place.lower() for place in uk_places]

# Places that are to be filtered out from geographical location
no_places = pd.read_excel('/home/pi/Sync/twitter/Location_exceptions.xlsx').Place.to_list()

# Keywords that will be used to search Twitter
keywords = ['depression', 'depressed', 'depressive', 'depressing']

# Current date to label the file name
current_date = time.strftime('%Y%m%d')
filename = current_date + '.csv'

# Function to append csv
def append_list_as_row(file_name, list_of_elem):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)

class MyStreamListener(StreamListener):
    # Time limit of 10 mins (600 sec)
    def __init__(self, time_limit=600):
        self.start_time = time.time()
        self.limit = time_limit
        self.api = api
        super(MyStreamListener, self).__init__()

    def on_status(self, status):

        # Checking that the script only runs cetain amount of time
        if (time.time() - self.start_time) < self.limit:
            user_data = []
            
            # Opens time tweets extracted and tweet identifier to log.txt
            log_file = open("/home/pi/Sync/twitter/Mining_Log.txt", 'a')
            
            self.save_tweet = 0
            
            # Checks if user has a location, then if location is in UK list
            try:
                if status.user.location is not None: 
                    if (sum([1 for loc in uk_places if loc in status.user.location.lower()]) > 0) and (sum([1 for place in no_places if place in status.user.location]) == 0):
                        self.save_tweet = 1
            except:
                pass

            # Checks that tweet is not RT or empty, then saves (full) tweet & info
            if self.save_tweet == 1:
                try:
                    if not hasattr(status, 'retweeted_status'):
                        try:
                            if any(status.extended_tweet["full_text"].find(keyword) > -1 for keyword in keywords):
                                twt_creat = status.created_at
                                user_data.append(twt_creat)

                                sn = status.user.screen_name
                                user_data.append(sn)
                                
                                user_data.append(status.user.location)
                                
                                user_data.append(status.extended_tweet["full_text"])
                            
                                log_file.write(f"{datetime.datetime.now()},{sn},{twt_creat}\n")
                                log_file.close()

                        except AttributeError:
                            if any(status.text.find(keyword) > -1 for keyword in keywords):
                                twt_creat = status.created_at
                                user_data.append(twt_creat)

                                sn = status.user.screen_name
                                user_data.append(sn)
                                
                                user_data.append(status.user.location)
                                
                                user_data.append(status.text)
                                
                                log_file.write(f"{datetime.datetime.now()},{sn},{twt_creat}\n")
                                log_file.close()

                        append_list_as_row('Dataset.csv', user_data)
                       
                except:
                    pass

        else:
            return False
        
myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener(), tweet_mode='extended')

myStream.filter(track=keywords, languages=["en"])



