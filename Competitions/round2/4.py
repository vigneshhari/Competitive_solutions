n = input()
for a in range(0,n):
    N = input()
    X = []
    Y = []
    for b in range(0,N):
        list = []
        list = raw_input().split(" ")
        X.append(float(list[0]))
        Y.append(float(list[1]))
    count = 0
    i = 0
    j = 1
    k = 2
    while k < len(X):
        ij = (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2
        jk = (X[j] - X[k]) ** 2 + (Y[j] - Y[k]) ** 2
        ik = (X[i] - X[k]) ** 2 + (Y[i] - Y[k]) ** 2
        if ij + jk == ik:
            count = count + 1
        i = j
        j = k
        k = k + 1
    print count