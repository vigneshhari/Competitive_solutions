


def recsol(a,b,lev):
    if (a <= 0 or b <= 0): return
    if (a == 1 and b == 1): return lev
    if(a > b and (( a / b ) -1) > 0 ):
        time = (a / b) -1
        a = a - b * ((a / b) - 1)
        return recsol(a, b, time + lev)
    elif(b> a and (( b / a ) -1) > 0 ):
        time = (( b / a ) ) -1
        b = b - a * (( b / a ) - 1)
        return recsol(a, b,time + lev)
    return recsol(a-b,b,lev+1) or recsol(a,b-a,lev+1)

def answer(M, F):
    M = int(M)
    F = int(F)
    if(M > 10 ** 50 or F > 10 ** 50 or M < 0 or F < 0):return "-1"
    val = recsol(M,F,0)
    if(val == None):return "impossible"
    else: return str(val)
