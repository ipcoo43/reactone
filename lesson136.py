import numpy as np

def nprint(arr):
    print(f'type  : {type(arr)}')
    print(f'shape : {arr.shape}')
    print(f'ndim : {arr.ndim}')
    print(f'dtype : {arr.dtype}')
    print(f'Data :\n {arr}')
    
a=np.array([1,2,3,4,5])
nprint(a)
print() 

b=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
nprint(b)

b.shape
print(b[0,0], b[0,1], b[1,0],b[3,2],b[-1,0],b[0,-1],b[-1,-1])
print(b[:,0])
print(b[:,4])
print(b[0,:])
print(b[2,:])
print(b[:])
print(b[1:3,2:4])

c = range(1,26)
c = np.array(c)
print(c.shape)
print(c)
c = np.array(range(1,26)).reshape(5,5)
c

print(np.zeros(5))
print(np.ones(5))

print(np.zeros((2,4)))
print(np.ones((2,4)))
