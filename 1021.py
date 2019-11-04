#Ex_1021
#원형
#array = [i for i in range(1,N+1)]
#나의 위치를 바꾸지 않고, 배열을 수정하는 방법
def move(p,num):
    right = 0
    left = 0
    while 1:
        if Deque[p] == num:
            left = len(Deque) - right
            break
        else:
            right+=1
            p+=1
    if right<left:
        if len(Deque) == 0:
            return 0,right
        return p,right
    else:
        if len(Deque) == 0:
            return 0, left
        return p,left

N,M = list(map(int,input().split(' ')))
Deque = [i for i in range(1,N+1)]
pick_num = list(map(int,input().split(' ')))
count = 0
for j in pick_num:
    target_index, distance = move(0,j)
    Deque = Deque[target_index+1:] + Deque[:target_index]
    count += distance
print(count)