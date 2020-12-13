def answer(n):
    counter = 0;num = long(n)
    while(num > 1):
        if num % 2 == 0:num = num / 2
        elif num == 3 or num % 4 == 1:num -= 1
        elif num % 4 == 3 :num += 1
        else:break
        counter += 1
    return counter