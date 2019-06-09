# 연립 방정식 : 미지수가 여러개인 방정식
# a1x + b1y = c1 (eq1)
# a2x + b2y = c2 (eq2)
# x + 2y/3 = 8 (eq2*2)
# (eq1)-(eq2*2) = 5y - 2y/3 = 13y/3 = 12
# y = 36/13
from fractions import Fraction
import numpy as np

a = [1, 5, 20]
b = [Fraction(1,2), Fraction(1,3), 4]
c = b*2
print(c)
a=np.array(a)
b=np.array(b)
c = b*2
print(c)

d = a-c
y = Fraction(d[2],d[1])
x = Fraction((a[2]-a[1]*y),a[0])
print(x,y)

def simultaneous_eq(a,b):
    if a[0] ==0:
        y = Fraction(a[2],a[1])
        x = Fraction(b[2]-b[1]*y, b[0])
    elif a[1] ==0:
        x = Fraction(a[2],a[0])
        y = Fraction(b[2]-b[0]*x, b[1])
    elif b[0] ==0:
        y = Fraction(b[2],b[1])
        x = Fraction(a[2]-a[1]*y, a[0])
    elif b[1] ==0:
        x = Fraction(b[2],b[0])
        y = Fraction(a[2]-a[0]*x, a[1])
    else:
        a = np.array(a)
        b = np.array(b)
        c = b * Fraction(a[0],b[0])
        d = a - c
        y = Fraction(d[2],d[1])
        x = Fraction(a[2]-a[1]*y, a[0])
    return x, y
# 5x + 2y = 14
# 2x + y = 4
a = [5,2,14]
b = [2,1,4]
x,y=simultaneous_eq(a,b)
print(x,y)   

# 2x + 3y = 4
# 3x + -4y = -4
a = [2,3,4]
b = [3,-4,-4]
x,y = simultaneous_eq(a,b)
print(x,y)

a = [1,3,4]
b = [5,0,-10]
x,y = simultaneous_eq(a,b)
print(x,y)

 
