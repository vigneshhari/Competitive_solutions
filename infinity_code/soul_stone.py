
num = input()
finish = {}
transfer = {}

answers = []

for i in range(1,num+1):
    val = raw_input().split(" ")
    if(val[-1] == "alien"):
        finish[i] = int(val[0])
    else:
        transfer[i] = int(val[0])
max_len = input()
'''
solve()

print answers
print finish,transfer
if( True ):
    print "RUN!"
else:
    print "Stay!"


'''
outs = []

def pathsolve( ):
    for i in range(1,num+1):
        solve(i, [i])


def solve(nums , seq):
    try:
        if(nums not in transfer.keys()):
            if(nums not in finish.keys()):return
            if(finish[nums] == num):
                outs.extend(seq)
                return
            return
        if( transfer[nums] in seq ) : return
        seq.append(transfer[nums])
        solve(transfer[nums] , seq )
    except:
        pass

pathsolve()
answers = []

if  (len( set(outs))  <= max_len): 
    print "RUN!"
else:
    print "Stay!"
