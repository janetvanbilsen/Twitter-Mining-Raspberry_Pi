# Twitter-Mining
Using Raspberry Pi to mine Tweets by automating the running of Tweepy API

## Create a cron job to automate the running of the .py file ##
Automate the running of the Twitter mining Python script by creating a cronjob in the Raspberry Pi terminal.  

Enter the crontab editor  
`pi@raspberrypi:~ $ crontab -e`
 
Cron job: runs the script every 10 mins from 7 am to midnight  
`*/10 07-23 * * * cd /home/pi/Sync/twitter && /usr/bin/python3.7 collect_tweets_master.py`
