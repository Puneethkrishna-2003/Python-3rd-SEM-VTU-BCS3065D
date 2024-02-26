import matplotlib.pyplot as plt

overs=[1,2,3,4,5,6]
runs=[0,4,12,16,18,22]
plt.plot(overs,runs,linestyle="dashed",linewidth="2",color="yellow",marker="p",markerfacecolor="red",markersize=20,markeredgecolor="green",markeredgewidth="5")
plt.grid(True)
plt.show()