# CATS - Raspbery Pi Twitter Mining Server
Since Streaming API, the most widely used tweets collection tool, returns at most only 1% of the available tweets on Twitter, projects trying to capture discourse on Twitter for a continuous period of time are at a disadvantage with a limited sample. It is therefore crucial to collect as many tweets as possible while still  keeping in line with Twitter's rate limit. However, sometimes research groups or individuals are not able to access a remote server to run Streaming API throughout the day. Keeping a laptop on 24/7 is not really a great option. <br />

It is for this reason that **CATS (Continuous rAspberry pi Tweets collection Server)** was developed. CATS is a program that can be installed on a Raspberry Pi to turn it into a cost-effective Twitter mining server. The current project is developed to work with UNIX-like operating systems.<br />

This project is fully open-source under the <a href="https://mit-license.org/">MIT License</a>.<br />

_CATS is still in development_

## Table of Contents ##
<!--ts-->
   * [Table of contents](#table-of-contents)
   * [Introduction](#introduction)
   * [Installation](#installation)
   * [Instructions](#instructions)
      * [Twitter Script Setup](#twitter-script-setup)
      * [Automating Script](#automating-script)
      * [Monitoring Progress](#monitoring-progress)
<!--te-->

## Introduction ##

## Installation ##
To install this project, either:
* Clone this Github repository 
* Download the master branch zip file


## Instructions ##

### Twitter Scirpt Setup ###
#### Developer API Keys ####
Make sure that you replace the Twitter API key placeholders in `CATS.py` with your own valid Twitter developer keys<br />
* `consumer_key = '*************************'`
* `consumer_secret = '*************************************************'`
* `access_token = '*******************-******************************'`
* `secret_token_secret = '*********************************************'`<br />

#### Twitter Search ####
Initialise the keywords that you would like to search using Streaming API in the `CATS.py` file. To do so, change the default terms :<br />

`keywords = ['keyword1', 'keyword2', 'keyword3']`<br />

The default tweet language is set to English. This can be changed by editing the following code:<br />

`myStream.filter(track=keywords, languages=['en'])`<br />

#### Specifying Tweet Location ####
Included are two location datasets. These are Excel files that contain one column with locations that are applied to filter Twitter users' self-entered location. Provided are location names for anyone wishing to study tweets exclusively from the UK.<br />

`incl_places.xlsx`: provided is a default dataset of 1000+ places within the UK to search for tweets from users that have any country, city or town within the UK in their Twitter bio location. _Names are not case sensitive_.<br /> 

`excl_places.xlsx`: provided is a default dataset of American state names. This is for places that you _do not_ want to be included in the user's location string
(i.e., MD is included to prevent Salisbury, Maryland from being included in a UK dataset). _Names are case sensitive_.<br />

Note: before running the script, you must enter your own file pathname for these two files.<br />

#### Specifying Mining Details ####
The current script saves the following Twitter attributes:
* (Entire) tweet content: `status.extended_tweet["full_text"]` and `status.text`
* Screen name of user: `status.user.screen_name`
* User location (from bio): `status.user.location`<br /> 

This can be changed by editing the `MyStreamListener` class.<br />

### Automating Script ###

#### Script Running Time ####
The current setup has `CATS.py` run for 600 seconds (10 mins). Since this server was developed to run from 7am to midnight. Instead of running the script for 17 hours straight, it runs every 10 minutes for 17 hours. This is because if there are any issues, the script will run again in less than 10 minutes and reduce the amount of data lost. _See the [Crontab section](#crontab) for details on how to automate the script_.<br />

To change the script running time, edit _time_limit_ in the MyStreamListener class:<br /><br />
`class MyStreamListener(StreamListener):`<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`def __init__(self, time_limit=600):`<br />

#### Automating Running of Script ####
Automate the running of the Twitter mining Python script by creating a cron job in the Raspberry Pi terminal. The default in the script is every 10 mins from 7 am to midnight.<br />

Enter into the cron editor with the following BASH command:<br />
`pi@raspberrypi:~ $ crontab -e`<br />
  
Format the cron job with the following cron expression:<br />
`*/10 07-23 * * * cd /home/pi/Sync/twitter && /usr/bin/python3.7 CATS.py`  

* `*/10 07-23 * * *`: cron expression signifying script automation rules
* `cd /home/pi/Sync/twitter`: changing directory to the folder that contains the python file
* `/usr/bin/python3.7`: folder that contains the Python version to be used
* `CATS.py`: Python file that is to be run<br />

It helps to use <a href="https://crontab.guru/">crontab guru</a> with creating cron schedule expressions.<br />

#### Cleaning Dataset ####

The mining file creates empty rows when it does not collect tweets. To solve this, the CATS folder contains a file called `cleaning_empty_rows.py'` that removes these empty rows. Simply use crontab as below to automate the removal the empty rows.<br />

`2 0 * * * cd /home/pi/Sync/twitter && /usr/bin/python3.7 cleaning_empty_rows.py`
* This runs every two minutes past midnight, since data collection runs from 7 am to midnight


### Monitoring Progress ###

#### Viewing Running Log ####
A running log of the process of the mining is be produced by CATS and saved as `mining_log.txt`. This log includes tweet collection date&time and tweet creation date&time in csv format.<br />

Example log:<br />
`2020-11-12 13:15:44.214850, 2020-11-12 13:15:39`<br />
`2020-11-12 13:16:15.402419, 2020-11-12 13:16:10`<br />
`2020-11-12 13:17:10.156553, 2020-11-12 13:17:04`<br />
`2020-11-12 13:17:20.880684, 2020-11-12 13:17:15`<br />
`2020-11-12 13:17:25.362443, 2020-11-12 13:17:19`<br />
`2020-11-12 13:17:50.145950, 2020-11-12 13:17:45`<br />
`2020-11-12 13:17:55.546557, 2020-11-12 13:17:50`<br />
`2020-11-12 13:18:09.518031, 2020-11-12 13:18:04`<br />

You can use SSH to run the mining log on a computer to view its progress. Once logged into the Pi's terminal using SSH, run the below code to have the mining log run on the terminal.<br />

`pi@raspberrypi:~ $ tail -n1 -F /home/pi/Sync/twitter/mining_log.txt`
* _tail_ prints out any changes that occur to the file to the terminal 
* _-n1_ only prints the last row
* _-F_ tracks the file even when the file does not exist yet, useful for when you want to track when the script starts running<br />

Alternatively, you can use <a href="https://www.realvnc.com/en/connect/download/viewer/">VNC viewer</a> to view the terminal of the Pi and in that way monitor it's progress.
