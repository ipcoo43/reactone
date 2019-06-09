# 행에는 0,5,10,15,20을 더하고
# 열에는 1,3,5,7,9를 더하는 2차원 배열 생성

import numpy as np
a = np.zeros((5,5)) # 5*5 크기를 가지는 a라는 변수를 생성하고
for idx1,val1 in enumerate(range(0,25,5)): # [0,5,10,15,20]
    for idx2,val2 in enumerate(range(1,10,2)): # [1,3,5,7,9]
        a[idx1, idx2] = val1 + val2
print(a)

