#회의실 배정
n = []
for i in range(int(input())):
    n.append(list(map(int, input().split(" "))))
    
n.sort(key = lambda x:(x[1], x[0]))

end, ans = -1, 0
for i in n:
    end, ans = (i[1], ans+1) if i[0] >= end else (end, ans)
print(ans)