#Ex_10845
#큐
#시간 초과
#sys.stdin.readline!!!!!!!!
import sys
class queue:
    def __init__(self):
        self.data=[]
    def size(self):
        return len(self.data)
    def empty(self):
        if(len(self.data)==0):return 1
        else:return 0
    def push(self, x):
        self.data.append(x)
    def pop(self):
        if len(self.data)==0: return -1
        else :
            return self.data.pop(0)
    def front(self):
        if len(self.data)==0: return -1
        else: return self.data[0]
    def back(self):
        if len(self.data)==0: return -1
        else: return self.data[-1]
T=int(sys.stdin.readline())

Q=queue()
for i in range(T):
    fn=input().split()
    if(fn[0]=='push'):
        Q.push(fn[1])
    elif(fn[0]=='front'):
        sys.stdout.write(str(Q.front()))
        sys.stdout.write('\n')
    elif(fn[0]=='back'):
        sys.stdout.write(str(Q.back()))
        sys.stdout.write('\n')
    elif(fn[0]=='pop'):
        sys.stdout.write(str(Q.pop()))
        sys.stdout.write('\n')
    elif(fn[0]=='size'):
        sys.stdout.write(str(Q.size()))
        sys.stdout.write('\n')
    elif(fn[0]=='empty'):
        sys.stdout.write(str(Q.empty()))
        sys.stdout.write('\n')