from array import*
x=array('i',[2,8,7,9,3],)
temp=x[0]
for i in range(len(x)):
    if x[i-1]>x[i]:
        x[i]=x[i-1]
        temp=x[i]
        x[i-1]=temp
print("largest is :",x[i])