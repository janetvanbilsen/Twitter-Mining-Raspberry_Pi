# Twitter Mining Using Raspberry Pi
Rather than running one Tweepy session a day, which results in tweets that are ony from one time period of the day, this project works with Raspberry Pi to _collect tweets continuously throughout the day_ (within the Twitter API rate-limit). This project is fully open-source under the MIT License.

## Table of Contents ##
<!--ts-->
   * [Table of contents](#table-of-contents)
   * [Introduction](#introduction)
   * [Installation](#installation)
   * [Instructions](#instructions)
      * [Crontab](#crontab)
<!--te-->

## Introduction ##
This README file describes the dataset of the final year project by Janet van Bilsen.  

## Installation ##
To install this project, either:
* Clone this Github repository 
* Download the master branch zip file.


## Instructions ##

## Python File ##
Ensure that you replace the Twitter API key placeholders with your own valid keys
* consumer_key
* consumer_secret
* access_token
* secret_token_secret

## Location Datasets ##
Included are two location datasets: 
* Places_UK.xlsx: includes a column with the locations that you want to collect tweets from _(names are not case sensitive)_
* Location_exceptions.xlsx: includes a column of location names that you _do not_ want to be included in the user's location string (e.g., USA is included to prevent American cities that are also UK cities, such as Birmingham)

### Crontab ###
Automate the running of the Twitter mining Python script by creating a cron job in the Raspberry Pi terminal.  


Enter into the cron editor by entering the following BASH command:<br />
`pi@raspberrypi:~ $ crontab -e`<br />
  
Format the cron job with the following cron expression:<br />
`*/10 07-23 * * * cd /home/pi/Sync/twitter && /usr/bin/python3.7 collect_tweets_master.py`  

* `*/10 07-23 * * *`: executing every 10 mins from 7 am to midnight _[minute hour day(month) month day(week)]_
* `cd /home/pi/Sync/twitter`: changing directory to the folder that contains the python file
* `/usr/bin/python3.7`: folder that contains the Python version to be used
* `collect_tweets_master.py`: Python file that is to be run
