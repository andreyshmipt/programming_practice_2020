import numpy as np
x=int(input())
y=np.log((np.e**(1/(np.sin(x)+1)))/(1.25+(x**-1)*0.2))/np.log(1+x**2)
print(y)
