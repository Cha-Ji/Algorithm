#Ex_11021
# for문
# sep parameter / format
x=int(input())
for _ in range(x):
    A,B=map(int,input().split(" "))
    print("Case #{}: {}".format(_+1,A+B))