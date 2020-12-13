a,count = map(int , raw_input().split())
ans = {}
for i in range(count):
    data = list(raw_input().split())
    if(len(data) == 1):ans = {}
    else:
        data = data[1]
        if(ans.pop(data, True) ):
            ans[data] = False
    print len(ans.keys())
