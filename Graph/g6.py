import matplotlib.pyplot as plt
import numpy as np

def wf(x,b,a):
    if b >= 1 or a%2 ==0 or b <=0 or a==1 :
        return 'некорректные параметры'
    sum=0
    for i in range(0,100):
        sum += (b**i) * np.cos((a**i) * np.pi*x)
    return sum
x=np.arange(-2 , 2 , 0.1)
plt.plot( x , wf(x,0.5,3) )
plt.grid()
plt.show()