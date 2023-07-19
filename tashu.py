T = int(input())
for _ in range(T):
    N = int(input())
    A = [*map(int,input().split())]
    M = int(input())
    for i in range(M):
        u, v = map(int,input().split())
        u -= 1
        v -= 1
        A[u] -= 1
        A[v] += 1
    print(*A)
        
