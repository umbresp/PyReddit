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

# flair.py
# Purpose: (Repeatedly) sets a flair for all submissions
# in a subreddit that reach a certain amount of points.
# Notes: This is meant to be run with cron about every 5 
# minutes or so.

# REMEMBER TO FILL OUT sub, karma_limit, and text!

import praw
import configparser as ConfigParser

# Name of subreddit you want to flair posts from. CASE SENSITIVE, no /r/
sub = 'masterhacker' # shameless plug

# Lower bound of karma the post must have to be flaired.
karma_limit = 1000

# Text to display on flair.
text = 'Certified Hacker'

config = ConfigParser.ConfigParser()
config.read('login.ini')
username = config.get('account', 'username')
password = config.get('account', 'password')
client_id = config.get('account', 'client id')
client_secret = config.get('account', 'client secret')
user_agent = f'{username} running flair.py'

r = praw.Reddit(client_id=client_id, client_secret=client_secret, password=password, user_agent=user_agent, username=username)

s = r.subreddit(sub)

for i in s.new(limit=1000):
    if i.score >= karma_limit:
        choices = i.flair.choices()
        template_id = next(x for x in choices if x['flair_text_editable'])['flair_template_id'] # TODO: add compatability for non-template flairs
        i.flair.select(template_id, text)

exit()