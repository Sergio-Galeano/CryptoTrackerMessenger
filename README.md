# CryptoTrackerMessenger

This repository contains a python script that tracks prices for the top ten cryptocurrencies by market cap. Using crontab, a time-based scheduling program in your operating system, you will be able to schedule the program at precise moments.

Skills practiced and learned by running this program include:
* webscraping
* working with a website's sourcecode (HTML and CSS)
* working with Twilio, an SMS gateway service that allows you to send text messages from your programs via the internet
        * note: Twilio is free and comes with an abundant quantity of free text messages to use before having to consider paying
* Making your python program executable and scheduling it to send yourself a text message at a predetermined time(s) using crontab


** REGARDING THE ACCOMPANYING FILES **

*requirements.txt            --> Contains the three libraries you will need to install in order to run the python program /n
*crontab.txt                 --> A short overview of working with crontab from your terminal /n
*running_python_programs.txt --> Instructions on making your program executable (TO BE DONE BEFORE SCHEDULING IT WITH CRONTAB)



** FINAL NOTE **

As with the majority of webscraping programs that grab data from websites, they will inevitably need to be updated over time, 
as companies and data providers change their website layout over time.

The webscraping program I built relies on several websites and their specific formatting in the HTML and CSS files. You may choose to use different websites from which to grab the cryptocurrency prices, which will require you to familiarize yourself with that specific website's sourcecode so that you can extract the desired content (i.e. price)

