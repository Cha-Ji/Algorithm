# Ex_11861
# 원형큐
# 조세퍼스 순열
class Queue:
    def __init__(self,n0,n1):
        self.data=[]
        for _ in range(n0):
            self.data.append(_+1)
        self.front=-1
        self.rear=n0
        self.jump=n1
    def pop(self):
        self.front=(self.front+self.jump)%self.rear
        item= self.data.pop(self.front)
        self.rear-=1
        self.front-=1
        return item
n=input().split()
q=Queue(int(n[0]),int(n[1]))
print("<",end="")
for _ in range(int(n[0])):
    if(_<int(n[0])-1):
        print(q.pop(),end=", ")
    else:
        print(q.pop(),end=">")