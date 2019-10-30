#Ex_10845
#큐
#시간 초과
#pop(0)은 밀어내기 때문에 연산이 느리다.
#rear없이 front만 있으면 비효율적이다.
#import sys를 사용하자
import sys
class queue:
    def __init__(self):
        self.data=[]
        self.head=-1
        self.count=0
        self.rear=-1
    def size(self):
        return self.count
    def empty(self):
        if(self.count==0):return 1
        else:return 0
    def push(self, x):
        self.count+=1
        self.rear+=1
        self.data.append(x)
    def pop(self):
        if self.empty(): return -1
        else :
            self.head+=1
            self.count-=1
            return self.data[self.head]
    def front(self):
        if self.empty(): return -1
        else: return self.data[self.head+1]
    def back(self):
        if self.empty(): return -1
        else: return self.data[self.rear]
T=int(sys.stdin.readline())

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
