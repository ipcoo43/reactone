import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

a={'name':'철수','age':15,'hobby':'baseball'}
print(a)
print(a['name'])
print(a['age'])
print(a['hobby'])
a['phone']='0102222333'
print(a)
del a['phone']
a
a.keys
a.values
print(list(a.keys()))
print(tuple(a.values()))
a.get('phone') == None
a.get('age')
'age' in a
'phone' in a
