T = int(input())

for j in range(T):
    N, M, K = map(int, input().split()) # 길이N, 부술수있는 벽M, 몬스터 수K
    S = list(input())
    J = list(map(int, input().split()))  # 준식 ATK, HP
    MS = [] # 몬스터들의 ATK, HP
    for i in range(K):
        MS.append(list(map(int, input().split()))) #위치, 공격력, 체력

    start = S.index('@')

    if j < T - 1:  # 빈줄 받기
        input()
        
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
            target = []
            for k in range(len(MS)):
                if MS[k][0] == i+1:
                    target = MS[k]
            while True:
                target[2] -= J[0]
                if target[2] < 1: # 몬스터의 체력이 0이하
                    break
                J[1] -= target[1]
                if J[1] < 1:
                    fb = False
                    break
        if not fb:
            break
        if cnt > M:
            break

    cnt = 0
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
                target = []
                for k in range(len(MS)):
                    if MS[k][0] == i+1:
                        target = MS[k]
                while True:
                    target[2] -= J[0]
                    if target[2] < 1: # 몬스터의 체력이 0이하
                        break
                    J[1] -= target[1]
                    if J[1] < 1:
                        fb = False
                        break
            if not fb:
                break
            if cnt > M:
                break
    if not flag:
        print("NO")
