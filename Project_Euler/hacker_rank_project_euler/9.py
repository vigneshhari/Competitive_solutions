

for _ in range(input()):
    inp = input()
    out = -1
    for i in range(1,inp  ):
        b = ((2 * inp * i) - (inp ** 2)) / ( (2 * i ) - (2 * inp) )
        c = inp - i - b
        if(c ** 2 == (i ** 2  + b **2)) :
            out = max(out , int(i * b * c ) )   
    if(out == 0 ):print -1
    else: print out