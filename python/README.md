I'm in the process of making this very nice and saving state after each request so that you can pick it back up
anytime. But for now I made it so its simply run by using crontab commands that will keep me within API limits

It uses the configuration file found in config directory to automatically assign defaults to arguments
for scraping

The current index is just a text file with an index in it. Found at alpha-vantage/state/current_index.txt

You must update the config file with your own alpha vantage API key which you can get here:
https://www.alphavantage.co/support/#

Run script like so (using all absolute paths):

alpha-vantage/get-stock-data-for-symbol \
-c /home/steven/employer-examples/python/alpha-vantage/config/time_period_30.yml \
-o /home/steven/employer-examples/python/alpha-vantage/data/time_period_30 \
-s /home/steven/employer-examples/python/alpha-vantage/stock-list.txt \
-i /home/steven/employer-examples/python/alpha-vantage/state/current_index.txt \
-l /home/steven/employer-examples/python/alpha-vantage/log.log

I run it in my crontab like this (repeating a couple times to not hit my request limit):

0 17 * * * /home/steven/ai/stocks/alpha-vantage/get-stock-data-for-symbol

Or you can make it repeating throughout the day if you want / have unlimited access

It takes about 10 minutes to run if you use the functions as per defined by the supplied config file

Also note that no data will be written until the certain stock finishes each indicator
