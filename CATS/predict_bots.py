#!/usr/bin/env python

import pandas as pd
import time
import tweepy
import botometer

# Authenticating twitter
consumer_key = 'uEgngDaydm9A5upXp44j6L2XM'
consumer_secret = 'lCMlwFbT0d4FTElh33wuay1NCHNC5W9b49regjGH7RJ40BXTer' 
access_token = '1306187660592123905-KHAcQ4Cyiw5IcB64Tys95Hb03sSYbe'
secret_token_secret = 'c4qxlhQsjsf02l4CrEJfzPcdHIReHZYgHmqrkUnP1QXct'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, secret_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Authenticating Botometer API
rapidapi_key = "efef2a84e3msh6e190d74b8cec09p1ee471jsnf9ef67417ba3"
twitter_app_auth = {
    'consumer_key': 'uEgngDaydm9A5upXp44j6L2XM',
    'consumer_secret': 'lCMlwFbT0d4FTElh33wuay1NCHNC5W9b49regjGH7RJ40BXTer',
    'access_token': '1306187660592123905-KHAcQ4Cyiw5IcB64Tys95Hb03sSYbe',
    'access_token_secret': 'c4qxlhQsjsf02l4CrEJfzPcdHIReHZYgHmqrkUnP1QXct',
  }

bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)
                          
# Function to create/append csv file
def append_as_row(file_name, new_row):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(new_row)

# Opening dataset
dataset = pd.read_csv('Dataset.csv', header=None)

# List of unique usernames from dataset
usernames = dataset.iloc[:,1].to_list()
unique_usernames = list(set(usernames))

# Reading existing users checked and saving as list
users_already_checked = pd.read_csv('usernames_checked_bot.csv')
users_already_checked = users_already_checked.user.to_list()

# Creating a new list that has filtered out users already checked
check_usernames = [user for user in unique_usernames if user not in users_already_checked]

# Capturing date of bot account check
current_date = time.strftime('%Y%m%d')

# Resetting current day's API limit back to 0
accounts_checked = 0

# Checking accounts for 6 hours
max_time = 21600
start_time = time.time()

for user in check_usernames:
    # Checking if past Botometer API limit and still usernames left to check
    if (accounts_checked < 2000) and (len(check_usernames) > 0):
        # Checking if script is still within time limim, otherwise doesn't run
        if (time.time() - start_time) > max_time:
            break
            
        try:
            bot_pred = bom.check_account('@' + user)['cap']['english']
        except tweepy.TweepError:
            bot_pred = 'NA'

        # Format: date checked, user, bot prediciton
        user_row = []
        row.append(current_date)
        row.append(user)
        row.append(bot_pred)

        append_as_row('bot_dataset.csv', user_row)
        append_as_row('usernames_checked_bot.csv', user)
        accounts_checked += 1
            


