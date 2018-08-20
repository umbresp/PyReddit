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

# remove_modqueue.py
# Purpose: Marks all posts currently in the modqueue of a
# selected subreddit before a certain date as removed.
# Notes: This is very badly written, and all the approve/
# remove/spam scripts are almost exactly the same. I haven't
# had an opportunity to clean up this code, so sorry.

# REMEMBER TO FILL OUT subreddit_to_clear, year_before, month_before, and day_before!

import praw
import datetime
import ConfigParser

# The subreddit you want to approve all posts in the unmoderated queue for.
subreddit_to_clear = "subredditname"  # CASE SENSITIVE, don't include the /r/

# The date you want to be the lower bound. For example, if my date is 12/31/2018,
# all posts with a timestamp before that date will have the action performed on.
year_before = "2000"
month_before = "1"
day_before = "1"

config = ConfigParser.ConfigParser()
config.read('login.ini')
username = config.get('account', 'username')
password = config.get('account', 'password')
client_id = config.get('account', 'client id')
client_secret = config.get('account', 'client secret')
user_agent = f'{username} running remove_modqueue.py'

r = praw.Reddit(client_id=client_id, client_secret=client_secret, password=password, user_agent=user_agent, username=username)
print(r)
for i in r.user.moderator_subreddits(limit=None):
    if i.display_name == subreddit_to_clear:
        print(i.display_name)
        for thing in [j for j in i.mod.modqueue(limit=None)]:  
            submissiontime = datetime.datetime.fromtimestamp(thing.created)  
            comparetotime = datetime.datetime(year_before, month_before, day_before)  
            if submissiontime < comparetotime:
                print(thing)
                print("removed")  
                thing.mod.remove(spam=False)  
            else:
                print(thing)
                print("ignored")