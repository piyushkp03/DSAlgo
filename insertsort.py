l=[5,3,1,7,2,8,0]
for i in range(1,len(l)):
    k=l[i]
    j=i-1
    x=False
    while(k<l[j] and j>=0):
        x=True
        l[j+1]=l[j]
        j-=1
    
    l[j+1]=k
print(l)