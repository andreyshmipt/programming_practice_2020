import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-100, 100, 1)
plt.plot(x, np.log((x ** 2 + 1) * np.exp(-abs(x) / 10)) / (np.log(1 + np.tan(1 / (1 + np.sin(x) ** 2)))))
plt.show()