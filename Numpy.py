import warnings
warnings.filterwarnings('ignore')

import numpy as np
# print(np.__version__)

t= np.array([1,2,3,4,5,6,7,8,9])
p=np.array([3.14,6,8,9,2,6,8])

# print(t,p)

j= np.array([3.14,6,2,9,18,69], dtype='float32')
# print(j)

# Section 2 - Creating Arrays from Scratch
a=np.array([range(i,i+3) for i in [2,3,4]])
print(a)

bb=np.zeros(100,dtype=int)

tt=np.ones((3,5), dtype=float)

qw= np.full((3,5),3.14)

er= np.arange(0,20,2)

op= np.linspace(0,1,5)

np.random.random((3,3))

np.random.normal(0,1,(3,3))

np.random.randint(0,13,(3,3))

np.eye(3)

np.empty(3)

