# Twitter Mining Using Raspberry Pi
Rather than running one Tweepy session a day, which results in tweets that are ony from one time period of the day, this project works with Raspberry Pi to _collect tweets continuously throughout the day_ (within the Twitter API rate-limit). This project is fully open-source under the MIT License.

## Table of Contents ##
<!--ts-->
   * [Table of contents](#table-of-contents)
   * [Introduction](#introduction)
   * [Installation](#installation)
   * [Usage](#usage)
      * [Crontab](#crontab)
<!--te-->

## Introduction ##
This README file describes the dataset of the final year project by Janet van Bilsen.  

## Installation ##
To install this project, either:
* Clone this Github repository 
* Download the master branch zip file.


## Usage ##

### Crontab ###
Automate the running of the Twitter mining Python script by creating a cronjob in the Raspberry Pi terminal.  

Enter the crontab editor  
`pi@raspberrypi:~ $ crontab -e`
 
Formatting the crontab job  
`*/10 07-23 * * * cd /home/pi/Sync/twitter && /usr/bin/python3.7 collect_tweets_master.py`  
* `*/10 07-23 * * *`: executing every 10 mins from 7 am to midnight [minute hour day(month) month day(week)]
* `cd /home/pi/Sync/twitter`: changing directory to the folder that contains the python file
* `/usr/bin/python3.7`: folder that contains the Python version to be used
* `collect_tweets_master.py`: Python file that is to be run
