arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
arr2 = [0 for i in range(26)]

S = input()
for i in range(len(S)):
    if (S[i] in arr):
        idx = arr.index(S[i])
        arr2[idx] += 1
flag = True
for i in range(len(arr2)):
    if arr2[i] == 0:
        print("NO")
        flag = False
        break
if flag == True:
    print("YES")
