import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fractions import Fraction

index = ['a', 'b', 'c', 'd', 'e']
s = pd.Series(np.random.randn(5), index=index)
print(s)
print(s+s)
print(s*2)
print(s**2)

d = {'a':0., 'b':1., 'c':2.}
f = pd.Series(d)
print(f)
print(f[0])
print(f[:])
print(f['a'])
'b' in f
'd' in f
f.get('a')

weight = [22, 24, 26, 30, 32, 40, 35, 45, 20, 29, 34, 36, 36, 38, 39, 48, 43, 37, 33, 31, 29, 39, 26, 29]

height = [124, 125, 128, 130, 134, 140, 131, 143, 122, 129, 136, 139, 141, 135, 142, 150, 149, 141, 127, 131, 130, 125, 135, 126]

len(weight)
len(height)

d = {'weight':pd.Series(weight), 'height':pd.Series(height)}
e = pd.DataFrame(d)
print(e)

f = np.zeros((len(weight),2))
f[:,0] = weight
f[:,1] = height
g = pd.DataFrame(f,columns=['weight','height'])
print(g)
g.name='A반의 몸무게와 키'
print(g.name)
print(e['weight'])
weight = [34,36,75]
height = [144,151,178]
wh = list(zip(weight, height))
index = ['철수','영희','선생님']
h = pd.DataFrame(wh, index=index, columns=['몸무게','키'])
print(h)

h.loc['철수']
h.iloc[0]
h.columns
h.index
