import numpy as np

a=(1,2,3,4,5,6,7,8,9)
e=(1,2,['Math','Coding'])
print(a[0:5])
print(a[3:])
print(a[:])
print(e[2][:])

t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)
print(t1*2 + t2*3)

a = np.array([1,2,3,4,5])
b = np.where(a == 3)
print(b)
print(type(b))
print(b[0])
print(type(b[0]))
print(b[0][0])

# zip으로 쌍을 만드고 나면 tuple로 묶어 진다.
a=[1,2,3]
b=['a','b','c']
print(list(zip(a,b)))
print(tuple(zip(a,b)))

a=(1,2,3)
b=['a','b','c']
print(list(zip(a,b)))

a=[1,2,3]
b=['a','b','c']
c=['딸기','복숭아','참외']
d=list(zip(a,b,c))
print(d)
