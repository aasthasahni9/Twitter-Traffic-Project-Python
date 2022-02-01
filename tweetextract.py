import tweepy
consumer_key = "1Woy5AQKx0OX3cXgBvfXThBql"
consumer_secret = "yEeRJ1Ck7evCQmEwsKkQF8yJbCl6NWsjuUPu6ofevwnscZTWEG"
# Replace the API_KEY and API_SECRET with your application's key and secret.
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
 
api = tweepy.API(auth, wait_on_rate_limit=True,
				   wait_on_rate_limit_notify=True)
 
if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)
tweetsPerQry = 15 # this is the max the API permits
new_tweets = api.search(q="#OSM", count=tweetsPerQry)
n=0
for tweet in new_tweets:
		    n+=1
		    print n,".","\n\n",tweet.text,"\n\n\n\n"
