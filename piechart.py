import matplotlib.pyplot as plt

split=[10,20,10]
cou=["hi","bye","bolo"]
e=[0.1,0.1,0.1]
plt.pie(split,autopct="%1.1f%%",shadow=True,explode=e,labels=cou)
plt.legend()
plt.show()
