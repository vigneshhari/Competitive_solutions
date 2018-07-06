largest = 0
for i in xrange(1,10000):
	multiplication = ''
	integer = 1
	while len(multiplication) < 9:	
		multiplication += str(i*integer)		
		integer += 1
	if ((len(multiplication) == 9) and (len(set(multiplication)) == 9) 
		and ('0' not in multiplication)):
		if int(multiplication) > largest:
			largest = int(multiplication)
print largest