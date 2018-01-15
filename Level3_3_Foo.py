
steps = 0

#Grandest Staircase

def memoize(f):

    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)

@memoize
def step(num):
    ss=0
    if(num <= 2):return 0
    if(num < 5):return 1
    for i in range(num-1,0,-1):
        if ((num - i) > i  ):ss = ss + smallsteps(i,num-i);continue
        elif(i == (num - i)):pass
        else:ss += 1
        temp = step(num - i)
        ss = ss + temp
    return ss

def natsum(n):return ((n*(n+1))/2)

@memoize
def smallsteps(num,lim):
    sum = 0
    if(natsum(num-1) < lim):return 0
    for i in range(num - 1 , 0 , -1):
        if(i > lim):continue
        nlim = lim - i
        if(nlim == 0):sum = sum + 1
        else:sum = sum + smallsteps(i,nlim)
    return sum

print step()
