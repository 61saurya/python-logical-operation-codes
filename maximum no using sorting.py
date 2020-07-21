from array import*
x=array('i',[2,8,7,9,3],)
temp=x[0]
for i in range(len(x)):
    if x[i-1]>x[i]:
        x[i]=x[i-1]
        temp=x[i]
        x[i-1]=temp
print("largest is :",x[i])




-----users input------

from array import *
x=array('i', [])
n=int(input("enter length of array: "))
print("enter the value:")
for i in range(n):
    a = int(input(""))
    x.append(a)
print(x)
temp=x[0]
for i in range(n):
    if x[i - 1] > x[i]:
        x[i] = x[i - 1]
        temp = x[i]
        x[i - 1] = temp
print("largest is :", x[i])