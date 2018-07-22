
out = []
for i in range(20):
    out.append(map(int , raw_input().split()))

def find_max(ypos , xpos):
    global out 
    vals = [0]
    if(ypos - 3 >=  0):
        vals.append( (out[ypos ][xpos] * out[ypos -1 ][xpos] * out[ypos -2 ][xpos] * out[ypos -3 ][xpos] ) )
    if(ypos + 3 < len(out) ):
        vals.append( (out[ypos ][xpos] * out[ypos +1 ][xpos] * out[ypos +2 ][xpos] * out[ypos +3 ][xpos] ) )

    if(xpos - 3 >=  0):
        vals.append( (out[ypos ][xpos] * out[ypos][xpos - 1] * out[ypos][xpos -2] * out[ypos][xpos - 3] ) )
    if(xpos + 3 < len(out) ):
        vals.append( (out[ypos ][xpos] * out[ypos ][xpos+1] * out[ypos][xpos+ 2] * out[ypos][xpos + 3] ) )

    if(xpos -1 >= 0 and ypos - 1 >= 0 and xpos + 2 <len(out) and ypos + 2 < len(out)  ):
        vals.append((out[ypos ][xpos] * out[ypos + 1 ][xpos+1] * out[ypos - 1][xpos - 1] * out[ypos + 2][xpos + 2] ))

    if(xpos -2 >= 0 and ypos - 2 >= 0 and xpos + 1 <len(out) and ypos + 1 < len(out)  ):
        vals.append((out[ypos ][xpos] * out[ypos + 1 ][xpos+1] * out[ypos - 1][xpos - 1] * out[ypos - 2][xpos - 2] ))
    
    if(xpos - 2 >= 0 and ypos - 1 >= 0 and xpos + 2 <len(out) and ypos + 2 < len(out)  ):
        vals.append((out[ypos ][xpos] * out[ypos + 1 ][xpos-1] * out[ypos - 1][xpos + 1] * out[ypos + 2][xpos - 2] ))

    if(xpos -2 >= 0 and ypos - 2 >= 0 and xpos + 2 <len(out) and ypos + 1 < len(out)  ):
        vals.append((out[ypos ][xpos] * out[ypos + 1 ][xpos-1] * out[ypos - 1][xpos + 1] * out[ypos - 2][xpos + 2] ))

    return max(vals)

maxv = 0

for i in range(20):
    for j in range(20):
        maxv = max(maxv , find_max(i,j))


print maxv