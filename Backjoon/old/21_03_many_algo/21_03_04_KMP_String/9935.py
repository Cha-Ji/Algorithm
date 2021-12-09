# Ex_9935 문자열 폭발 [골4]
txt, bomb = input(), input()

lenB = len(bomb)
stack = [""]
for c in txt:
    if c == bomb[0] or len(stack[-1]) > lenB:
        stack.append(c)
    else:
        stack[-1] += c

    if stack[-1] == bomb:
        stack.pop()

print(*stack if stack[-1] else "FRULA", sep="")
