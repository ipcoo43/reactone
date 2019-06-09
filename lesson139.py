import numpy as np

b = [3,4,5,6,7]
b.index(6)  # 3
# array에서 index 사용 할 수 없다
c = np.array(b)
print(np.where(6 == c))
print(np.where(6 == c)[0][0])

a = np.array([3,4,5,7,3,1,3])
np.where(3==a)

a = np.array([-3,4,7,2,5])
print(max(a))
print(min(a))

c = np.array(range(1,26)).reshape(5,5)
c
cmax = np.max(c)
print(f'max : {cmax}')
cmax_index = np.where(cmax == c)
print(f'cmax_index : {cmax, cmax_index}')

sum([3,2,4])
sum(np.array([3,2,4]))
np.sum([3,2,4])
np.sum(np.array([3,2,4]))

np.arange(10)
type(np.arange(10))
np.arange(10)+7
