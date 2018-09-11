#!/bin/python

#
# Complete the diagonalDifference function below.
#
def diagonalDifference(a):
    i, far , lar = 0,0,0
    while i < len(a):
        far += a[i][i]
        lar += a[i][len(a) - i -1]
        i += 1
    return abs(lar - far)

if __name__ == '__main__':

    n = int(raw_input())

    a = []

    for _ in xrange(n):
        a.append(map(int, raw_input().rstrip().split()))

    result = diagonalDifference(a)

    print result
