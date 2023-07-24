S = list(input())

count = 1
for i in range(len(S)):
    if S[i] == '#':
        count -= 1
if count < 0:
    print("NO")
else:
    print("YES")
    
