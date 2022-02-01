import csv
import nltk
import HTMLParser
from nltk.corpus import stopwords
from textblob import TextBlob
import re


english_stopwords=stopwords.words("english")
html_parser = HTMLParser.HTMLParser()

f=open('tb2.csv','a')
csvWriter = csv.writer(f)
infile = 'finaltrain.csv'

with open(infile, 'r') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        sentence = row[1].decode("utf-8").encode("ascii","ignore").lower()
	sentence=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",sentence).split())
	filtered_line = [w for w in sentence.split() if not w in english_stopwords]
	filtered_line=' '.join(filtered_line)
	blob = TextBlob(filtered_line)
        csvWriter.writerow([blob,blob.sentiment.polarity, blob.sentiment.subjectivity])

