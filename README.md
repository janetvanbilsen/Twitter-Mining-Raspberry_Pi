# Twitter Mining Using Raspberry Pi
Rather than running one Tweepy session a day, which results in tweets that are ony from one time period of the day, this project works with Raspberry Pi to _collect tweets continuously throughout the day_ (within the Twitter API rate-limit). This project is fully open-source under the MIT License.

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
The Raspberry Pi 4 Model B (4GB RAM) was used for this project, alongside a case that includes a cooling fan and heatsinks for the board. While _quiet mode_ was used for the cooling fan, the only program that was running was this project. Therefore, if you plan to use the Pi for other processes, it is advised to use the coolin fan in a higher setting.<br />

A monitor was used to initially setup the project. The Pi was subsequently used in headless mode for the rest of the data mining process. To keep track of the mining progress, it is advisable to track changes in the Dataset.csv via the terminal:<br />
`pi@raspberrypi:~ $ tail -n1 -F /home/pi/Sync/twitter/Dataset.csv`
* tail prints out any changes that occur to the file to the terminal 
* -F tracks the file even when the file does not exist yet, which is useful is the script is not running yet and you want to keep track when it starts 

### Python File ###
Make sure that you replace the Twitter API key placeholders with your own valid keys
* consumer_key
* consumer_secret
* access_token
* secret_token_secret

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

* `*/10 07-23 * * *`: executing every 10 mins from 7 am to midnight _[minute hour day(month) month day(week)]_
* `cd /home/pi/Sync/twitter`: changing directory to the folder that contains the python file
* `/usr/bin/python3.7`: folder that contains the Python version to be used
* `collect_tweets_master.py`: Python file that is to be run
