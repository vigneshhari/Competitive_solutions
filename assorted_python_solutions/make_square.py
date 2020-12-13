data = range(10,30)

width = 5
stri = ""

temp = 0

def pretty(lis):
    stri = ""
    for i in lis:
        stri += str(i) + " "
    return stri

def spacer(data):
    return "  " * int(data)

while temp < len(data):
    stri += pretty(data[temp : temp + 5])
    temp += 4
    stri += spacer(width*1.6)
    temp += width * 3 - 3

start = width + 1

temp_arr = [5,10]
looper = 0
current = 0
stri += "\n"
for i in range(width-2):
    while True:
        if(looper ==2):looper = 0
        current  += temp_arr[looper]
        stri += spacer( (width ) * 1.5 )
        if(current >= len(data)):break
        stri += str(data[current])
        looper+=1 
    stri += "\n"
    temp_arr[0] += 1
    temp_arr[1] -= 2
    looper = 0
    current = 0

temp = width * 2 -2
while temp < len(data):
    stri += spacer(width * 1.6)
    stri += pretty(data[temp : temp + 5])
    temp += 4
    temp += width * 3 - 3

print stri