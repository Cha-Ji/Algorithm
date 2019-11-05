#Ex_3052
# list
N=[]
for i in range(10):
    N.append(int(input())%42)
    for j in range(len(N)-1):
        if(N[j]==N[-1]):
            N.pop()
            break
print(len(N))