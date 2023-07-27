T = int(input())

for j in range(T):
    N, M = map(int, input().split())
    S = list(input())
    J = list(map(int, input().split()))  # 준식 ATK, HP
    MS = list(map(int, input().split()))  # 몬스터 ATK, HP

    start = S.index('@')

    if j < T - 1:  # 빈줄 받기
        input()

    t = MS
    flag = False
    fb = True
    cnt = 0
    for i in range(start, -1, -1):
        if S[i] == '#':
            cnt += 1
        elif S[i] == 'O':
            print("YES")
            flag = True
            break
        elif S[i] == '&':
            while True:
                MS[1] -= J[0]
                if MS[1] < 1: # 몬스터의 체력이 0이하
                    break
                J[1] -= MS[0]
                if J[1] < 1:
                    fb = False
                    break
        if not fb:
            break
        if cnt > M:
            break

    cnt = 0
    MS = t
    fb = True
    if not flag:
        for i in range(start, N):
            if S[i] == '#':
                cnt += 1
            elif S[i] == 'O':
                print("YES")
                flag = True
                break
            elif S[i] == '&':
                while True:
                    MS[1] -= J[0]
                    if MS[1] < 1: # 몬스터의 체력이 0이하
                        break
                    J[1] -= MS[0]
                    if J[1] < 1:
                        fb = False
                        break
            if not fb:
                break
            if cnt > M:
                break
    if not flag:
        print("NO")
