N = int(input())
S = list(map(int, input().split()))

for i in range(N):
    low = 0
    high = 0
    for j in range(N):
        if S[i] > S[j]:
            low += 1
        elif S[i] < S[j]:
            high += 1
    print(low, high)
print()
