N = int(input())
S = list(input())

max = 0
for i in range(N-1):
    a = S.copy()
    b = S.copy()
    a = set(a[:i+1])
    b = set(b[i+1:])
    
    if max < len(a) + len(b):
        max = len(a) + len(b)
print(max)
