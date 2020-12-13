def f(n):
    if(n%4 == 0):return n
    elif(n%4==1):return 1
    elif(n%4==2):return n+1
    elif(n%4==3):return 0

def answer(start,length):
    result = 0
    for i in xrange(length):
        result = result ^ f((start + i*length ) -1) ^  f(start + (i+1)*length -(i+1))
    return result

print answer(17,4000000)