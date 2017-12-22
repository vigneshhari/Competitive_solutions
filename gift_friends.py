#for code monk .. P1 Q2

for i in range(0,input()):
    friends,gift = map(int ,raw_input().split(" "))
    friend_gift = []
    for friend in xrange(0,friends):
        friend_gift.append(input())
    print "START"
    for val in range(0,friends):
        tot_val = 0;
        for gifts in friend_gift[val:]:
            tot_val = tot_val + int(gifts)
            if(tot_val == gift):print "YES"
            if(tot_val >= gift):break
        if(tot_val == gift):break
    if(tot_val != gift ):print "NO"


