size , rotations = map(int , raw_input().split(" "))
array = map(int , raw_input().split(" "))
out = []
for i in range(size):
    out.append( str(  array[(rotations + i ) % size]) ) 
print " ".join(out) 