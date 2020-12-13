size = input()
out = ""
for i in range(size):
    pos = list(raw_input())
    if("p" in pos):
        val = pos.index('p')
        if(i > size/2):
            out += "DOWN\n" * ( i - (size/2)  )
        if(i < size/2):
            out += "UP\n" * ( (size/2) - i)
        if(val > (size/2)):
            out += "RIGHT\n" * ( val - (size/2) )
        if(val < (size/2)):
            out += "LEFT\n" * ((size/2) - val)
print out[:-1]
