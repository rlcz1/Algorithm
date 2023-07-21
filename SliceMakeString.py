S = list(input())
T = list(input())
    
flag = True
i = 0
while i < len(T):
    if T[i] in S:
        val = T[i]
        idx = S.index(val)
        S = S[idx:]
    else:
        flag = False
        print("NO")
        break
    i += 1
if flag:
    print("YES")
