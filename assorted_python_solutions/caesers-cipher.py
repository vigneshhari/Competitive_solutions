input()
inpstr = raw_input()
import string
lowercase = string.lowercase
uppercase = string.uppercase
shifter = input()
newletter = {}
for i,j in enumerate(lowercase):
    newletter[j] = lowercase[(shifter + i) % 26] 
for i,j in enumerate(uppercase):
    newletter[j] = uppercase[(shifter + i) % 26]
for k in inpstr:
    if( k not in newletter.keys()):
        newletter[k] = k 
print "".join([newletter[i] for i in inpstr])