#offers a viable open source alternative to MATLAB
import matplotlib.pyplot as plt

import numpy as np

# data = np.arange(10)
# plt.plot(data)
# plt.show()
#%matplotlib notebook - Jupyter

# fig = plt.figure()
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# plt.show()
#An empty matplotlib figure with three subplots

# plt.plot(np.random.randn(50).cumsum(), 'k--')
# plt.show()
#The 'k--' is a style option instructing matplotlib to plot a black dashed line

# ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
# plt.show()

#Adjusting the spacing around subplots
#matplotlib includes a convenience method, plt.subplots
#subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=None, hspace=None)

fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
   for j in range(2):
       axes[i, j].scatter(np.random.randn(500),np.random.randn(500)*5)
plt.subplots_adjust(wspace=0, hspace=0)
plt.subplots_adjust(wspace=0)
plt.subplots_adjust(hspace=0)
plt.show()

#Colors, Markers, and Line Styles
x=np.array([0,1,2,3,4])
y=np.array([0,1,2,3,4])
axes[0,0].plot(x, y, 'g--')
linestyle=='-', color='g'
plt.show()

#Line plots can additionally have markers to highlight the actual data points
#axes[0,0].plot(x, y, 'ko--')
#color='k', linestyle='dashed', marker='o'
#plt.show()

data = np.random.randn(30).cumsum()
#Line plot with different drawstyle options
#plt.plot(data, 'k--', label='Default')
#plt.plot(data, 'k-', drawstyle='steps-post', label='steps-post')
#plt.legend(loc='best')
#plt.show()

#Ticks, Labels, and Legends
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(np.random.randn(1000).cumsum())
#plt.show()

ticks = ax.set_xticks([0, 250, 500, 750, 1000])
labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'],rotation=30, fontsize='small')
ax.set_title('My first matplotlib plot')
ax.set_xlabel('Stages')

props = {
'title': 'My first matplotlib plot',
'xlabel': 'Stages'
}
#ax.set(**props)
#The axes class has a set method that allows batch setting of plot properties

# plt.show()


#Drawing shapes
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3)
circ = plt.Circle((0.7, 0.2), 0.15, color='b', alpha=0.3)
pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]],
color='g', alpha=0.5)
ax.add_patch(rect)
ax.add_patch(circ)
ax.add_patch(pgon)
#plt.show()

#Saving Plots to File
#plt.savefig('figpath.png', dpi=400, bbox_inches='tight')
#dpi, which controls the dots-per-inch resolution, and
#bbox_inches, which can trim the whitespace around the actual figure
#plt.show()













