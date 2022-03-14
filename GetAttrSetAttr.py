class Cls:
    def __init__(self,x,y):
        self.a=x+y
x=Cls(1,2)
y=getattr(x,'a')
print(y)
setattr(x,'a',y+1)
print(x)
print(x.a)
