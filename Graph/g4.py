import matplotlib.pyplot as plt
import numpy as np

f = input()
x = np.arange(-10, 10.1, 0.1)
with plt.xkcd():
    plt.plot(x, eval(f))
    plt.show()

