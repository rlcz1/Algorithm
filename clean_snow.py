N = int(input())

r1, c1, r2, c2 = map(int, input().split())
arr = [['*' for j in range(N)] for i in range(N)]

if r1 > r2:
    temp = r1
    r1 = r2
    r2 = temp
if c1 > c2:
    temp = c1
    c1 = c2
    c2 = temp


for i in range(r1-1, r2):
    for j in range(c1-1, c2):
        arr[i][j] = '.'

for i in range(N):
    for j in range(N):
        print(arr[i][j], end='')
    print()

