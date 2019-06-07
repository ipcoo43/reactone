import numpy as np

plus = lambda x: x+5
plus(5)
plus(np.array([1,2,3,4,5]))

a=lambda x,y: x+y
a(2,6)

even = lambda x: x % 2 == 0
even(np.array([range(1,11)]))

list(filter(even,range(1,11)))

list(filter(lambda x:x%2==0, [3,1,4,2,9]))