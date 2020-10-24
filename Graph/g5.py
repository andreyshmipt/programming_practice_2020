import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 10))
x = [1, 2, 3, 4, 5, 6]
y = [1, 1.42, 1.76, 2, 2.24, 2.5]
plt.errorbar(x, y, xerr=0.05, yerr=0.1, fmt='none')
plt.scatter(x, y, label=r'$Экспериментальные точки$', s=10, color=(0, 0, 0, 1))
p1, v1 = np.polyfit(x, y, deg=1)
p2, v2, d2 = np.polyfit(x, y, deg=2)
t = np.arange(1, 6.1, 0.1)
plt.plot(t, p1 * t + v1, color='red')
plt.plot(t, p2 * (t ** 2) + v2 * t + d2, color='green')
plt.grid(True)
plt.show()
