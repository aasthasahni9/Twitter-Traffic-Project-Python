# -*- coding: utf-8 -*-
from string import digits
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize

import csv
import math
import string
from collections import Counter
from nltk.stem import PorterStemmer
from nltk import ngrams
from nltk import pos_tag


english_stopwords=stopwords.words("english")
stemmer=PorterStemmer()
all_tokens=[]
all_bigrams=[]


f = open("tb1.csv", "rb")
f1=open('tfout.csv','a')
csvWriter = csv.writer(f1)
reader = csv.reader(f, delimiter=',')
for row in reader:
	tokens=word_tokenize(row[0].decode("utf-8","ignore").encode("ascii","ignore").lower())
	#bigrams= list(ngrams(tokens,3))
	all_tokens= all_tokens+tokens
	#all_bigrams=bigrams+all_bigrams
	all_tokens_stemmed=[]
	for token in all_tokens:
		if len(token)<2:	
			continue
		stemmed_token=stemmer.stem(token)
		all_tokens_stemmed.append(stemmed_token)
	frequency=Counter(all_tokens_stemmed)
	top_50=frequency.most_common(50)
	csvWriter.writerows(top_50)



   
	
