import numpy as np

lst1 = [1,2,3,4]
a=np.array(lst1)
a.shape

lst2 = [[1,2,3],[4,5,6]]
b=np.array(lst2)
b.shape

c=np.zeros((2,2))
c

d=np.ones((2,2))
d

e=np.full((2,3),5)
e

f=np.eye(3)
f

g=np.array(range(20)).reshape((4,5))
g
