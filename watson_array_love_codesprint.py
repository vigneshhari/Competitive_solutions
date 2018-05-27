for _ in range(input()):
    n , m , k = map(int , raw_input().split())
    counter = 0
    array = map(int , raw_input().split())
    pos = 0
    temper = 1
    temp_prod = 1
    crazy = 0
    for i in array:
        temp = i - m * (i//m)
        temp = temp - k
        if(temp == 0):
            counter += (len(array) - pos) * temper
            temper = 1
            temp_prod = 1
            counter += crazy
            crazy = 0
        else:
            temper+=1
        pos+=1
        #print temp,
    print counter