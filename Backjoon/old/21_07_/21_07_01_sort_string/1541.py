# Ex_1541 잃어버린 괄호 [실2]

num = input().split('-')
ans = 0
end = 1
for minus in num:
    ans -= sum(map(int, minus.split('+'))) * end
    end = -1
print(ans)
