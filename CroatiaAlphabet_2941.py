alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
S = input()

count = 0
i = 0
while i < len(S):
    if S[i] == 'c':
        if i+1 < len(S):
            if S[i+1] == '=':
                i += 1
            elif S[i+1] == '-':
                i += 1
    elif S[i] == 'd':
        if i+1 < len(S):
            if S[i+1] == '-':
                i += 1
            elif i+2 < len(S):
                if S[i+1] == 'z' and S[i+2] == '=':
                    i += 2
    elif S[i] == 'l':
        if i+1 < len(S):
            if S[i+1] == 'j':
                i += 1
    elif S[i] == 'n':
        if i+1 < len(S):
            if S[i+1] == 'j':
                i += 1
    elif S[i] == 's':
        if i+1 < len(S):
            if S[i+1] == '=':
                i += 1
    elif S[i] == 'z':
        if i+1 < len(S):
            if S[i+1] == '=':
                i += 1
    count += 1
    i += 1

print(count)