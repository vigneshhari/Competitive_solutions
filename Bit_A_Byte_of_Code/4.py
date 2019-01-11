"""
7 3
Tsi
h%x
i #
sM
$a
#t%
ir!
"""

def check_alpha_numeric(val):
    return (97 <= ord(val) and ord(val) <= 122 ) or (48 <= ord(val) and ord(val) <= 57 ) or (65 <= ord(val) and ord(val) <= 90 )


nm = raw_input().split()

n = int(nm[0])

m = int(nm[1])

matrix = []

for _ in xrange(n):
    matrix_item = raw_input()
    matrix.append(matrix_item)


print matrix

string = ""



for i in xrange(m):
    for j in xrange(n):
        try:
            string += matrix[j][i]
        except:
            string += " "

ans = ""
i = 0
while (i < n*m ):
    adder = ""
    tans = ans
    try:
        while not check_alpha_numeric(string[i]):
            tans = tans + string[i]
            i +=1
            adder = " "
    except:
        ans = tans
        break
    ans = ans + adder
    ans = ans + string[i]
    i+=1
print ans
