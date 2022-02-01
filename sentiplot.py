import pandas
import matplotlib.pyplot as plt
import pylab


data=pandas.read_csv('/home/aastha9/tb1.csv', sep=',',index_col=['polarity'])

my_plot =data.sort(columns='subjectivity',ascending=False).plot(kind='line',legend=None,title="tweets sentiments polarity",color="green")

my_plot.set_xlabel('subjectivity')
my_plot.set_ylabel('polarity')
pylab.xlim(10,10)
plt.show()

