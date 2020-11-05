# CATS - Raspbery Pi Twitter Mining Server
CATS (Continuous rAspberry pi Tweets collection Server) can be used to turn a Raspberry Pi into a Twitter mining server. Using a server allows for tweets to be continuously collected throughout the day, rather than at one specific time period. CATS is therefore ideal for any project looking to observe patterns on Twitter for a span of time. This project is fully open-source under the MIT License.

## Table of Contents ##
<!--ts-->
   * [Table of contents](#table-of-contents)
   * [Introduction](#introduction)
   * [Installation](#installation)
   * [Instructions](#instructions)
      * [Twitter Script Setup](#twiiter-script-setup)
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

#### Script Running Time ####
The current setup has the script run for 600 seconds (10 mins). This is because the server was developed to run from 7am to midnight and instead of running the script for 17 hours straight, for stability reasons it would be better to run it every 10mins for 17 hours. Therefore, if there is any issues with timeout, the script will run again in less than 10 mins and reduce the amount of data lost. _See the [Crontab section](#crontab) for more details on how to automate the script_.<br />

To change the script running time, edit _time_limit_ in the MyStreamListener class:
`class MyStreamListener(StreamListener):
    def __init__(self, time_limit=600):`


### Location Datasets ###
Included are two location datasets. These are Excel files that contain one column with locations that are applied to filter Twitter users' self-entered location.<br />

`Places_UK.xlsx`<br />

Includes a column with the locations that you want to collect tweets from. _Names are not case sensitive_.<br />

`Location_exceptions.xlsx`<br /> 

Includes a column of location names that you _do not_ want to be included in the user's location string<br />
(e.g., USA is included to prevent American cities that are also UK cities, such as Birmingham)

### Crontab ###
Automate the running of the Twitter mining Python script by creating a cron job in the Raspberry Pi terminal.<br />

Enter into the cron editor by entering the following BASH command:<br />
`pi@raspberrypi:~ $ crontab -e`<br />
  
Format the cron job with the following cron expression:<br />
`*/10 07-23 * * * cd /home/pi/Sync/twitter && /usr/bin/python3.7 collect_tweets_master.py`  

* `*/10 07-23 * * *`: executing every 10 mins from 7 am to midnight
* `cd /home/pi/Sync/twitter`: changing directory to the folder that contains the python file
* `/usr/bin/python3.7`: folder that contains the Python version to be used
* `collect_tweets_master.py`: Python file that is to be run

### Raspberry Pi Setup ###
CATS was developed with the Raspberry Pi 4 Model B (4GB RAM). Although CATS has not been tested using older models, the running of the script is not very CPU intensive. <br />

While it might be easier to initially setup CATS using a monitor, the server is normally run in headless mode. A running log of the process of the tweets mining will be produced by CATS and saved as _Mining_Log.txt_' This log includes tweet creation date&time, username of the tweeter, and date&time that the tweet was collected. Using the below code, you can keep this running log open in the terminal window on the Pi and use VNC Viewer to check on its progress via a virtual monitor on smartphone or laptop.<br />

`pi@raspberrypi:~ $ tail -n1 -F /home/pi/Sync/twitter/Mining_Log.txt`
* _tail_ prints out any changes that occur to the file to the terminal 
* _-n1_ only prints the last row
* _-F_ tracks the file even when the file does not exist yet, useful for when you want to track when the script starts running
