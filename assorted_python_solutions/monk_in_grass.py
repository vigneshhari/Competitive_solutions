#for code monk .. P2 Q4


def sum_row_col(arr,time):
        row,col = [],[]
        for x in range(0,time):
            r,c=0,0
            for y in range(0,time):
               r = r + data[x][y]
               c = c + data[y][x]
            row.append(r)
            col.append(c)
        return [row,col]

for i in range(0,input()):
    time,lim = (int(x) for x in raw_input().split(" "))
    data = []
    ans = 0
    for tim in range(0,time):
        data.append([int(x) for x in raw_input().split(" ")])
    row,col = sum_row_col(data,time)
    while lim != 0:
        lim-=1
        mc = min(col)
        mr = min(row)
        if(mc == mr):
            if(sum(col) < sum(row)):
                ans += mc
                col[col.index(mc)] += time
                for tim in range(0,time):row[tim] +=1
            else:
                ans += mr
                for tim in range(0,time):col[tim] +=1
                row[row.index(mr)] += time
        elif(mc < mr):
            ans += mc
            col[col.index(mc)] += time
            for tim in range(0,time):row[tim] +=1
        else:
            ans += mr
            for tim in range(0,time):col[tim] +=1
            row[row.index(mr)] += time
    print ans
