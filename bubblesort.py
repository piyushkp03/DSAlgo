import time

t1=time.time()

l=[2,9,1,2,3,5,8,6]

for i in range(len(l)):
    for j in range(1,len(
            l)):
        if l[j]<l[j-1]:
            tmp=l[j]
            l[j]=l[j-1]
            l[j-1]=tmp
print(l)
t2=time.time()
print("The execution time is:",t2-t1)