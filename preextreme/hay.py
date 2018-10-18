val = input()
ans = []
for i in range(1,1000):
    for j in range(1,1000):
        for k in range(1,1000):
            A,B,C = i - 1 , j -2 , k - 2
            if(A * B * C == val and A > 0 and B> 0 and C > 0  ):
                ans.append( (i*j*k) - 4 )
print min(ans) , max(ans)
