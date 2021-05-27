#Ex_17298
#스택
TestCase = int(input())
arr=list(map(int,input().split(' ')))
stack=[]

result=[-1 for TestCase in range(len(arr))]

for i in range(len(arr)):
    while len(stack) !=0 and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = arr[i]
    stack.append(i)
print(*result)