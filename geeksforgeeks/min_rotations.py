
#Python3

'''

2
222 333
2345 5432

'''


for _ in range(int(input())):
    startl , endl = input().split()
    startl = list(map(int , list(startl)))
    endl = list(map(int, list(endl)))
    ans = 0
    for i in range(len(startl)):
        startpos = startl[i]
        endpos = endl[i]
        ans += min( abs(endpos - startpos) , ((endpos + 10) - startpos)   % 10  , ((startpos + 10) - endpos)   % 10 )
    print(ans)
