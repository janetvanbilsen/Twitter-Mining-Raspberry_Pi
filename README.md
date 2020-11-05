# CATS - Raspbery Pi Twitter Mining Server
CATS (Continuous rAspberry pi Tweets collection Server) can be used to turn a Raspberry Pi into a Twitter mining server. Using a server allows for tweets to be continuously collected throughout the day, rather than at one specific time period. CATS is therefore ideal for any project looking to observe patterns on Twitter for a span of time. This project is fully open-source under the MIT License.

## Table of Contents ##
<!--ts-->
   * [Table of contents](#table-of-contents)
   * [Introduction](#introduction)
   * [Installation](#installation)
   * [Instructions](#instructions)
      * [Raspberry Pi Setup](#raspberry-pi-setup)
      * [Location Datasets](#location-datasets)
      * [Crontab](#crontab)
<!--te-->

## Introduction ##
This README file describes the dataset of the final year project by Janet van Bilsen.  

## Installation ##
To install this project, either:
* Clone this Github repository 
* Download the master branch zip file.


## Instructions ##

### Raspberry Pi Setup ###
CATS was developed with the Raspberry Pi 4 Model B (4GB RAM). Although CATS has not been tested using older models, the running of the script is not very CPU intensive. <br />

While it might be easier to initially setup CATS using a monitor, the server is normally run in headless mode. A running log of the process of the tweets mining will be produced by CATS and saved as 'Mining_Log.txt.' This log includes tweet creation date&time, username of the tweeter, and date&time that the tweet was collected. Using the below code, you can keep this running log open in the terminal window on the Pi and use VNC Viewer to check on its progress via a virtual monitor on smartphone or laptop.<br />

`pi@raspberrypi:~ $ tail -n1 -F /home/pi/Sync/twitter/Mining_Log.txt`
* _tail_ prints out any changes that occur to the file to the terminal 
* _-n1_ only prints the last row
* _-F_ tracks the file even when the file does not exist yet, useful for when you want to track when the script starts running

### Python File ###
Make sure that you replace the Twitter API key placeholders with your own valid keys
* consumer_key
* consumer_secret
* access_token
* secret_token_secret<br />

The current setup has the script run for a maximum of 600 seconds (10 mins). This was done for stability reasons. Rather than have the script run for 17 consecutive hours, it was run for 10 mins every 10 mins for 17 hours. Doing so ensured that if there were any errors that caused the script to exit, it would be run again in less than 10 minutes again. Data loss is also therefore minimal. _See the [Crontab section](#crontab) for more details on how to automate the script_.


### Location Datasets ###
Included are two location datasets. These are Excel files that contain one column with locations that are applied to filter Twitter users' self-entered location. <br /><br />
`Places_UK.xlsx`<br />
Includes a column with the locations that you want to collect tweets from. _Names are not case sensitive_.
<br />
<br />
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
