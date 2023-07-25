T = int(input())

for j in range(T):
    N, M = map(int, input().split())
    S = input()
    J = 0 
    O = 0
    if j < T-1: # 빈줄 받기
        input()
    for i in range(N):
        if S[i] == '@':
            J = i
        elif S[i] == 'O':
            O = i
    if J > O:
        for i in range(J, O, -1):  
            if S[i] == '#':
                M -= 1
    else:
        for i in range(J,O):
            if S[i] == '#':
                M -= 1
    if M < 0:
        print("NO")
    else:
        print("YES")
