class Cls:

    def __init__(self,id):
        self.id=id

obj=Cls(5)

obj.__dict__['count']=10
print(obj.count+len(obj.__dict__))
