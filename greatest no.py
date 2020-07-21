from array import *
a=array('i', [])
n=int(input("enter length of array: "))
print("enter the value:")
for i in range(n):
    x = int(input(""))
    a.append(x)
temp=a[0]
for i in range(n):
    if temp <a[i]:
        temp=a[i]
print(a)
print("largest no is: ",temp)



for smallest no:-------

from array import *
a=array('i', [])
n=int(input("enter length of array: "))
print("enter the value:")
for i in range(n):
    x = int(input(""))
    a.append(x)
temp=a[0]
for i in range(n):
    if temp >a[i]:
        temp=a[i]
print(a)
print("largest no is: ",temp)




