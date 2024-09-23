import matplotlib.pyplot as plt

import numpy as np

import pandas as pd

#develope histogram
#A histogram is a chart that plots the distribution
#of a numeric variable's values as a series of bars

#fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
#for i in range(2):
#    for j in range(2):
#        axes[i, j].hist(np.random.randn(500), bins=50, color='k', alpha=0.5)
#plt.subplots_adjust(wspace=0, hspace=0)
#plt.show()

# create data
data = [32, 96, 45, 67, 76, 28, 79, 62, 43, 81, 70,
        61, 95, 44, 60, 69, 71, 23, 69, 54, 76, 67,
        82, 97, 26, 34, 18, 16, 59, 88, 29, 30, 66,
        23, 65, 72, 20, 78, 49, 73, 62, 87, 37, 68,
        81, 80, 77, 92, 81, 52, 43, 68, 71, 86]
 
# create histogram
#plt.hist(data, bins=20, color='r', alpha=0.7)
 
# display histogram
#plt.show()

#multiple histograms comparison
x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)

#kwargs = dict(histtype='stepfilled', alpha=0.3, bins=40)
#kwargs = dict(histtype='step', alpha=0.3, bins=40)

#plt.hist(x1, **kwargs)
#plt.hist(x2, **kwargs)
#plt.hist(x3, **kwargs)

#plt.show()
#density plots - They can be used to identify the shape of the distribution

#*************Bar Plots
fig, axes = plt.subplots(2, 1)
data = pd.Series(np.random.rand(16), index=list('abcdefghijklmnop'))
#data.plot.bar(ax=axes[0], color='k', alpha=0.7)
#data.plot.barh(ax=axes[1], color='g', alpha=0.3)

#plt.show()

#With a DataFrame, bar plots group the values in each row together
#in a group in bars,side by side, for each value

df = pd.DataFrame(np.random.rand(6, 4),index=['one', 'two', 'three', 'four', 'five', 'six'],columns=['A', 'B', 'C', 'D'])

df.plot.bar()
df.plot.barh(stacked=True, alpha=0.5)
plt.show()






