data = raw_input().split(" ")
wl = int(data[0])
ar = int(data[1])
print type(wl),type(ar)
def suf_area(l,b,h):
    return (2*l*b) + (2*b*h) + (2*l*h)
def vol(n):
    return n[0]*n[1]*n[2]
def approxans(val,wl):
    if(val <= wl and val + .1 >= wl):return True
    return False
max_val = [0] * 3
lc = 0.01
h,l,b=0,0,0
loop = 0
while True:
    loop+=1
    print "CH " ,loop
    l = l + 0.1
    if(4*(b+l+h) > wl):break
    while True:
        h = h +  0.1
        if(4*(b+l+h) > wl):h=0;break
        while True:
            b = b+0.1
            if((4*(b+l+h)) != float(wl)):
                if((4*(b+l+h)) > wl):print "brocken at" , l , " " , h , " " , b;b=0;break
            print l ," ",h," ",b
            if(vol(max_val) < vol([l,b,h]) and approxans(suf_area(l,b,h),ar) and approxans(4*(l+b+h),wl)):
                print l,b,h
                max_val = [l,b,h]
print vol(max_val)
print max_val