#Ex_10845
#큐
#시간 초과
class queue:
    def __init__(self):
        self.data=[]
    def size(self):
        return len(self.data)
    def empty(self):
        if(self.size()==0):return 1
        else:return 0
    def push(self, x):
        self.data.append(x)
    def pop(self):
        if self.empty(): return -1
        else :return self.data.pop(0)
    def front(self):
        if self.empty(): return -1
        else: return self.data[0]
    def back(self):
        if self.empty(): return -1
        else: return self.data[-1]
T=int(input())
Q=queue()
for i in range(T):
    fn=input().split()
    if(fn[0]=='push'):
        Q.push(fn[1])
    elif(fn[0]=='front'):
        print(Q.front())
    elif(fn[0]=='back'):
        print(Q.back())
    elif(fn[0]=='pop'):
        print(Q.pop())
    elif(fn[0]=='size'):
        print(Q.size())
    elif(fn[0]=='empty'):
        print(Q.empty())
    else:print()