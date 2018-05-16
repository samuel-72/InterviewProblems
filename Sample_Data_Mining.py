'''
This is a sample program to pull data from Twitter APIs

Name - Sample_Data_Mining
Description - To pull sample data from twitter for performing mining
Website - http://www.placeholder.com
https://apps.twitter.com/app/9214450

'''

import tweepy
from tweepy import OAuthHandler

consumer_key = 'gzpExhkffgtnanhAXdxBd3wYw'
consumer_secret = 'wRQzfU9yw4513K35Ke1dP1xBOd22WuQGBguB1ALv2FyqHElB72'
access_token = '157910787-y4aDLb2caKz6UZ5yzMdd0vMkxlsmt3gyMo7c68YT'
access_secret = 'yphZoI0LGD5bAQQtX2fjyYcDZ9rKDgWkRNce7OyxR7MJa'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

print type(api)
'''
for tweet in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(tweet.text) 
'''    
#timeline = api.user_timeline(screen_name='arjun6_6', include_rts=True, count=100)
timeline = api.user_timeline(screen_name='rajnikanth', include_rts=True, count=10)
for tweet in timeline:
    print ("ID:", tweet.id)
    print ("User ID:", tweet.user.id)
    print ("Text:", tweet.text)
    print ("Created:", tweet.created_at)
    print ("Source:", tweet.source)
    # Process a single status

print api.search_users("vikash",20)
api.create_friendship('arjun6_6')
print "\n\n",api.rate_limit_status()
print api.reverse_geocode(37.3087450,-121.9178500)

'''

print "\nI am : " , api.me().name
print "\nMy unique twitter id is : " , api.me().id
print "\nI am at: " , api.me().location
print "\nI have " , api.me().friends_count, " friends."
'''
'''
print dir(twitter)
apiSearch = twitter.Api( consumer_key, consumer_secret, access_token, access_secret  )

search = apiSearch.GetSearch(term='adventure', lang='en', result_type='recent', count=100, max_id='')
for t in search:
    print t.user.screen_name + ' (' + t.created_at + ')'
    #Add the .encode to force encoding
    print t.text.encode('utf-8')
    print ''
'''