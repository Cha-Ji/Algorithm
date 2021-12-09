# Ex_2243 사탕상자: [플5]

def addCandy(favor, num, index):
    if tree[index][1] == -1:
        tree[index] = [0, favor]
        return

    if tree[index][1] < favor:
        tree[index][0] += num
        tree[index][1] = favor
        addCandy(favor, num, index * 2 + 1)
    
    else:
        tree[index][0] += num
        addCandy(favor, num, index * 2)

def delCandy(favor, num, index):
    if tree[index][1] < favor:
        tree[index][0] -= num
        delCandy(favor, 1, index * 2 + 1)
    

n = int(input())
tree = [[0, -1] for _ in range(n)] # [자식 개수, 최대값]
for _ in range(n):
    order = list(map(int, input().split()))
    
    # 사탕을 꺼내는 경우
    if order[0] == 1:
        delCandy(order[1], 0, 1)
    
    # 사탕을 넣는 경우
    if order[1] == 2:
        addCandy(order[1], order[2], 1)