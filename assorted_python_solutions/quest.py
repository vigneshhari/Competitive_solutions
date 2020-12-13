#for code monk .. P3 Q1

blah,q = [int(x) for x in raw_input().split(" ")]
data = [int(x) for x in raw_input().split(" ")]
data.sort()
for i in xrange(0,q):
    print i
    val = int(input())
    for dat in data:
        if(val == dat):print "YES"
        if(val < dat):print "NO";break
