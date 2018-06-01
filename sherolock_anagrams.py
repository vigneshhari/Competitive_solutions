import operator as op
def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, xrange(n, n-r, -1), 1)
    denom = reduce(op.mul, xrange(1, r+1), 1)
    return numer//denom

def get_v_substr(string):
    out = {}
    finder = {}
    for i in range(1,len(string)):
        temp = 0
        while True:
            if(temp + i > len(string)  ):break
            val = "".join(sorted(string[temp:temp+i]))
            if(val in out.get(i, [] )):
                finder[val] = finder.get(val,1) + 1
            else:
                out[i] = out.get(i,[]) + [val]
            temp +=1
    return finder
for _ in range(input()):
    data = get_v_substr(raw_input())
    out = 0
    for i in data.values():
        out = out + ncr(i,2)
    print out 