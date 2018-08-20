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

# spoiler.py
# Purpose: Marks posts with certain flair classes as Spoiler.
# Notes: This was made solely for /r/MysteryDungeon and
# has not been adapted for other subreddits, so it may
# have some bugs. Also, this is meant to be run with cron
# or something similar every 5 minutes or so.

# REMEMBER TO FILL OUT subreddit and spoiler_classes!

import praw
import requests
import ConfigParser

# Name of subreddit to perform spoiler marking on.
subreddit = "MysteryDungeon"  # CASE SENSITIVE, don't include the /r/

# Flair classes that are considered spoilers.
spoiler_classes = ['All-spoilers', 'PMD1-spoilers', 'PMD2-spoilers', 'PMD3-spoilers', 'PMD4-spoilers']

config = ConfigParser.ConfigParser()
config.read('login.ini')
username = config.get('account', 'username')
password = config.get('account', 'password')
client_id = config.get('account', 'client id')
client_secret = config.get('account', 'client secret')
user_agent = f'{username} running spoiler.py'

r = praw.Reddit(client_id=client_id, client_secret=client_secret, password=password, user_agent=user_agent, username=username)

s = r.subreddit(subreddit)

for i in s.new(limit=1000):
    if i.link_flair_css_class in spoiler_classes:
        i.mod.spoiler()
        print(i.title)
        
exit()
