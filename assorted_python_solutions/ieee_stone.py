t = input()
for i in range(0,t):
    no = input()
    turns = 0
    for j in range(0,no):
        pile = input()
        pile_stone = [int(x) for x in raw_input().split()]
        for k in range(0,pile):
            if pile_stone[k]>1:
                turns += (pile_stone[k]-1)/2
    if turns % 2 == 0:
        print 'Bob'
    else:
        print 'Alice'