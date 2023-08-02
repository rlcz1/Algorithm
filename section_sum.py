N, M = map(int, input().split())

arr = list(map(int, input().split()))

for _ in range(M):
    L, R = map(int, input().split())
    sum = 0
    for i in range(L-1, R):
        sum += arr[i]
    print(sum)
