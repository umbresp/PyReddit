# MIT License
#
# Copyright 2018 umbresp
#
# Permission is hereby granted, free of charge, to any 
# person obtaining a copy of this software and 
# associated documentation files (the "Software"), to 
# deal in the Software without restriction, including 
# without limitation the rights to use, copy, modify, 
# merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom
# the Software is furnished to do so, subject to the 
# following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions
# of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF 
# ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
# TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT 
# SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR 
# ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN 
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

# archive.py
# Purpose: Archives all new modmail for a selected 
# subreddit before a certain date.
# Notes: I had a mini-stroke and forgot how to use strptime,
# also this only works with new modmail. (duh)

# REMEMBER TO FILL OUT sub, year_before, month_before, and day_before!

import praw
import datetime
import ConfigParser

# Name of subreddit you want to archive modmail from. CASE SENSITIVE, no /r/
sub = 'gumballmemes' # shameless plug

# The date you want to be the lower bound. For example, if my date is 12/31/2018,
# all modmails with a timestamp before that date will be archived.
year_before = "2000"
month_before = "1"
day_before = "1"

config = ConfigParser.ConfigParser()
config.read('login.ini')
username = config.get('account', 'username')
password = config.get('account', 'password')
client_id = config.get('account', 'client id')
client_secret = config.get('account', 'client secret')
user_agent = f'{username} running archive.py'


r = praw.Reddit(client_id=client_id, client_secret=client_secret, password=password, user_agent=user_agent, username=username)

s = r.subreddit(sub)

date2 = datetime.datetime.strptime(f'{year_before}{month_before}{day_before}000000+0000', "%Y%m%d%H%M%S%z")

for i in s.modmail.conversations(limit=1000):
    time = i.last_updated.replace(":", "")
    date = datetime.datetime.strptime(time, "%Y-%m-%dT%H%M%S.%f%z")
    if date < date2:
        print(i.subject)
        i.archive()

exit()
