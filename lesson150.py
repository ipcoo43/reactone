import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,10,1) 
for i in [2,-2]:
    plt.plot(x,i*x, label=f'y={i}x')
    plt.grid()
    plt.legend(fontsize=15, loc=8)

x=np.arange(-10,10,1)
plt.figure(figsize=(5,7))
for i in [1/2,0,2,8]:
    plt.plot(x, i*x, label=f'y = {i}x')
plt.grid()
plt.legend(fontsize=14,loc=4)

x=np.arange(-10,10,1)
plt.figure(figsize=(5,7))
for i in [-1/2,0,-2,-8]:
    plt.plot(x,i*x, label=f'y = {i}x')
plt.grid()
plt.legend(fontsize=14, loc=3)

x=np.arange(-10,10)
b=np.arange(-5,5,2)
for i in b:
    plt.plot(x, x+i, label='y = x + {}'.format(i))
plt.grid()
plt.legend(fontsize=13)