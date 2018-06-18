
missing = -1

def numberlength(number):
    out = 0 
    if(number == 0 ) :return 1 
    while number != 0:
        number = number // 10
        out += 1
    return out  


def checker(number , pos , l):
    temp = 1
    fin = 0
    mover = pos +  numberlength(number) - 1
    while mover >= pos :
        if(mover >= len(l)): return False
        fin = fin +  temp*l[mover]
        temp = temp * 10
        mover -=1
    if(fin == number):return True
    return False

def completed( number , listpos, intstr , chance  ):
    if(listpos  == len(intstr)  ):return True
    correct = checker(number , listpos , intstr)
    if(correct == False and chance == 0):return False
    if(correct == False and chance == 1):
        global missing
        missing = number 
        return completed(number+1 , listpos , intstr , 0)
    return completed(number+1 , numberlength(number) + listpos ,intstr ,  chance )


def getnum(length , l):
    temp = 1
    fin = 0
    mover = length
    while mover >= 0 :
        fin = fin +  temp * l[mover]
        temp = temp * 10
        mover -=1
    return fin

def missingNumber(string):
    global missing
    missing = -1
    l = list(map(int , list(string)))
    done = True
    for i in range(0,(len(string)//2) + 1 ):
        if(completed(getnum(i,l)+1 ,i+1 , l , 1  ) == True):
            if(missing == -1):return -1
            return missing
            done = False
            break
        missing = -1
    if(done == True):return -1



if __name__=='__main__':
    t = int(input())
    for i in range(t):
        string = input().strip()
        print(missingNumber(string))
