class cq:
    def __init__(self,n) -> None:
        self.q=[None for i in range(n)]
        self.n=n
        self.front=-1
        self.rear=-1

    def isempty(self):
        if self.front==-1:
            return True 
        else:
            return False 
    def isfull(self):
        if (self.rear+1)%self.n==self.front:
            return True
        else:
            return False
        
    def insert(self,x):
        if self.isfull():
            print("The queue is full..Cannot insert:",x)
            return 
        if self.isempty():
            self.front=0
            self.rear+=1
            print("Inserted ",x,"at:",self.rear)
            self.q[self.rear]=x
            
        else:
            self.rear+=1
            if self.rear>=self.n:
                self.rear=self.rear%self.n
            print("Inserted ",x,"at:",self.rear)
            self.q[self.rear]=x
            
    
    def delete(self):
        if self.isempty():
            print("Nothing there")
        elif self.front==self.rear:
            print("deleted",self.q[self.front])
            self.front=-1 
            self.rear=-1
            
        else:
            print("Deleted",self.q[self.front])
            self.front=(self.front+1)%self.n
            
    
    def display(self):
        print(self.front,self.rear)
        if self.isempty():
            print("Empty q")
            return
        elif self.rear>=self.front:
            for i in range(self.front,self.rear+1):
                print(self.q[i],end=" ")
        else:
            for i in range(self.front,self.n):
                 print(self.q[i],end=" ")
            for i in range(0,self.rear+1):
                 print(self.q[i],end=" ")

             

            print("\n")


        print("\n")

q1=cq(5)
q1.insert(1)
q1.display()
q1.insert(2)
q1.display()
q1.insert(3)
q1.display()
q1.insert(4)
q1.display()
q1.insert(5)
q1.display()
q1.delete()
q1.display()
q1.delete()
q1.display()
q1.delete()
q1.display()
q1.insert(6)
q1.display()
q1.insert(7)
q1.display()
q1.delete()
q1.display()
q1.insert(8)
q1.display()
q1.delete()
q1.display()
q1.delete()
q1.display()





    


            
            
        

            

