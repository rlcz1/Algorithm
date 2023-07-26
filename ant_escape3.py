T = int(input())

for j in range(T):
    N, M = map(int, input().split())
    S = input()
    J, O, G = 0, 0, 0
    
    if j < T-1: # 빈줄 받기
        input()
    for i in range(N):
        if S[i] == '@':
            J = i
        elif S[i] == 'O':
            O = i
        elif S[i] == 'G':
            G = i
    a = O - J
    b = G - J
    
    flag = False
    J_cnt = 0
    if a > 0: # a가 양수이면
        for i in range(J, O):
            if S[i] == '#':
                J_cnt += 1
    else: # a가 음수이면
        for i in range(J, O, -1):
            if S[i] == '#':
                J_cnt += 1
    if J_cnt <= M:
        flag = True
        print("YES")
    # 탈출구에서 벽을 못부셔서 탈출못했을때
    if flag == False:
        wall_cnt = 0
        if b > 0: # b가 양수이면
            for i in range(J, G):
                if S[i] == '#':
                    wall_cnt += 1
        else: # b가 음수이면
            for i in range(J, G, -1):
                if S[i] == '#':
                    wall_cnt += 1
        if wall_cnt <= M:
            flag = True
            print("YES")
            
    if flag == False:
        print("NO")       
