import tweepy
import pymongo
import jsonpickle
import json
consumer_key = "1Woy5AQKx0OX3cXgBvfXThBql"
consumer_secret = "yEeRJ1Ck7evCQmEwsKkQF8yJbCl6NWsjuUPu6ofevwnscZTWEG"
# Replace the API_KEY and API_SECRET with your application's key and secret.
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
 
api = tweepy.API(auth, wait_on_rate_limit=True,
				   wait_on_rate_limit_notify=True)
 
client=pymongo.MongoClient()
db=client.work
if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)
tweetsPerQry = 1 # this is the max the API permits
new_tweets = api.search(q="#OSM")
n=0
for tweet in new_tweets:
		    n+=1
		    #print n,".","\n\n",tweet.text,"\n\n\n\n"		    
		    #print tweet
		    new=jsonpickle.encode(tweet._json, unpicklable=False)
		    new_tweets1=json.loads(new)
		    print new_tweets1
		    db.tweet.insert(new_tweets1) 
