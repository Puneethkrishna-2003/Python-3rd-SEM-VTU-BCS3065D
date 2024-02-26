import matplotlib.pyplot as plt
import numpy as np

y=np.random.normal(11,1,100)
print(y)
plt.hist(y,20,color="yellow",edgecolor="black",label="histogram")
plt.legend()
plt.show()