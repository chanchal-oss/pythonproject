#numpy attributes and the functions

import numpy as np
arr=[[1,2,3],[4,5,6],[7,8,9]]#2D array #shape->(2,3)
x=np.array(arr) # or x=np.array(arr,dtype='d') to change the data type
print(x)

#ndim attribute

print(x.ndim)# or dimension=np.ndim(x)  print(dimension)

#shape attribute

print(x.shape)

#size attribute gives the no. of elements having

print(x.size)

#dtype attribute

print(x.dtype)

#itemsize attribute which tells one element memory (in bytes)

print(x.itemsize)

#slicing 

print(x[0:3])

#indexing

print([0,1])

#indexing+slicing

print(x[0,1:2])

#nbytes attribute gives -> itemsize*size

print(x.nbytes)

#fancy index-> gives value of given array of indexes

indices=[0,1,2]
print(x[indices])#or print(x[[0,1,2]])

#boolean masking -> Condition check → True/False array → True positions ke values select hoti hain

y=x>2
print(y)
print(x[y])
i=0
while i<3:
    print(x[i])
    i+=1

#linspace function->numbers ke beech equally spaced values generate karta hai

print(np.linspace(1,10,5))

#zeros-> gives matrix of zeros only

a=np.zeros((2,2),dtype="i")# or print(np.zeros((2,2)))
print(a)

#making a copy by copy function so that original array will not get affected

b=x[0:3].copy()
b[0,1]=30
print("copied one->\n",b)
print("original one->\n",x,"\n")

#broadcasting

y=np.array([[1,2,3],[2,5,6]])
print(y.shape) #shape->(2,3)

z=np.array([[1,0,0],[2,0,1]])
print(z.shape)
print(y+z)