def isfull(top, n):
    if top==n-1:
        return True
    else:
        return False
def isempty(top):
    if top==-1:
        return True
    else:
        return False


class Stack:
    def __init__(self,n):
        self.top=-1
        self.s=[]
        self.n=n

    def pushx(self,x):
        if(isfull(self.top,self.n)):
            print("Stack is full")
        else:
            self.top+=1
            self.s.insert(self.top,x)
            print("Inserted ",x)

    def popx(self):
        if(isempty(self.top)):
            print("Stack is empty!!")
        else:
            val=self.s[self.top]
            print("deleted ",val)
            self.top-=1
    def traverse(self):
        if(isempty(self.top)):
            print("Empty Stack!!")
        else:
            for i in range(self.top+1):
                print(self.s[i],end=" ")
            print("\n")


n=int(input("Enter stack size"))
s1=Stack(n)
while(1):
    choice=int(input("1.Insert 2.Delete 3.Display 4.Exit"))
    if choice==1:
        x=input("Enter an element to insert")
        s1.pushx(x)
    elif choice==2:
        s1.popx()
    elif choice==3:
        s1.traverse()
    elif choice==4:
        break
    else:
        print("Invalid option!")














