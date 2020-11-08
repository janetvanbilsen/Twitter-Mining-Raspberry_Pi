# CATS - Raspbery Pi Twitter Mining Server
Since Streaming API, the most widely used tweets collection tool, returns at most only 1% of the available tweets on Twitter, projects trying to capture discourse on Twitter for a continuous period of time are at a disadvantage with a limited sample. It is therefore crucial to collect as many tweets as possible while still  keeping in line with Twitter's rate limit. However, sometimes research groups or individuals are not able to access a remote university server, for example, to run Streaming API throughout the day. Keeping a laptop on 24/7 is not really a great option. <br />

It is for this reason that **CATS (Continuous rAspberry pi Tweets collection Server)** was developed. CATS is a program that can be installed on a Raspberry Pi to turn it into a cost-effective Twitter mining server. Due to its stability and lower power requirements, the Pi is perfect for hosting a server that collects 24/7 or for whatever other period required. <br />

This project is fully open-source under the MIT License.

## Table of Contents ##
<!--ts-->
   * [Table of contents](#table-of-contents)
   * [Introduction](#introduction)
   * [Installation](#installation)
   * [Instructions](#instructions)
      * [Twitter Script Setup](#twitter-script-setup)
      * [Location Datasets](#location-datasets)
      * [Crontab](#crontab)
      * [Raspberry Pi Setup](#raspberry-pi-setup)
<!--te-->

## Introduction ##

## Installation ##
To install this project, either:
* Clone this Github repository 
* Download the master branch zip file.


## Instructions ##

### Twitter Scirpt Setup ###
#### Developer API Keys ####
Make sure that you replace the Twitter API key placeholders in `collect_tweets_master.py` with your own valid Twitter developer keys
* consumer_key
* consumer_secret
* access_token
* secret_token_secret<br />

#### Twitter Search ####
CATS was developed to study depression on Twitter. Hence, the default keywords. To change the terms used to search Twitter, edit the following code in `collect_tweets_master.py`:<br />

`keywords = ['depression', 'depressed', 'depressive', 'depressing']`<br />

The tweet language is set to English. This can be changed by editing the following code:<br />

`myStream.filter(track=keywords, languages=["en"])`<br />

#### Script Running Time ####
The current setup has `collect_tweets_master.py` run for 600 seconds (10 mins). Since this server was developed to run from 7am to midnight, instead of running the script for 17 hours straight, it runs every 10 minutes for 17 hours. This is because if there are any issues, the script will run again in less than 10 minutes and reduce the amount of data lost. _See the [Crontab section](#crontab) for details on how to automate the script_.<br />

To change the script running time, edit _time_limit_ in the MyStreamListener class:<br /><br />
`class MyStreamListener(StreamListener):`<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`def __init__(self, time_limit=600):`

### Location Datasets ###
Included are two location datasets. These are Excel files that contain one column with locations that are applied to filter Twitter users' self-entered location.<br />

`Places_UK.xlsx`: includes a column with the locations that you want to collect tweets from. _Names are not case sensitive_.<br />

`Location_exceptions.xlsx`: includes a column of location names that you _do not_ want to be included in the user's location string
(e.g., USA is included to prevent American cities that are also UK cities). _Names are case sensitive_.

### Crontab ###
Automate the running of the Twitter mining Python script by creating a cron job in the Raspberry Pi terminal.<br />

Enter into the cron editor with the following BASH command:<br />
`pi@raspberrypi:~ $ crontab -e`<br />
  
Format the cron job with the following cron expression:<br />
`*/10 07-23 * * * cd /home/pi/Sync/twitter && /usr/bin/python3.7 collect_tweets_master.py`  

* `*/10 07-23 * * *`: executing every 10 mins from 7 am to midnight
* `cd /home/pi/Sync/twitter`: changing directory to the folder that contains the python file
* `/usr/bin/python3.7`: folder that contains the Python version to be used
* `collect_tweets_master.py`: Python file that is to be run

### Raspberry Pi Setup ###
CATS was developed with the Raspberry Pi 4 Model B (4GB RAM). Although CATS has not been tested using older models, the running of the script is not very CPU intensive. <br />

While it might be easier to initially setup CATS using a monitor, the server is normally run in headless mode. A running log of the process of the mining will be produced by CATS and saved as `Mining_Log.txt`. This log includes tweet creation date&time, username of the tweeter, and date&time that the tweet was collected. Using the code below, you can keep this running log open in the terminal window on the Pi and use VNC Viewer to check on its progress (via smartphone or laptop).<br />

`pi@raspberrypi:~ $ tail -n1 -F /home/pi/Sync/twitter/Mining_Log.txt`
* _tail_ prints out any changes that occur to the file to the terminal 
* _-n1_ only prints the last row
* _-F_ tracks the file even when the file does not exist yet, useful for when you want to track when the script starts running
