T = list(input())
S = list(input())

flag = True
for i in range(len(T)):
    if (S[i] in T):
        val = S[i]
        T.remove(val)
    else:
        flag = False
        print("NO")
        break
if flag == True:
    print("YES")
