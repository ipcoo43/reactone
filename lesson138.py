# 1부터 24까지 정수로 이루어진 (6,4) 크기의 array 만들고
# 각 원소에다가 행의 index를 곱하고
# 열의 index로 더한 숫자를 원소로하는 2차원 array

import numpy as np
a = np.array(range(1,25)).reshape(6,4)
for i in range(6):
    for j in range(4):
        a[i,j] = (a[i,j]*i) + j
print(a)
