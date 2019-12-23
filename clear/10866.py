#Ex_10866
#덱
#sys출력형식을 사용해야 시간복잡도가 훨씬 짧다.

import sys

class Deque:
    def __init__(self):
        self.data=[]
    def push_front(self,X):
        self.data.insert(0,X)
    def push_back(self,X):
        self.data.append(X)
    def pop_front(self):
        if(len(self.data)==0):
            return -1
        else:
            return self.data.pop(0)
    def pop_back(self):
        if(len(self.data)==0):
            return -1
        else:
            return self.data.pop()
    def size(self):
        return len(self.data)
    def empty(self):
        if(len(self.data)==0):
            return 1
        else:return 0
    def front(self):
        if(len(self.data)==0):
            return -1
        else:return self.data[0]
    def back(self):
        if(len(self.data)==0):return -1
        return self.data[-1]
N = int(input())
q=Deque()
for _ in range(N):
    do = sys.stdin.readline().split()
    if(do[0]=='push_back'):
        q.push_back(int(do[1]))
    elif(do[0]=='push_front'):
        q.push_front(int(do[1]))
    elif(do[0]=='pop_front'):
        sys.stdout.write(str(q.pop_front()))
        sys.stdout.write('\n')
    elif(do[0]=='pop_back'):
        sys.stdout.write(str(q.pop_back()))
        sys.stdout.write('\n')
    elif(do[0]=='size'):
        sys.stdout.write(str(q.size()))
        sys.stdout.write('\n')
    elif(do[0]=='front'):
        sys.stdout.write(str(q.front()))
        sys.stdout.write('\n')
    elif(do[0]=='back'):
        sys.stdout.write(str(q.back()))
        sys.stdout.write('\n')
    elif(do[0]=='empty'):
        sys.stdout.write(str(q.empty()))
        sys.stdout.write('\n')