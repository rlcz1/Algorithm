T = int(input())

for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    val = 0
    for idx in range(1, N-1):
        if arr[idx] != arr[idx-1] and arr[idx] != arr[idx+1]: # idx와 idx-1이 다르고, idx와 idx+1이 다르면 idx저장
            val = idx+1 # 몇번째인지 위치 출력이므로 idx+1
            break
    else:
        if arr[0] != arr[1]:
            val = 1
        else:
            val = N
    print(val)
