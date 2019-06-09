# 부등식
# 60L 의 물이 들어 있는 600L 욕조에 물을 더 받으려 한다.
# 매분 30L 물을 받는다고 할때
# x분 동안 물을 더 받는다고 할 때
# 60 + 30x < 600
# x가 집합 [2,3,5,7]의 원소일때 다음 부등식
# 3x + 2 <= 11
x=[2,3,5,7]
a=[]
for i in x:
    if 3*i + 2 <= 11:
        a.append(True)
    else:
        a.append(False)
print(a)

x=[2,3,5,7]
a=[3*i+2<=11 for i in x]
print(a)

x=[2,3,5,7]
a=[i for i in x if 3*i+2 <= 11]
print(a)

# 4x - 5 > 13
x=[2,3,5,7]
a=[i for i in x if 4*i - 5 > 13 ]
print(a)

# 2x + 1 < 15
x=[2,3,5,7]
a=[i for i in x if 2*i + 1 < 15]
print(a)

# x+5 >= 4
import numpy as np
x = np.arange(-10,11)
b = lambda a: a+5 >= 4
print(b(x))
b=list(filter(lambda a: a+5 >= 4, x))
print(b)

# x-4 <= -3
y = list(filter(lambda a: a - (-4) <= -3, np.arange(-10,11,1)))
print(y)

# 2/3*x >= -4
y=list(filter(lambda a: 2/3*a >= -4, np.arange(-10,11,1)))
print(y)

# x + 5 >= 4
x = np.arange(-10,11)
a=[]
for i in x:
    if i+5 >=4:
        a.append(i)
print(a)