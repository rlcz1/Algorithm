import math

S = input()
len = len(S)
flag = True
for i in range(math.floor(len/2)):
    if (S[i] != S[len-i-1]):
        print("NO")
        flag = False
        break
if flag == True:
    print("YES")
        
        
