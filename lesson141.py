import numpy as np

# 높이가 h, 밑변이 a인 삼각형의 넓이
def triangle_area(a,h):
    return 1/2*a*h
a=3
h=5
print(triangle_area(a,h))

# 높이(h)와 밑변(a)이 1부터 10까지 변할때 삼각형의 넓이
a=np.array(range(1,11))
h=np.array(range(1,11))
area = np.zeros((len(a),len(h)))
print(area.shape) # (10,10)
for i in a:
    for j in h:
        area[i-1,j-1] = triangle_area(i,j)
print(area)

triangle_area2 = lambda a,h : 0.5*a*h
print(triangle_area2(10,5))