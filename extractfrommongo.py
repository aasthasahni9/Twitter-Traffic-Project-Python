import pymongo
import pymongo
client=pymongo.MongoClient()
db=client.work
str1=db.tweet.find()
file1=open('userfromdb.txt','a')
for s in str1:
	file1.write(s['user']['screen_name'])
	print s['user']['screen_name'],":"
	print s['text']
	print "\n"
