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

pp= np.linspace(0,1,5)

np.random.random((3,3))

np.random.normal(0,1,(3,3))

op=np.random.randint(0,13,(3,3))

np.eye(3)

np.empty(3)

op.ndim

op.shape

op.size

op.dtype

op.itemsize

op.nbytes

op[:2,:3]

op[:,0] #first column

op[0,:] #first row 

s = np.array([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
])

b=np.sum(s,axis=1)
b == 45
# or
for i in b:
    if i!=45:
        print("sudoku is not valid")
        break
else:
    print("for rows it is valid")

c= np.sum(s,axis=0)
for i in c:
    if i!=45:
        print("sudoku is not valid")
        break
else:
    print("for columns it is valid")


for i in range(0,9,3):
    for j in range(0,9,3):
          arr=s[i:i+3,j:j+3]
          sum=np.sum(arr)
          if sum!=45:
              print("it is not valid" )
              break


import numpy as np

# Columns: [Age, Math Marks, Science Marks]
data = np.array([
    [18, 85, 78],   # Student 1
    [19, 92, 88],   # Student 2
    [17, 76, 95],   # Student 3
    [18, 65, 70],   # Student 4
    [20, 90, 85]    # Student 5
])

#Get the shape of the matrix.
data.shape


#Find the average age of students.
sa=data[:,0]
np.sum(sa)/len(sa)

np.mean(data[:,0])


#Extract Math marks of all students.
mm=data[:,1]

#Find the highest Science mark.
np.max(data[:,2])


#Get details of the student who scored more than 90 in Math.
data[data[:,1]>90]
