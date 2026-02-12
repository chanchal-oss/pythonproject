import numpy as pd
arr=[1,2,3,4]
x=pd.array(arr)
print(x)
size=int(input("enter size of array which you want to make of that size"))
A=pd.empty(size)
#let size=2 then 2 size ki array means two elements ki array bana do
for i in range(size):
    n=int(input("enter the element of array"))
    A[i]=n
print(A)

#to print the garbage values in the array
s=int(input("enter size of new arr"))
new_arr=pd.empty(s)#ye array banayega ,put garbage values only
print(new_arr)

#to create an array not manually or by default ,giving row and columns then
r=int(input("enter rows"))
c=int(input("enter columns"))
new=pd.empty((r,c))
print(new)


