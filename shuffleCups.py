N, M = map(int, input().strip().split(' '))
nl = list(range(1, N+1))
for i in range(M):
    u, v = map(int, input().strip().split(' '))
    temp = nl[u-1]
    nl[u-1] = nl[v-1]
    nl[v-1] = temp
print(*nl)
