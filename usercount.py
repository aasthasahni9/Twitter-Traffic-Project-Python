import csv
import StringIO
from collections import Counter


f = open("tfout.csv", "rb")
reader = csv.reader(f, delimiter=',')

reader.next() #skip header
word = [row[0] for row in reader]

frequency=Counter(word)
top_ten= frequency.most_common(100)
print(top_ten)

