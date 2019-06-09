import numpy as np

def plus(a,b):
    return a+b
print(plus(4,9))

def plus_args(*args):
    return np.sum(np.array(args))
print(plus_args(3,6,9))
print(plus_args(3,15,6,4,7))

def plus_multiple(a,*b):
    return a*np.sum(np.array(b))
print(plus_multiple(3,6,9))
print(plus_multiple(3,1,5,6,4,7))

def plus_multi(a,*b):
    n = len(b)
    for i in range(n):
        print(b[i])
    return a*np.sum(np.array(b))
print(plus_multi(3,1,5,6,4,7))

def plus_a(*args):
    print(np.sum(np.array(args)))
plus_a(3,6,9)

def plus_with_5(a,b,c=5):
    return a+b+c
print(plus_with_5(1,2))
print(plus_with_5(1,2,10))

def calcul(a,b,c=5, d=10,e=15):
    return a+b-c+d-e
print(calcul(1,2,d=3,c=10,e=0.1))

def custom_zip(a,b):
    if len(a) != len(b):
        print('두 입력값이 길이가 다릅니다.')
    else:
        n=len(a)
        c=[]
        for i in range(n):
            c.append((a[i],b[i]))
        return c
a=[1,2,3]
b=['a','b','c']
print(custom_zip(a,b))