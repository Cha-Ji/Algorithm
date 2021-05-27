#Ex_1874
#스택 수열
class Stack:
    def __init__(self):
        self.data=[]
    def size(self):
        return len(self.data)
    def push(self,item):
        self.data.append(item)
    def pop(self):
        return self.data.pop()
    def peek(self):
        if(self.size()==0):
            return -1
        else:
            return self.data[-1]

sorting_arr=[]
print_arr=[]
checking_arr=Stack()

test_case=int(input())
#input
i = 1
while i <= test_case:
    sorting_num = int(input())
    sorting_arr.append(sorting_num)
    i += 1

#check
i=1
j=0
while i<=test_case:
    checking_arr.push(i)
    print_arr.append("+")
    while sorting_arr[j]==checking_arr.peek() and j<test_case-1:
        checking_arr.pop()
        print_arr.append("-")
        j+=1
    i+=1
print_arr.append('-')
#print & push,pop
if(checking_arr.size()==1):
    i=0
    while i<len(print_arr):
        print(print_arr[i])
        i+=1
else:
    print("NO")