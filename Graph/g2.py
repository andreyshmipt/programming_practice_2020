import matplotlib.pyplot as plt
import numpy as np
#x**2 - x -6
sp = plt.subplot(111)
x=np.arange(-10,10.01,0.01)
plt.plot(x, x**2-x -6)
sp.spines['bottom'].set_position('center')
plt.show()