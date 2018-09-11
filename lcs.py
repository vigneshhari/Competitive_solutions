raw_input()
string1 = raw_input().split()
string2 = raw_input().split()

def lcs(X , Y):
    m = len(X)
    n = len(Y)
 
    L = [[None]*(n+1) for i in xrange(m+1)]
    maxv = 0
    maxpos = -1
    temp = []
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
                if(L[i][j] >= maxv):
                    if(maxpos == -1 or L[i][j] > maxv ):
                        temp.append(X[i-1])
                        maxpos=j
                    else:
                        if( j < maxpos ):
                            del temp[-1]
                            temp.append(X[i-1])
                            maxpos=j
                    maxv = L[i][j]

            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
 
    return " ".join(temp)

print lcs(string1,string2)