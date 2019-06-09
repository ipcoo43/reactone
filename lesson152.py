import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fractions import Fraction

weight = 22, 24, 26, 30, 32, 40, 35, 45, 20, 29, 34, 36, 36, 38, 39, 48, 43, 37, 33, 31, 29, 39, 26, 29

hist = np.zeros(6)
for i in weight:
    if i//5 == 4:    # 몸무게를 5로 나눈 몫이 4이면 20~25
        hist[0] += 1
    elif i//5 == 5:  # 몸무게를 5로 나눈 몫이 5이면 25~30
        hist[1] += 1
    elif i//5 == 6:  # 몸무게를 5로 나눈 몫이 6이면 30~35
        hist[2] += 1
    elif i//5 == 7:  # 몸무게를 5로 나눈 몫이 7이면 35~40
        hist[3] += 1
    elif i//5 == 8:  # 몸무게를 5로 나눈 몫이 8이면 40~45
        hist[4] += 1
    elif i//5 == 9:  # 몸무게를 5로 나눈 몫이 9이면 45~50
        hist[5] += 1
print(hist)

index = ['20~25', '25~30', '30~35', '35~40', '40~45', '45~50']
a = pd.Series(hist, index=index)
print(a)
print(type(a))

index = np.array([20,25,30,35,40,45]) + 2.5
b = pd.Series(hist, index=index, dtype=int)
print(b)

b.name = 'A반의 체중 도수분포표'
print(b)
print(a.index)
print(b.index)