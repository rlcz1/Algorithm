import math
T = int(input())

for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    while True:
        flag = 0
        for j in range(N-1):
            if (A[j] > A[j+1]):
                A[j] = math.floor(A[j]/2)
                flag = 1
        if flag == 0: 
            break
    print(*A)
