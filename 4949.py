class Stack:
    def __init__(self):
        self.data=[]
    def push(self,item):
        self.data.append(item)
    def pop(self):
        return self.data.pop()
    def peek(self):
        return self.data[-1]
    def size(self):
        return len(self.data)
box_check = Stack()
check_string=[]
while True:
    temp=input()
    if(temp=='.'):break
    check_string+=temp
i=0
while(i<len(check_string)):
    box_check.__init__()
    check = 1
    while (check_string[i] != '.'):
        if (check_string[i] == '(' or check_string[i] == '['):
            box_check.push(check_string[i])
        elif (check_string[i] == ')' ):
            if(box_check.size()==0):
                check = 0
            elif (box_check.peek() == '('):
                box_check.pop()
            else:
                check = 0
        elif (check_string[i] == ']'):
            if (box_check.size() == 0):
                check = 0
            elif (box_check.peek() == '['):
                box_check.pop()
            else:
                check = 0
        i += 1
    if (check == 0):
        print("no")
    elif (box_check.size() == 0):
        print("yes")
    else:
        print("no")
    i+=1
