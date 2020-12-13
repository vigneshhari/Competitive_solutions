dat = raw_input() + " :"
val = raw_input()
sum = len(val) * -1
ans = dat.split(val)
if(len(ans) == 1 ):print "-1"
else:
    for i in ans[:-1]:
        sum = sum + len(i) + len(val)
    print sum