def check(it,lister):
    ans = 0;
    for i in lister:
        if(i == it):
            ans+=1
    return ans

a = input()
for i in range(0,a):
    num = input()
    lis = []
    for i in range(0,num):
        lis.append(raw_input())
    val = 0
    done = []
    for i in lis:
        if(i not in done):
            done.append(i)
            val = check(i,lis) + val - 1
    print val