#Ex 5543
# if문 실습
burger = []
juice = []
for _ in range(3):
    burger.append(int(input()))
for _ in range(2):
    juice.append(int(input()))
result = 4000
for i in range(3):
    for j in range(2):
        result = min(result,burger[i]+juice[j])
print(result-50)

